import asyncio
import discord
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
client = discord.Client()

token = "Nzg5NzMwNzcxNDcxNjk1OTIy.X92UGA.LSVkffyPtLDtVvSvjBAHsOhutL8"

@client.event
async def on_ready():
    print("Logged in as ")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    url = "http://ncov.mohw.go.kr/"
    print (url)
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    tmpContent = bsObject.find_all("span", {"class":"num"})[0].text
    tmpContent12 = bsObject.find_all("span", {"class":"before"})[0].text
    tmpContent1 = bsObject.find_all("span", {"class":"num"})[1].text
    tmpContent13 = bsObject.find_all("span", {"class":"before"})[1].text
    tmpContent2 = bsObject.find_all("span", {"class":"num"})[2].text
    tmpContent14 = bsObject.find_all("span", {"class":"before"})[2].text
    tmpContent3 = bsObject.find_all("span", {"class":"num"})[3].text
    tmpContent15 = bsObject.find_all("span", {"class":"before"})[3].text
                            
    if message.author.bot: 
        return None 
    id = message.author.id 
    channel = message.channel
    if message.content.startswith('!누적'):
        embed=discord.Embed(title="코로나19 누적 확진 수", color=0x00fbff)
        embed.add_field(name="누적현황", value=str(tmpContent[4:]), inline=True)
        embed.add_field(name="(전일대비)", value=str(tmpContent12[4:]), inline=True)
        await channel.send(embed=embed)
        return
        url = "http://ncov.mohw.go.kr/"
    print (url)
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    tmpContent = bsObject.find_all("span", {"class":"num"})[0].text
    tmpContent12 = bsObject.find_all("span", {"class":"before"})[0].text
    tmpContent1 = bsObject.find_all("span", {"class":"num"})[1].text
    tmpContent13 = bsObject.find_all("span", {"class":"before"})[1].text
    tmpContent2 = bsObject.find_all("span", {"class":"num"})[2].text
    tmpContent14 = bsObject.find_all("span", {"class":"before"})[2].text
    tmpContent3 = bsObject.find_all("span", {"class":"num"})[3].text
    tmpContent15 = bsObject.find_all("span", {"class":"before"})[3].text
                            
    if message.author.bot: 
        return None 
    id = message.author.id 
    channel = message.channel
    if message.content.startswith('!격리해제'):
        embed=discord.Embed(title="코로나19 격리해제자 수", color=0x00fbff)
        embed.add_field(name="격리해제 수", value=str(tmpContent1), inline=True)
        embed.add_field(name="(전일대비)", value=str(tmpContent13), inline=True)
        await channel.send(embed=embed)
        return
    url = "http://ncov.mohw.go.kr/"
    print (url)
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    tmpContent = bsObject.find_all("span", {"class":"num"})[0].text
    tmpContent12 = bsObject.find_all("span", {"class":"before"})[0].text
    tmpContent1 = bsObject.find_all("span", {"class":"num"})[1].text
    tmpContent13 = bsObject.find_all("span", {"class":"before"})[1].text
    tmpContent2 = bsObject.find_all("span", {"class":"num"})[2].text
    tmpContent14 = bsObject.find_all("span", {"class":"before"})[2].text
    tmpContent3 = bsObject.find_all("span", {"class":"num"})[3].text
    tmpContent15 = bsObject.find_all("span", {"class":"before"})[3].text
                            
    if message.author.bot: 
        return None 
    id = message.author.id 
    channel = message.channel
    if message.content.startswith('!치료중'):
        embed=discord.Embed(title="코로나19 치료중 (격리중) 수", color=0x00fbff)
        embed.add_field(name="치료중 (격리중) 수", value=str(tmpContent2), inline=True)
        embed.add_field(name="(전일대비)", value=str(tmpContent14), inline=True)
        await channel.send(embed=embed)
        return
    url = "http://ncov.mohw.go.kr/"
    print (url)
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    tmpContent = bsObject.find_all("span", {"class":"num"})[0].text
    tmpContent12 = bsObject.find_all("span", {"class":"before"})[0].text
    tmpContent1 = bsObject.find_all("span", {"class":"num"})[1].text
    tmpContent13 = bsObject.find_all("span", {"class":"before"})[1].text
    tmpContent2 = bsObject.find_all("span", {"class":"num"})[2].text
    tmpContent14 = bsObject.find_all("span", {"class":"before"})[2].text
    tmpContent3 = bsObject.find_all("span", {"class":"num"})[3].text
    tmpContent15 = bsObject.find_all("span", {"class":"before"})[3].text
                            
    if message.author.bot: 
        return None 
    id = message.author.id 
    channel = message.channel
    if message.content.startswith('!사망자'):
        embed=discord.Embed(title="코로나19 사망자 수", color=0x00fbff)
        embed.add_field(name="사망자 수", value=str(tmpContent3), inline=True)
        embed.add_field(name="(전일대비)", value=str(tmpContent15), inline=True)
        await channel.send(embed=embed)
        return
    print (url)
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    tmpContent = bsObject.find_all("span", {"class":"num"})[0].text
    tmpContent12 = bsObject.find_all("span", {"class":"before"})[0].text
    tmpContent1 = bsObject.find_all("span", {"class":"num"})[1].text
    tmpContent13 = bsObject.find_all("span", {"class":"before"})[1].text
    tmpContent2 = bsObject.find_all("span", {"class":"num"})[2].text
    tmpContent14 = bsObject.find_all("span", {"class":"before"})[2].text
    tmpContent3 = bsObject.find_all("span", {"class":"num"})[3].text
    tmpContent15 = bsObject.find_all("span", {"class":"before"})[3].text
                            
    if message.author.bot: 
        return None 
    id = message.author.id 
    channel = message.channel
    if message.content.startswith('!코로나'):
        embed=discord.Embed(title="코로나19 종합 현황", color=0x00fbff)
        embed.add_field(name="1. 누적현황", value=str(tmpContent[4:]), inline=False)
        embed.add_field(name="(전일대비)", value=str(tmpContent12[4:]), inline=False)
        embed.add_field(name="2. 격리해제 수", value=str(tmpContent1[4:]), inline=False)
        embed.add_field(name="(전일대비)", value=str(tmpContent13), inline=False)
        embed.add_field(name="3. 치료중 (격리중) 수", value=str(tmpContent2), inline=False)
        embed.add_field(name="(전일대비)", value=str(tmpContent14), inline=False)
        embed.add_field(name="4. 사망자 수", value=str(tmpContent3), inline=False)
        embed.add_field(name="(전일대비)", value=str(tmpContent15), inline=False)
        embed.set_footer(text="모든 통계는 아래 사이트에서 제공됩니다.\nhttp://ncov.mohw.go.kr/")
        await channel.send(embed=embed)
        return
    print (url)
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    tmpContent = bsObject.find_all("span", {"class":"num"})[0].text
    tmpContent12 = bsObject.find_all("span", {"class":"before"})[0].text
    tmpContent1 = bsObject.find_all("span", {"class":"num"})[1].text
    tmpContent13 = bsObject.find_all("span", {"class":"before"})[1].text
    tmpContent2 = bsObject.find_all("span", {"class":"num"})[2].text
    tmpContent14 = bsObject.find_all("span", {"class":"before"})[2].text
    tmpContent3 = bsObject.find_all("span", {"class":"num"})[3].text
    tmpContent15 = bsObject.find_all("span", {"class":"before"})[3].text
    tmpContent4 = bsObject.find_all("span", {"class":"data"})[0].text
    tmpContent16 = bsObject.find_all("span", {"class":"data"})[1].text
    
                            
    if message.author.bot: 
        return None 
    id = message.author.id 
    channel = message.channel
    if message.content.startswith('!통계'):
        embed=discord.Embed(title="코로나19 통계", color=0x00fbff)
        embed.add_field(name="국내 발생", value=str(tmpContent4), inline=True)
        embed.add_field(name="해외 유입 ", value=str(tmpContent16), inline=True)
        await channel.send(embed=embed)
        return
    if message.author.bot: 
        return None 
    id = message.author.id 
    channel = message.channel
    if message.content.startswith('!명령어'):
        embed=discord.Embed(title="코로나19봇 명령어", color=0x00fbff)
        embed.add_field(name="!누적", value="누적 확진자 수", inline=True)
        embed.add_field(name="!격리해제 ", value="격리해제자 수", inline=True)
        embed.add_field(name="!치료중 ", value="치료중 (격리중) 수", inline=True)
        embed.add_field(name="!사망자 ", value="사망자 수", inline=True)
        embed.add_field(name="!코로나 ", value="코로나 전체 집계", inline=True)
        embed.add_field(name="!통계 ", value="일일 확진자 통계\n제작자 : 석영", inline=True)
        embed.add_field(name="제작자 ", value="석영", inline=True)
        await channel.send(embed=embed)
        

client.run(token)
