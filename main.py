# pip imports
import discord
import os
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta
from discord.ext import commands  # ext = extensions

# local imports
from embed import footer, images
from utils import disclaimer, default
from functions import timestamp
from data import miracletime

load_dotenv()

"""
Initialize our Discord bot
@param {string} prefix - The prefix we want our discord bot to look out for, for commands
@return {} - void
"""
intents = discord.Intents.all()  # or specify the intents you need
client = commands.Bot(command_prefix='!', intents=intents)

# States of certain commands
ursus_state = True
dmt_state = False
"""
Called when the client is done preparaing the data received from Discord
"""


@client.event
async def on_ready():
  print(f'{client.user.name} Bot has connected to Discord!')
  print("-----------------------------")

"""
@return - Returns the Discord timestamp for Ursus in UTC
"""


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

  embed = discord.Embed(title=title, colour=discord.Color.green())
  embed.add_field(name='Description', value='Ursus is a unique boss that allows up to 18 players to join the fight. In MapleStory Reboot, Ursus is popular because of the daily mesos player(s) can receive. At special times of the day, the amount of mesos you earn from Ursus is doubled.', inline=False)
  embed.add_field(name='Ursus Golden Time Slot 1 (your timezone)',
                  value=interval1, inline=True)
  embed.add_field(name='Ursus Golden Time Slot 2 (your timezone)',
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
    title=title, description=description, colour=discord.Color.green())
  embed.add_field(name="Reddit Thread",
                  value="https://www.reddit.com/r/Maplestory/comments/13jji1j/master_list_of_class_discord_links_for_savior_and/")
  embed.set_image(url=images.classes)
  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)
  await ctx.send(embed=embed)


@client.command()
async def bossmule(ctx):
  title = 'Boss Mule'
  description = 'Here is a YouTube video on how to equip and prepare a boss mule for MapleStory Reboot. The video was created in 2022 but the Orchid Bot team still believes a lot of the information present is valid.'
  embed = discord.Embed(title=title, colour=discord.Color.green())
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
  embed = discord.Embed(title=title, colour=discord.Color.green())
  embed.add_field(name="MapleStory Official Discord Server",
                  value="Join the Official MapleStory Discord Server for communities with Reboot and non-Reboot, official announcements, NX updates and more!\n\nhttps://discord.gg/maplestory", inline=False)

  embed.add_field(name="Reboot Central", value="Join the MapleStory Reboot Community Server, a hub for all MapleStory Class discord servers. After joining and specifiying your Channels & Roles, you'll get exclusive access to a variety of class specific information! \n\nhttps://discord.gg/rebootcentral", inline=False)

  embed.set_image(url=images.new_age)
  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)
  await ctx.send(embed=embed)


@client.command()
async def creators(ctx):
  title = 'Recommended MapleStory Creators'
  main_embed = discord.Embed(title=title, colour=discord.Color.green())
  main_embed.add_field(
    name="Disclaimer", value=disclaimer.INFO_DISCLAIMER, inline=False)

  embed_creator1 = discord.Embed(colour=discord.Color.green())
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
  embed = discord.Embed(title=title, colour=discord.Color.green())
  embed.add_field(name='Abyssal Expedition Guide',
                  value='Document guide for the Abyssal Expedition event. \n[Link](https://docs.google.com/document/d/1X7L6hxmweLghxXa82BjLrzu-od8D9RQYrp9m6Ha1ano/preview)\n', inline=False)
  embed.add_field(name='Abyssal Expedition Daily Calculator',
                  value='Spreadsheet daily reference for the Abyssal Expedition event. \n[Link](https://docs.google.com/spreadsheets/d/1MwrYUe5xmbdIEZ9-3SOxjZ8GBzGu56o4/edit?usp=sharing&ouid=101090533765814226839&rtpof=true&sd=true)\n', inline=False)
  embed.add_field(
    name='', value='Created by MapleStory community member oSilent / ElysiumGMS\n> For more information see the [MapleStory Official Patch Notes](https://maplestory.nexon.net/news/88519/join-the-abyssal-expedition)', inline=False)

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

