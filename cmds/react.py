import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options

intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def picA(self,ctx,*,msg):
        


        PATH="C:/Users/user/Desktop/chromedriver/chromedriver.exe"

        driver = webdriver.Chrome(PATH)

        driver.get("https://www.google.com/imghp")




        search = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="sbtc"]/div/div[2]/input'))
        )

        search.send_keys(msg)
        time.sleep(1)
        search.send_keys(Keys.RETURN)


        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,'rg_i'))
        )


        imgs = driver.find_elements(By.CLASS_NAME,'rg_i')
        pictures=[]

        for img in imgs:
            picture=img.get_attribute("src")
            if picture != None and  'https' in picture:
                pictures.append(picture)


        driver.quit()
        await ctx.send(random.choice(pictures))
        

        
                    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def ytA(self,ctx,*,msg):
        


        chrome_options = Options() 
        chrome_options.add_argument('--headless')  # 啟動Headless 無頭


        PATH="C:/Users/user/Desktop/chromedriver/chromedriver.exe"

        driver = webdriver.Chrome(PATH,chrome_options=chrome_options)

        driver.get(f"https://www.youtube.com/results?search_query={msg}")

        yts = driver.find_elements(By.CLASS_NAME,'yt-simple-endpoint')

        videos=[]


        for yt in yts:
            video=yt.get_attribute("href")
            if video != None and  'watch' in video:
                if video not in videos:
                    videos.append(video)
        driver.quit()
        await ctx.send(random.choice(videos))

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def ytB(self,ctx,*,msg):
        

        chrome_options = Options() 
        chrome_options.add_argument('--headless')  # 啟動Headless 無頭


        PATH="C:/Users/user/Desktop/chromedriver/chromedriver.exe"

        driver = webdriver.Chrome(PATH,chrome_options=chrome_options)

        driver.get(f"https://www.youtube.com/results?search_query={msg}")

        yts = driver.find_elements(By.CLASS_NAME,'yt-simple-endpoint')

        videos=[]


        for yt in yts:
            video=yt.get_attribute("href")
            if video != None and  'watch' in video:
                if video not in videos:
                    videos.append(video)
        driver.quit()
        await ctx.send(videos[0])


def setup(bot):
    bot.add_cog(React(bot))