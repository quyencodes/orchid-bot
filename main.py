# pip imports
import discord
from datetime import datetime, timezone, timedelta
from discord.ext import commands  # ext = extensions

# local imports
from secret import *
from embed import footer, colour, images
from utils import disclaimer, default
from functions import timestamp
from data import miracletime

"""
Initialize our Discord bot
@param {string} prefix - The prefix we want our discord bot to look out for, for commands
@return {} - void
"""
intents = discord.Intents.all()  # or specify the intents you need
client = commands.Bot(command_prefix='!', intents=intents)

# States of certain commands
ursus_state = True
dmt_state = True
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
  utc_plus1 = utc_now.replace(
    hour=1, minute=0, second=0, microsecond=0)
  utc_plus5 = utc_now.replace(
    hour=5, minute=0, second=0, microsecond=0)
  utc_minus6 = utc_now.replace(
    hour=18, minute=0, second=0, microsecond=0)
  utc_minus2 = utc_now.replace(
    hour=22, minute=0, second=0, microsecond=0)

  # Convert to unix time
  unix1 = timestamp.utc_unix_timestamp(
    utc_plus1.year, utc_plus1.month, utc_plus1.day, utc_plus1.hour, utc_plus1.minute, utc_plus1.second)
  unix2 = timestamp.utc_unix_timestamp(
    utc_plus5.year, utc_plus5.month, utc_plus5.day, utc_plus5.hour, utc_plus5.minute, utc_plus5.second)
  unix3 = timestamp.utc_unix_timestamp(
    utc_minus6.year, utc_minus6.month, utc_minus6.day, utc_minus6.hour, utc_minus6.minute, utc_minus6.second)
  unix4 = timestamp.utc_unix_timestamp(
    utc_minus2.year, utc_minus2.month, utc_minus2.day, utc_minus2.hour, utc_minus2.minute, utc_minus2.second)

  # Build the embed
  title = 'Ursus 2x Time / Golden Time'
  interval1 = f"{timestamp.discord_timestamp(unix1, 'short_time')} - {timestamp.discord_timestamp(unix2, 'short_time')}"
  interval2 = f"{timestamp.discord_timestamp(unix3, 'short_time')} - {timestamp.discord_timestamp(unix4, 'short_time')}"

  embed = discord.Embed(title=title, colour=colour.light_blue)
  embed.add_field(name='Description', value='Ursus is a unique boss that allows up to 18 players to join the fight. In MapleStory Reboot, Ursus is popular because of the daily mesos player(s) can receive. At special times of the day, the amount of mesos you earn from Ursus is doubled.', inline=False)
  embed.add_field(name='Ursus Golden Time Slot 1',
                  value=interval1, inline=True)
  embed.add_field(name='Ursus Golden Time Slot 2',
                  value=interval2, inline=True)
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

  embed = discord.Embed(
    title=title, description=description, colour=colour.light_blue)
  embed.add_field(name="Reddit Thread",
                  value="https://www.reddit.com/r/Maplestory/comments/13jji1j/master_list_of_class_discord_links_for_savior_and/")
  embed.set_image(url=images.classes)
  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)
  await ctx.send(embed=embed)


@client.command()
async def bossmule(ctx):
  title = 'Boss Mule'
  description = 'Here is a YouTube video on how to equip and prepare a boss mule for MapleStory Reboot. The video was created in 2022 but the Orchid Bot team still believes a lot of the information present is valid.'
  embed = discord.Embed(title=title, colour=colour.light_blue)
  embed.add_field(name="Description", value=description, inline=False)
  embed.add_field(name="YouTube Video",
                  value="https://www.youtube.com/watch?v=qh_h1FaLZpc", inline=False)
  embed.add_field(name="Disclaimer",
                  value=disclaimer.INFO_DISCLAIMER, inline=False)
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
  embed.add_field(name="MapleStory Official Discord Server",
                  value="Join the Official MapleStory Discord Server for communities with Reboot and non-Reboot, official announcements, NX updates and more!\n\nhttps://discord.gg/maplestory", inline=False)

  embed.add_field(name="Reboot Central", value="Join the MapleStory Reboot Community Server, a hub for all MapleStory Class discord servers. After joining and specifiying your Channels & Roles, you'll get exclusive access to a variety of class specific information! \n\nhttps://discord.gg/rebootcentral", inline=False)

  embed.set_image(url=images.new_age)
  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)
  await ctx.send(embed=embed)