"""
@param {ctx} - Short for context. Used by discord.ext.commands and includes information like who executed the command, where it was executed and so on.
@return - Full list of commands via Embed
"""
@client.command()
async def commands(ctx):
  title = 'Frequently Used Commands',
  description = 'Here is a list of most common commands most people run with our bot!'
  commands = {
    '!utc': 'What time is it right now in UTC?',
    '!bossprequests': 'What are the prequests I have to do for the bosses?',
    '!ursus': 'When is Ursus 2x Time / Golden Time?',
    '!dmt': 'When is the next Double Miracle Time?',
    '!classes': 'How do I get access to my class\' discord?',
    '!archetype': 'Which classes share Cash Shop inventories?',
  }
  master_list = {
    '!viproyal': 'Where can I find the VIP Royal Hair / Face coupon choices?',
    '!scrapyard': 'What are the useful resources for Scrapyard weeklies?',
    '!abyssal': 'What is the Abyssal Expedition event?',
    '!creators': 'What MapleStory creators do you recommend?',
    '!invite': 'Permanent invite link for MapleStory\'s Official Discord Server(s)',
    '!bossmule': 'How should I gear my boss mules?',
  }
  embed = discord.Embed(title=title, description=description, colour=discord.Color.green())

  for command, explanation in commands.items():
    embed.add_field(name='', value=f"`{command}` {explanation}", inline=False)

  embed.add_field(name='', value='> For a full list of our commands, please see our website [here](https://github.com/quyencodes/orchid-bot)')
  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)

  await ctx.send(embed=embed)

"""
@return - Returns the resources needed for Scrapyard weeklies
"""


@client.command()
async def scrapyard(ctx):
  data = {
    'title': 'Scrapyard',
    'description': 'lorem ipsum huynh asdadjw medlc dsuuem cdcdfasddsaj',
    'field1': {
      'name': 'Scrapyard Weekly Quest Guide',
      'value': 'Visit the guide and scroll down to the Overall Recommendations section. Expand the Simplified drop-down menu and follow the instructions there:\n[Link](https://strategywiki.org/wiki/MapleStory/Towns/Scrapyard)'
    },
  }

  embed = discord.Embed(
    title=data['title'], description=data['description'], colour=discord.Color.green())

  for key in data:
    if key in ['field1']:
      embed.add_field(name=data[key]['name'], value=data[key]['value'])

  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)

  await ctx.send(embed=embed)

"""
@return - Returns the prequest information for bosses in MapleStory
"""


@client.command()
async def bossprequests(ctx):
  data = {
    'title': 'MapleStory Boss Prequests',
    'description': 'Here is a list of resources to complete the prequest for each boss!',
    'prequest_data': {
      'Barlog': {
        'link': None
      },
      'Zakum': {
        'link': None
      },
      'Hilla': {
        'link': None
      },
      'Ursus': {
        'link': '[DigitalTQ](https://www.digitaltq.com/maplestory-ursus-guide)'
      },
      'Magnus': {
        'link': '[DigitalCrowns](https://thedigitalcrowns.com/magnus-prequest-guide-updated-maplestory/)'
      },
      'OMNI-CLN': {
        'link': '[YouTube Link](https://www.youtube.com/watch?v=UDc1cuQC_Ac)'
      },
      'Papalatus': {
        'link': '[YouTube Link](https://www.youtube.com/watch?v=f9UdUnyJ4-o)'
      },
      'Root Abyss': {
        'link': '[YouTube Link](https://www.youtube.com/watch?v=5dWMN4NGaQQ)'
      },
      'Von Leon': {
        'link': '[YouTube Link](https://www.youtube.com/watch?v=2-f2tHoFypA)'
      },
      'Horntail': {
        'link': '[MapleWiki](https://maplestory.fandom.com/wiki/Quests/41/(Horntail)_Certificate_of_the_Dragon_Squad)'
      },
      'Arkarium': {
        'link': '[YouTube Link](https://www.youtube.com/watch?v=wfGRei71ZsY)'
      },
      'Pink Bean': {
        'link': '[Digital Crowns](https://thedigitalcrowns.com/pink-bean-prequest-guide-updated-maplestory/)'
      },
      'Cygnus': {
        'link': '[DigitalTQ](https://www.digitaltq.com/maplestory-cygnus-prequest-guide)'
      },
      'Guardian Angel Slime': {
        'link': '[YouTube Link](https://www.youtube.com/watch?v=MjdYWrvw4iQ)'
      },
      'Gollux': {
        'link': '[YouTube Link](https://www.youtube.com/watch?v=S-HiKCTHh7k)'
      },
      'Ranmaru': {
        'link': '[YouTube Link](https://www.youtube.com/watch?v=lvF33nTRmeo)'
      },
      'Princess No': {
        'link': '[YouTube Link](https://www.youtube.com/watch?v=zXKJYay-zSI&t=6s)'
      },
      'Akechi Mitsuhide': {
        'link': '[DigitalTQ](https://www.digitaltq.com/maplestory-akechi-mitsuhide-boss-prequest-the-asura-crisis)'
      },
      'Lotus': {
        'link': '1) Dimensional Mirror\n2) Ereve Conference Pavilion\n3) Interact with [Moco](https://maplestory.fandom.com/wiki/Moco)\n4) Black Heaven **(Complete All Acts)**'
      },
      'Damien': {
        'link': '1) Dimensional Mirror\n2) Ereve Conference Pavilion\n3) Interact with [Moco](https://maplestory.fandom.com/wiki/Moco)\n4) Heroes of Maple **(Complete Act 4)**'
      },
    },
  }

  embed = discord.Embed(
    title=data["title"], description=data["description"], colour=discord.Color.green())

  for boss in data['prequest_data']:
    current = data['prequest_data'][boss]

    value = current['link'] if current['link'] is not None else 'No Prequests'

    embed.add_field(name=boss, value=value, inline=True)

  embed.add_field(name='Other', value="Bosses such as **Lucid**, **Will**, **Gloom**, **Verus Hilla**, **Black Mage**, **Chosen Seren**, **Kalos**, and **Kaling** are unlocked as you progress through the Arcane River and Grandis storyline", inline=False)
  embed.add_field(
    name='', value="> Last updated December 30, 2023", inline=False)
  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)

  await ctx.send(embed=embed)


