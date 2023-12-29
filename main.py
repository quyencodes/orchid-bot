# pip imports
import discord
from datetime import datetime, timezone, timedelta
from discord.ext import commands # ext = extensions

# local imports
from secret import *
from embed import footer, colour, images
from utils import disclaimer, default

"""
Initialize our Discord bot
@param {string} prefix - The prefix we want our discord bot to look out for, for commands
@return {} - void
"""
intents = discord.Intents.all()  # or specify the intents you need
client = commands.Bot(command_prefix='!', intents=intents)

# States of certain commands
ursus_state = True
"""
Called when the client is done preparaing the data received from Discord
"""
@client.event
async def on_ready():
  print(f"{client.user.name} Bot is currently running on localhost.")
  print("-----------------------------")

"""
Called when user types in !hello in the discord text-channels
"""
@client.command()
async def hello(ctx):
  await ctx.send(default.message)

@client.command()
async def ursus(ctx):
  if not ursus_state:
    await ctx.send(default.message)
    return

  # Get the current UTC time (YYYY-MM-DD HH:MM:SS +ms)
  utc_now = datetime.now(timezone.utc)

  # Set the time to UTC +/- time specified
  utc_plus1 = utc_now.replace(hour=1, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M:%S %z')
  utc_plus5 = utc_now.replace(hour=5, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M:%S %z')
  utc_minus6 = utc_now.replace(hour=18, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M:%S %z')
  utc_minus2 = utc_now.replace(hour=22, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M:%S %z')

  # Native function to convert UTC string (YYYY-MM-DD HH:MM:SS +0000) to unix time
  unix1 = convert_to_unix_time(utc_plus1)
  unix2 = convert_to_unix_time(utc_plus5)
  unix3 = convert_to_unix_time(utc_minus6)
  unix4 = convert_to_unix_time(utc_minus2)

  title = 'Ursus 2x Time / Golden Time'
  interval1 = f"{discord_timestamp(unix1, 'short_time')} - {discord_timestamp(unix2, 'short_time')}"
  interval2 = f"{discord_timestamp(unix3, 'short_time')} - {discord_timestamp(unix4, 'short_time')}"

  embed = discord.Embed(title=title, colour=colour.light_blue)
  embed.add_field(name='Description', value='Ursus is a unique boss that allows up to 18 players to join the fight. In MapleStory Reboot, Ursus is popular because of the daily mesos player(s) can receive. At special times of the day, the amount of mesos you earn from Ursus is doubled.',inline=False)
  embed.add_field(name='Ursus Golden Time Slot 1', value=interval1, inline=True)
  embed.add_field(name='Ursus Golden Time Slot 2', value=interval2, inline=True)
  embed.set_image(url=images.ursus)
  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)

  # Send back to discord text-channel
  await ctx.send(embed=embed)


"""
Discord embed creator: https://embed.dan.onl/
"""
@client.command()
async def classes(ctx):
  title = 'MapleStory Classes Discord'
  description = 'Here is a Reddit thread containing links to every class Discord server. Please be aware that these are run by members of the community and are not tied to the Official MapleStory team and MapleStory Discord server'

  embed = discord.Embed(title=title, description=description, colour=colour.light_blue)
  embed.add_field(name="Reddit Thread", value="https://www.reddit.com/r/Maplestory/comments/13jji1j/master_list_of_class_discord_links_for_savior_and/")
  embed.set_image(url=images.classes)
  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)
  await ctx.send(embed=embed)

@client.command()
async def bossmule(ctx):
  title = 'Boss Mule'
  description = 'Here is a YouTube video on how to equip and prepare a boss mule for MapleStory Reboot. The video was created in 2022 but the Orchid Bot team still believes a lot of the information present is valid.'
  embed = discord.Embed(title=title, colour=colour.light_blue)
  embed.add_field(name="Description", value=description, inline=False)
  embed.add_field(name="YouTube Video", value="https://www.youtube.com/watch?v=qh_h1FaLZpc", inline=False)
  embed.add_field(name="Disclaimer", value=disclaimer.INFO_DISCLAIMER, inline=False)
  embed.set_image(url=images.boss_mule)
  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)
  await ctx.send(embed=embed)

@client.command()
async def sunnysunday(ctx):
  pass

@client.command()
async def invite(ctx):
  title = 'Recommended MapleStory Discord Servers'
  embed = discord.Embed(title=title, colour=colour.light_blue)
  embed.add_field(name="MapleStory Official Discord Server", value="Join the Official MapleStory Discord Server for communities with Reboot and non-Reboot, official announcements, NX updates and more!\n\nhttps://discord.gg/maplestory", inline=False)

  embed.add_field(name="Reboot Central", value="Join the MapleStory Reboot Community Server, a hub for all MapleStory Class discord servers. After joining and specifiying your Channels & Roles, you'll get exclusive access to a variety of class specific information! \n\nhttps://discord.gg/rebootcentral", inline=False)

  embed.set_image(url=images.new_age)
  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)
  await ctx.send(embed=embed)