@client.command()
async def creators(ctx):
  title = 'Recommended MapleStory Creators'
  main_embed = discord.Embed(title=title, colour=colour.light_blue)
  main_embed.add_field(
    name="Disclaimer", value=disclaimer.INFO_DISCLAIMER, inline=False)

  embed_creator1 = discord.Embed(colour=colour.light_blue)
  embed_creator1.set_author(
    name="x3TheAran59", url="https://www.youtube.com/@x3TheAran59/videos")
  embed_creator1.add_field(name="About", value="Steve creates MapleStory content featuring the latest KMS (Korean MapleStory) and KMST (Korean MapleStory Testpia - Test Server) updates and gameplay. *GMS generally receives KMS updates 6 months subsequently.")
  embed_creator1.add_field(
    name="Links", value="https://www.youtube.com/@x3TheAran59/videos")
  embed_creator1.set_thumbnail(
    url="https://yt3.googleusercontent.com/ytc/AIf8zZTpYxKa-cWKqo66Wwu5r7vliT3gvozcknV5nYOw-A=s176-c-k-c0x00ffffff-no-rj")
  embed_creator1.set_footer(text=footer.embed_footer,
                            icon_url=footer.embed_image_url)

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
  embed.add_field(name='Abyssal Expedition Guide',
                  value='Document guide for the Abyssal Expedition event. Created by MapleStory community member oSilent / ElysiumGMS \n[Link](https://docs.google.com/document/d/1X7L6hxmweLghxXa82BjLrzu-od8D9RQYrp9m6Ha1ano/preview)\n', inline=False)
  embed.add_field(name='Abyssal Expedition Daily Calculator',
                  value='Spreadsheet daily reference for the Abyssal Expedition event. Created by MapleStory community member oSilent / ElysiumGMS \n[Link](https://docs.google.com/spreadsheets/d/1MwrYUe5xmbdIEZ9-3SOxjZ8GBzGu56o4/edit?usp=sharing&ouid=101090533765814226839&rtpof=true&sd=true)\n', inline=False)
  embed.add_field(
    name='', value='> For more information see the [MapleStory Official Patch Notes](https://maplestory.nexon.net/news/88519/join-the-abyssal-expedition)', inline=False)

  embed.set_image(url=images.abyssal)
  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)
  await ctx.send(embed=embed)


@client.command()
async def dmt(ctx):
  if not dmt_state:
    await ctx.send(default.message)
    return

  embed = discord.Embed(title='Double Miracle Time (DMT)',
                        description='Take advantage of ranking up your equipment potentials with MapleStory\'s Double Miracle Time event!', colour=discord.Color.green())
  embed.add_field(
    name=miracletime.weapon.get_name(), value=miracletime.weapon.get_discord_timestamp(), inline=False)
  embed.add_field(
    name=miracletime.overall.get_name(), value=miracletime.overall.get_discord_timestamp(), inline=False)
  embed.add_field(
    name=miracletime.shoes.get_name(), value=miracletime.shoes.get_discord_timestamp(), inline=False)
  embed.add_field(
    name=miracletime.accessories.get_name(), value=miracletime.accessories.get_discord_timestamp(), inline=False)
  embed.add_field(
    name=miracletime.gloves.get_name(), value=miracletime.gloves.get_discord_timestamp(), inline=False)
  embed.add_field(
    name=miracletime.hats.get_name(), value=miracletime.hats.get_discord_timestamp(), inline=False)

  embed.add_field(name="Frequently Asked Questions (FAQ)", value='**Which cubes should I use for DMT?**\nUse Bright Cubes to maximize your chances at ranking up an equip to legendary.\n\n**Do any cubes work?**\nIn Reboot, only cash cubes (Bright Cubes and Glowing Cubes) have increased rank-up chances during DMT.', inline=False)

  embed.add_field(
    name='', value='> For more information see [Patch Notes](https://maplestory.nexon.net/news/88447/miracle-winter-december-30-primary-weapons-secondary-equipment).', inline=False)
  embed.set_image(url=images.dmt)

  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)

  await ctx.send(embed=embed)


@client.command()
async def viproyal(ctx):
  title = 'VIP Royal Style Coupons'
  embed = discord.Embed(title=title, colour=discord.Color.green())

  embed.add_field(
    name='', value='> For more information see [VIP Royal Style Coupons](https://maplestory.nexon.net/micro-site/53407).')
  embed.set_image(
    url="https://preview.redd.it/b0a9bdk5cjc61.png?width=735&format=png&auto=webp&s=dd01dff4d596d5f862f4dbe199117f04c336062c")
  await ctx.send(embed=embed)


@client.command()
async def commands(ctx):
  embed = discord.Embed(colour=discord.Color.green())
  embed.add_field(
    name='', value='> For a full list of commands please visit our Official [Github Repo](https://github.com/quyencodes/orchid-bot).')
  await ctx.send(embed=embed)

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