@client.command()
async def bucc(ctx):
  title = 'Buccaneer Class Infographic 2023/2024'
  embed = discord.Embed(title=title, color=discord.Color.green())
  embed.set_image(url="https://cdn.discordapp.com/attachments/1175225470749507685/1175235598336929823/buccaneer_info.png?ex=65a1dd71&is=658f6871&hm=3ef2f5d952297787ccd2c54d0e068a02d38437ac38da9450630fc78a64d2d6d6&")
  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)

  await ctx.send(embed=embed)

"""
@return - Returns the return
"""


@client.command()
async def reset(ctx):

  # daily reset timestamp
  utc_reset = datetime.now(timezone.utc).replace(
    hour=23, minute=59, second=59)

  utc_reset_timestamp = timestamp.utc_unix_timestamp(
    utc_reset.year, utc_reset.month, utc_reset.day, utc_reset.hour, utc_reset.minute, utc_reset.second)

  # sunday reset timestamp
  utc_monday = timestamp.get_day_of_week(
    'sunday').replace(hour=0, minute=0, second=0)

  utc_monday_timestamp = timestamp.utc_unix_timestamp(
    utc_monday.year, utc_monday.month, utc_monday.day, utc_monday.hour, utc_monday.minute, utc_monday.second)

  # wednesday reset timestamp
  utc_wednesday = timestamp.get_day_of_week(
    'wednesday').replace(hour=0, minute=0, second=0)

  utc_wednesday_timestamp = timestamp.utc_unix_timestamp(
    utc_wednesday.year, utc_wednesday.month, utc_wednesday.day, utc_wednesday.hour, utc_wednesday.minute, utc_wednesday.second)

  data = {
    "daily": {
      'name': "Daily",
      'value': f"> Reset is at {timestamp.discord_timestamp(utc_reset_timestamp, 'short_time')} ({timestamp.discord_timestamp(utc_reset_timestamp, 'relative')}).",
      'inline': False
    },
    "weekly_bosses": {
      'name': 'Weekly Bosses',
      'value': f"> Reset is at {timestamp.discord_timestamp(utc_wednesday_timestamp, 'short_time')} ({timestamp.discord_timestamp(utc_wednesday_timestamp, 'relative')}).",
      'inline': False
    },
    "weekly": {
      'name': 'Weekly Story Quests',
      'value': f"Scrapyard, Dark World Tree, and Arcane River weeklies reset\n> Reset is at {timestamp.discord_timestamp(utc_monday_timestamp, 'short_time')} ({timestamp.discord_timestamp(utc_monday_timestamp, 'relative')}).",
      'inline': False
    },
  }

  description = 'Timestamps are adjusted for your respective timezone'
  embed = discord.Embed(description=description, colour=discord.Color.green())

  for field in data:
    embed.add_field(name=data[field]['name'], value=data[field]
                    ['value'], inline=data[field]['inline'])

  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)

  await ctx.send(embed=embed)