@client.command()
async def creators(ctx):
  title = 'Recommended MapleStory Creators'
  main_embed = discord.Embed(title=title, colour=colour.light_blue)
  main_embed.add_field(name="Disclaimer", value=disclaimer.INFO_DISCLAIMER, inline=False)

  embed_creator1 = discord.Embed(colour=colour.light_blue)
  embed_creator1.set_author(name="x3TheAran59", url="https://www.youtube.com/@x3TheAran59/videos")
  embed_creator1.add_field(name="About", value="Steve creates MapleStory content featuring the latest KMS (Korean MapleStory) and KMST (Korean MapleStory Testpia - Test Server) updates and gameplay. *GMS generally receives KMS updates 6 months subsequently.")
  embed_creator1.add_field(name="Links", value="https://www.youtube.com/@x3TheAran59/videos")
  embed_creator1.set_thumbnail(url="https://yt3.googleusercontent.com/ytc/AIf8zZTpYxKa-cWKqo66Wwu5r7vliT3gvozcknV5nYOw-A=s176-c-k-c0x00ffffff-no-rj")
  embed_creator1.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)

  await ctx.send(embed=main_embed)
  await ctx.send(embed=embed_creator1)

@client.command()
async def liberation(ctx):
  await ctx.send(default.message)

@client.command()
async def archetype(ctx):
  explorers = discord.Embed()

  # cygnus = discord.Embed()
  # heroes = discord.Embed()
  # resistance = discord.Embed()
  # nova = discord.Embed()
  # sengoku = discord.Embed()
  # flora = discord.Embed()
  # anima = discord.Embed()
  # friendstory = discord.Embed()
  # child = discord.Embed()
  # other = discord.Embed()

@client.command()
async def abyssal(ctx):
  title = 'Join the Abyssal Expedition (2023)'
  embed = discord.Embed(title=title, colour=colour.light_blue)
  embed.add_field(name='MapleStory Official Patch Notes', value='See the official GMS patch notes for the Abyssal Expedition\n[Link](https://maplestory.nexon.net/news/88519/join-the-abyssal-expedition)', inline=False)
  embed.add_field(name='Abyssal Expedition Guide', value='Document guide for the Abyssal Expedition event. Created by MapleStory community member oSilent / ElysiumGMS \n[Link](https://docs.google.com/document/d/1X7L6hxmweLghxXa82BjLrzu-od8D9RQYrp9m6Ha1ano/preview)\n', inline=False)
  embed.add_field(name='Abyssal Expedition Daily Calculator', value='Spreadsheet daily reference for the Abyssal Expedition event. Created by MapleStory community member oSilent / ElysiumGMS \n[Link](https://docs.google.com/spreadsheets/d/1MwrYUe5xmbdIEZ9-3SOxjZ8GBzGu56o4/edit?usp=sharing&ouid=101090533765814226839&rtpof=true&sd=true)\n', inline=False)

  embed.set_image(url=images.abyssal)
  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)
  await ctx.send(embed=embed)

"""
@param - Unix time formatted string
@return - Returns a dynamic date-time display in the discord text-channel
"""
def discord_timestamp(unix, format):
  # Discord Timestamp Formatting - https://gist.github.com/LeviSnoot/d9147767abeef2f770e9ddcd91eb85aa
  formatting = {
    'default': '',
    'short_time': 't',
    'long_time': 'T',
    'short_date': 'd',
    'long_date': 'D',
    'short_both': 'f',
    'long_both': 'F',
    'relative': 'R'
  }
  return f"<t:{unix}:{formatting[format]}>"

"""
@param - Takes in the UTC date and time of interest
@return - Returns unix formatted version of time
"""
def convert_to_unix_time(time_str):
    # Parse the input string to a datetime object
    dt_object = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S %z")

    # Convert to Unix timestamp
    unix_timestamp = int(dt_object.timestamp())
    return unix_timestamp

client.run(API_TOKEN)