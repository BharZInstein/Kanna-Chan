import os
import discord
from discord.ext import commands
import random
from decouple import config


intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix='eri ', case_insensitive=True, intents=intents)
client.remove_command("help")


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name='Asheeshh Senpai'))
  print('Eri is Online.')

@client.command()
async def help(ctx):
  try:
    h = discord.Embed(
      title="NEED HELP?",
      description="Bot Creator: **ASHISH**",
      color=0x2e69f2,
    )
    h.add_field(
      name="__ABOUT__", 
      value=f"\nPrefix : `m.`\nEri Chan is a fun discord bot. She can play fun games with you, do some fun stuff and love you if you love her❤️.", 
      inline=False
    )
    h.add_field(
      name="__COMMANDS__",
      value=f"`love` Eri sends love to the person.\n`thank` Eri thanks the person.\n`befriend` Eri befriends the person.\n`say` Eri says what you want her to say.\n`arz` Eri sends a shayari for you.",
      inline=False
    )
    h.add_field(
      name="__GAMES__", value="Send `eri games` to see the list of games available and how to play them.", inline=False
    )
    h.add_field(
      name="__MISC__", value="Eri Chan also replies to you when you say `love you eri chan` or `hate you eri chan`.", inline=False
    )
    h.add_field(
      name="__SOURCE__", value="`m.source`", inline=False
    )
    await ctx.send(embed=h)
  except Exception as e:
    print(e)

@client.command()
async def source(ctx):
  await ctx.send("https://github.com/AsheeshhSenpai/Miko-Chan")
 

@client.command()
async def games(ctx):
  emb = discord.Embed(title="GAMES", color=0x2e69f2)
  emb.add_field(
    name="__TRUTH OR DARE__",
    value="Start a game of truth or dare using eri! For truth send `eri truth` and for dare send `eri dare`.",
    inline="False"
  )
  emb.add_field(
    name="__LOTTERY__",
    value="Start a game of lattery using eri. You will have to send three random numbers between 0 to 5 with space in between like `t.lottery 1 3 4`.",
    inline="False"
  )
  emb.add_field(
    name="__SHIP__",
    value="Ship two people, cus why not? Command: `eri ship`",
    inline="False"
  )
  await ctx.send(embed=emb)


@client.command()
async def love(ctx, mem: discord.User = None):
    if mem == None:
        mem = ctx.author
    emb = discord.Embed(title="", description=f"Eri sends love to {mem.mention} uwu", color=0x2e69f2)
    emb.set_image(url="https://i.pinimg.com/564x/58/1d/84/581d84005865fc6f74c8831ad50ade85.jpg")
    await ctx.send(embed=emb)

@client.command()
async def thank(ctx, mem: discord.User = None):
    if mem == None:
        mem = ctx.author
    emb = discord.Embed(title="", description=f"Arigatou {mem.mention} :)", color=0x2e69f2)
    emb.set_image(url="https://i.pinimg.com/564x/11/34/c6/1134c617f1e64a46364ff606b1c917a8.jpg")
    await ctx.send(embed=emb)


@client.command()
async def befriend(ctx, mem: discord.User = None):
  if mem == None:
    mem = ctx.author
  emb = discord.Embed(title="", description=f"Eri is your friend now uwu {mem.mention} :)", color=0x2e69f2)
  emb.set_image(url="https://i.pinimg.com/originals/69/28/d5/6928d57fd76c7822724abbae3800e354.gif")
  await ctx.send(embed=emb)

@client.command()
async def truth(ctx):
  truth = [
  "When was the last time you lied?",
  "When was the last time you cried?",
  "What's your biggest fear?",
  "What's your biggest fantasy?",
  "Do you have any fetishes?",
  "What's something you're glad your mum doesn't know about you?",
  "Have you ever cheated on someone?",
  "What's the worst thing you've ever done?",
  "What's a secret you've never told anyone?",
  "Do you have a hidden talent?",
  "Who was your first celebrity crush?",
  "What are your thoughts on politicians?",
  "What's the worst intimate experience you've ever had?",
  "Have you ever cheated in an exam?",
  "What's the most drunk you've ever been?",
  "Have you ever broken the law?",
  "What's the most embarrassing thing you've ever done?",
  "What's your biggest insecurity?",
  "What's the biggest mistake you've ever made?",
  "What's the most disgusting thing you've ever done?",
  "Who would you like to kiss in this server?",
  "What's the worst thing anyone's ever done to you?",
  "Have you ever had a run in with the law?",
  "What's your worst habit?",
  "What's the worst thing you've ever said to anyone?",
  "Have you ever peed in the shower?",
  "What's the strangest dream you've had?",
  "Have you ever been caught doing something you shouldn't have?",
  "What's the worst date you've been on?",
  "What's your biggest regret?",
  "What's the biggest misconception about you?",
  "Are you virgin?",
  "Why did your last relationship break down?",
  "Have you ever lied to get out of a bad date?",
  "What's the most trouble you've been in?"
]
  await ctx.send(f"Truth: {random.choice(truth)}")