"""

"""


@client.command()
async def utc(ctx):
  utc_now = datetime.now(timezone.utc)

  year = int(utc_now.year)
  month = int(utc_now.month)
  day = int(utc_now.day)
  hour = int(utc_now.hour)
  minute = int(utc_now.minute)
  second = int(utc_now.second)

  dt = datetime(year, month, day, hour, minute, second)

  embed = discord.Embed(
    title='', description=f"> The current time is: {timestamp.discord_timestamp(int(dt.timestamp()))} +UTC", colour=discord.Color.green())

  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)

  await ctx.send(embed=embed)


@client.command()
async def linkskills(ctx):
  data = {
    'title': 'Recommended Link Skills',
    'description': 'For best results please look at your Class\' discord for recommended link skills.',
    'training': [
      'Mercedes', 'Evan', 'Ark', 'Illium', 'Kain', 'Lara', 'Phantom', 'Kanna', 'Hayato', 'Kinesis', 'Demon Avenger'
    ],
    'bossing': [
      'Fury Unleashed', 'Phantom Instinct', 'Light Wash', 'Wild Rage', 'Judgment', 'Unfair Advantage', 'Spirit of Freedom', 'Solus', 'Terms and Conditions', 'Emperical Knowledge', 'Thief\'s Cunning', 'Focus Spirit'
    ]
  }
  embed = discord.Embed(title=data.title)
  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)

@client.command()
async def andrew(ctx):
  await ctx.send("ãndréw")

@client.command()
async def specialchars(ctx):
  data = {
    'title': 'Valid Special Characters in Maplestory',
    'description': 'lorem ipsum lorem ipsum lorem ipsum lorem ipsum',
    'vowels': {
      'a': ['à', 'á', 'â', 'ã', 'ä', 'å'],
      'e': ['é', 'ê', 'ë'],
      'i': ['ì', 'í', 'î', 'ï'],
      'o': ['ó', 'ô', 'õ', 'ö', 'ò', 'ø'],
      'u': ['ù', 'ú', 'û', 'ü'],
    }
  }

  embed = discord.Embed(
    title=data['title'], description=data['description'], colour=discord.Color.green())

  for vowel in data['vowels']:
    embed.add_field(
      name='', value=f"**{vowel}**: {' '.join(data['vowels'][vowel])}", inline=False)

  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)

  await ctx.send(embed=embed)


@client.command()
async def dragon(ctx):
  data = {
    'title': 'New Year: Legendary Blue Dragon Event',
    'details': [
      '- Hunt mobs for eggs (+/- 20 levels)',
        '- Use 8 eggs for a set of pulls (summoning)',
        '- 2 blue summons per __**event**__ **(MOST IMPORTANT PULLS)**',
        '- 1 gold summon per **day**',
        '- 3 red summon per **day**',
        '**Getting all 16 blue eggs:**',
        '  - 9 from hunting mobs (across event period)',
        '  - 7 from checking in every day (7 days of the event)',
        '**CHECK IN EVERY DAY FOR A BLUE EGG**',
        '  - Missing even one day means you can only pull blue summon 1 time (instead of 2)'
    ],
  }
  embed = discord.Embed(
    title=data['title'], colour=discord.Color.green())

  for bulletpoint in data['details']:
    embed.add_field(name='', value=bulletpoint, inline=False)

  embed.set_footer(text=footer.embed_footer, icon_url=footer.embed_image_url)

  await ctx.send(embed=embed)

# Get the token from GitHub Actions or from .env
api_token = os.environ.get('DISCORD_TOKEN') or os.getenv('DISCORD_TOKEN')

if api_token is None:
  raise ValueError('We have an error retrieving the API TOKEN from the enviornment variables.')

client.run(api_token)