@client.command()
async def dare(ctx):
  dare = [
  "Show the most embarrassing photo on your phone",
  "Show the last five people you texted and what the messages said",
  "Let the rest of the group DM someone from your Instagram account",
  "Eat a raw piece of garlic",
  "Do 100 squats",
  "Keep three ice cubes in your mouth until they melt",
  "Say something dirty to the person on your left",
  "Give a foot massage to the person on your right",
  "Put 10 different available liquids into a cup and drink it",
  "Yell out the first word that comes to your mind",
  "Give a lap dance to someone of your choice",
  "Remove four items of clothing",
  "Like the first 15 posts on your Facebook newsfeed",
  "Eat a spoonful of mustard",
  "Keep your eyes closed until it's your go again",
  "Send a text to the last person in your phonebook",
  "Show off your orgasm face",
  "Seductively eat a banana",
  "Empty out your wallet/purse and show everyone what's inside",
  "Do your best sexy crawl",
  "Pretend to be the person to your right for 10 minutes",
  "Eat a snack without using your hands",
  "Say two honest things about everyone else in the group",
  "Twerk for a minute",
  "Try and make the group laugh as quickly as possible",
  "Try to put your whole fist in your mouth",
  "Tell everyone an embarrassing story about yourself",
  "Try to lick your elbow",
  "Post the oldest selfie on your phone on Instagram Stories",
  "Tell the saddest story you know",
  "Howl like a wolf for two minutes",
  "Dance without music for two minutes",
  "Pole dance with an imaginary pole",
  "Let someone else tickle you and try not to laugh",
  "Put as many snacks into your mouth at once as you can"
]
  await ctx.send(f"Dare: {random.choice(dare)}")

@client.command(aliases=['lotto'])
async def lottery(ctx, *, guesses):
  '''Enter the lottery and see if you win!'''
  numbers = []
  for x in range(3):
    numbers.append(random.randint(1, 5))

  split = guesses.split(' ')
  if len(split) != 3:
    return await ctx.send('Please separate your numbers with a space, and make sure your numbers are between 0 and 5.')
  string_numbers = [str(i) for i in numbers]
  if split[0] == string_numbers[0] and split[1] == string_numbers[1] and split[2] == string_numbers[2]:
    await ctx.send(f'{ctx.author.mention} You won! Congratulations on winning the lottery!')
  else:
    await ctx.send(f"{ctx.author.mention} Better luck next time... You were one of the 124/125 who lost the lottery...\nThe numbers were `{', '.join(string_numbers)}`")

@client.command()
async def arz(ctx):
  shayari=[
      "*samundar ke kinare abadi nahi hoti, jisse pyar ho usse shadi nhi hoti..\n~SENSEI*",
      "*Ladki ka hasna adda hai, jo use pyaar samjhe vo gadha hai..\n~SENSEI*",
      "*tera bhi katega..\n~SENSEI*",
      "*kadu kata hai mere dost intejaar kar sabme batega,\nishq hua hai? intejaar kar tera bhi katega..\n~SENSEI*",
      "*ab na tere aana ki khushi rhi na tere jaane ka gam,\nvo jamana beet gya jab tere diwane the hum..\n~SENSEI*",
      "*Wo tumhen DP dikhaakar gumraah karegi,\nMagar Tum Aadhaar card par adde rehna..\n~KAKASHI*",
      "*yeh waqt bhi guzar jayega..\n~KAKASHI*",
      "*na reply chahiye\nna tera sath\nnikal meri zindagi se\nnahi karni tujhse koi baat..\n~SENSEI*"
    ]
  emb = discord.Embed(title="arz kiya hai..", description=f"{random.choice(shayari)}", color=0x2e69f2)
  await ctx.send(embed=emb)

@client.command()
async def say(ctx, *, message):
  emb = discord.Embed(title=message, description=f"by {ctx.author.mention}", color=0x2e69f2)
  await ctx.send(embed=emb)

@client.command()
async def ship(ctx, m1: discord.User = None, m2: discord.User = None):
  if m1 == None:
    m1 = ctx.author
    m2 = ctx.author
  elif m2 == None:
    m2 = m1
    m1 = ctx.author

  ship_list=[
    "Possible..",
    "Not in this life..",
    "Maybe..",
    "Best couple!",
    "Looks impossible..",
    "Fated partners..",
    "Should already be in this relationship.."
  ]

  await ctx.send(f"{m1.mention} X {m2.mention}\n{random.choice(ship_list)}")


@client.event
async def on_message(message):
  await client.process_commands(message)

  love_words=[
    "i love you eri chan",
    "love you eri chan",
    "eri chan i love you",
    "i love eri chan",
    "eri chan is love",
    "i love you eri",
    "love you eri"
  ]

  hate_words=[
    "i hate you eri chan",
    "hate you eri chan",
    "eri chan i hate you",
    "eri chan hate",
    "i hate you eri",
    "hate you eri"
  ]

  love_emb = discord.Embed(title="", description=f"Eri loves you too {message.author.mention} uwu", color=0x2e69f2)
  love_emb.set_image(url="https://i.pinimg.com/564x/58/1d/84/581d84005865fc6f74c8831ad50ade85.jpg")
  
  hate_emb = discord.Embed(title="", description=f"Eri is sad :( {message.author.mention} eri loves you :(", color=0x2e69f2)
  hate_emb.set_image(url="https://i.pinimg.com/originals/24/c5/0c/24c50cdc5844753daaaa713745e094a9.gif")

  if message.content.lower() in love_words:
    if message.author.id == 784363251940458516:
      await message.channel.send(f"{message.author.mention}\nEri loves asheesh too uwu..❤")
      await message.add_reaction('❤')
    else: 
      await message.channel.send(embed=love_emb)
      await message.add_reaction('❤')
  elif message.content.lower() in hate_words:
    if message.author.id == 784363251940458516:
      await message.channel.send(f"{message.author.mention}\nBut Eri loves asheesh..❤")
      await message.add_reaction('❤')
    else: 
      await message.channel.send(embed=hate_emb)
      await message.add_reaction('❤')

token = config("TOKEN")
client.run(token)
