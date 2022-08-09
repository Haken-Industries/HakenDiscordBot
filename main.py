from discord.ext.commands import cooldown, BucketType
import discord
from discord.utils import get
import random
import immortal
import os
import asyncio
import discord 
import aiohttp
from discord.ext import commands


token = os.getenv("token")
bot = commands.Bot(command_prefix = "*")
file33 = open("words.txt")
scors = []
file = open("database.txt","r")
for lines in file:
  lines = lines.replace(" \n","")
  try:
    lin = float(lines)
    scors.append(lin)
  except:
    scors.append(lines)
print(scors)
baxe = []
file = open("baxe.txt","r")
for lines in file:
    lines = lines.replace(" \n","")
    lin = (lines)
    baxe.append(lin)

goldenshield = []
file = open("goldenshield.txt","r")
for lines in file:
    lines = lines.replace(" \n","")
    lin = (lines)
    goldenshield.append(lin)

loc = []
file = open("location.txt","r")
for lines in file:
    lines = lines.replace(" \n","")
    lin = (lines)
    loc.append(lin)

bsword = []
file = open("bsword.txt","r")
for lines in file:
    lines = lines.replace(" \n","")
    lin = (lines)
    bsword.append(lin)

magmablade = []
file = open("magmablade.txt","r")
for lines in file:
    lines = lines.replace(" \n","")
    lin = (lines)
    magmablade.append(lin)


bshield = []
file = open("bshield.txt","r")
for lines in file:
    lines = lines.replace(" \n","")
    lin = (lines)
    bshield.append(lin)

seatrident = []
file = open("seatrident.txt","r")
for lines in file:
    lines = lines.replace(" \n","")
    lin = (lines)
    seatrident.append(lin)

nucshield = []
file = open("nucshield.txt","r")
for lines in file:
    lines = lines.replace(" \n","")
    lin = (lines)
    nucshield.append(lin)

octolord = []
file = open("octolord.txt","r")
for lines in file:
    lines = lines.replace(" \n","")
    lin = (lines)
    octolord.append(lin)

firewings = []
file = open("firewings.txt","r")
for lines in file:
    lines = lines.replace(" \n","")
    lin = (lines)
    firewings.append(lin)

bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=f"*help"))

@bot.command()
async def buy(ctx, arg1 = None):
  amon = None
  try:
    coinpo = scors[scors.index(f"{ctx.author}")+1]
  except:
    scors.append(f"{ctx.author}")
    scors.append(0)
    coinpo = scors[scors.index(f"{ctx.author}")+1]
  if arg1 == None:
    embed=discord.Embed(title="**WEAPONS MARKET**",  description='''
```Item             |Price   | Item code
Basic axe        |50⭐   |baxe
Basic sword      |50⭐   |bsword
Basic shield     |65⭐   |bshield
Axe of firewings |80⭐   |firewings
Blade of octolord|105⭐  |octolord
Sea trident      |155⭐  |seatrident
Nuclear shield   |200⭐  |nucshield
```
    
    ''', color=0xFF5733)
    await ctx.reply(embed=embed)
  
  else:
    if arg1 == "baxe":
      if coinpo >= 50:
        embed = discord.Embed(title = "`BASIC AXE`", description = "**You have now obtained the basic axe, being the first of its kind, it was made by one of the first humans themselves!**")
        embed. set_image(url="https://media.discordapp.net/attachments/957641660500684820/1004744276179169373/baxe-removebg-preview_2.png")
        await ctx.reply(embed = embed)
        baxe.append(f"{ctx.author}")
        amon = 50
      else:
        await ctx.reply("`Not enough points!`")
    elif arg1 == "bsword":
      if coinpo >= 50:
        embed = discord.Embed(title = "`BASIC SWORD`", description = "**You have now obtained the basic sword, being the first of its kind, it was made by one of the first humans themselves!**")
        embed. set_image(url="https://media.discordapp.net/attachments/957641660500684820/1004744685866201108/bsword-removebg-preview_4.png")
        await ctx.reply(embed = embed)
        bsword.append(f"{ctx.author}")
        amon = 50
      else:
        await ctx.reply("`Not enough points!`")

    elif arg1 == "bshield":
      if coinpo >= 65:
        embed = discord.Embed(title = "`BASIC SHIELD`", description = "**You have now obtained the basic shield, being the first of its kind, it was made by one of the first humans themselves!**")
        embed. set_image(url="http://pixelartmaker-data-78746291193.nyc3.digitaloceanspaces.com/image/cc9ed077aed46f5.png")
        await ctx.reply(embed = embed)
        bshield.append(f"{ctx.author}")
        amon = 65
      else:
        await ctx.reply("`Not enough points!`")

    elif arg1 == "firewings":
      if coinpo >= 80:
        embed = discord.Embed(title = "`AXE OF FIRE WINGS`", description = "**You have now obtained the legendary axe of wire wings, made with metal from the core of the earth, smelted in a volcano and crafted in the workshop of The Hawk himself!**")
        embed. set_image(url="https://media.discordapp.net/attachments/957641660500684820/1004744543532486666/bsword-removebg-preview_2.png")
        await ctx.reply(embed = embed)
        firewings.append(f"{ctx.author}")
        amon = 80
      else:
        await ctx.reply("`Not enough points!`")

    elif arg1 == "octolord":
      if coinpo >= 105:
        embed = discord.Embed(title = "`BLADE OF OCTOLORD`", description = "**You have now obtained the blade of octolord, after saving the gods for the 1000th time, the gods awarded kraken with a sword, sharper than the tip of a needle, stronger than a diamond, THE BLADE OF THE OCTOLORD!**")
        embed. set_image(url="https://media.discordapp.net/attachments/957641660500684820/1004807920782946354/bsword-removebg-preview__4_-removebg-preview.png")
        await ctx.reply(embed = embed)
        octolord.append(f"{ctx.author}")
        amon = 105
      else:
        await ctx.reply("`Not enough points!`")
    elif arg1 == "nucshield":
      if coinpo >= 155:
        embed = discord.Embed(title = "`NUCLEAR SHIELD`", description = "**You have obtained the nuclear shield! Forged in the hidden depths of hell, this shield was made using celestial gold, it has a powerful charm that makes it strong enough to block off a nuclear blast!**")
        embed. set_image(url="https://media.discordapp.net/attachments/957641660500684820/1004908309414948884/golshield-removebg-preview.png")
        await ctx.reply(embed = embed)
        nucshield.append(f"{ctx.author}")
        amon = 155
      else:
        await ctx.reply("`Not enough points!`")

    elif arg1 == "seatrident":
      if coinpo >=20-0:
        embed = discord.Embed(title = "`SEA TRIDENT`", description = "**You have now obtained the sea trident, during the war between the surface beings and marines, the mighty kraken had this weapon crafted by the hawk, this legandary weapon holds the power of controlling the sea and bringing mass destruction!**")
        embed. set_image(url="https://media.discordapp.net/attachments/957641660500684820/1004906464311267349/trident-removebg-preview.png")
        await ctx.reply(embed = embed)
        seatrident.append(f"{ctx.author}")
        amon = 200
      else:
        await ctx.reply("`Not enough points!`")
    else:
      await ctx.reply(f"`Invalid item. Use format : `")
      await ctx.reply("`buy {item code}`")
  if amon != None:
    scors[scors.index(f"{ctx.author}")+1] = coinpo - amon
  
  file = open("database.txt","w+")
  for i in scors:
    file.write(f"{i} \n")
  file.close()
  file = open("baxe.txt","w+")
  for i in baxe:
    file.write(f"{i} \n")
  file.close()
  file = open("bsword.txt","w+")
  for i in bsword:
    file.write(f"{i} \n")
  file.close()
  file = open("bshield.txt","w+")
  for i in bshield:
    file.write(f"{i} \n")
  file.close()
  file = open("nucshield.txt","w+")
  for i in nucshield:
    file.write(f"{i} \n")
  file.close()
  file = open("seatrident.txt","w+")
  for i in seatrident:
    file.write(f"{i} \n")
  file.close()
  file = open("firewings.txt","w+")
  for i in firewings:
    file.write(f"{i} \n")
  file.close()
  file = open("octolord.txt","w+")
  for i in octolord:
    file.write(f"{i} \n")
  file.close()

  

@bot.command()
async def stats(ctx):
  try:
    coinpo = scors[scors.index(f"{ctx.author}")+1]
  except:
    scors.append(f"{ctx.author}")
    scors.append(0)
    coinpo = scors[scors.index(f"{ctx.author}")+1]
  weapon = None
  shield = None
  x = 1
  if x == 1:
      if f"{ctx.author}" in baxe:
        weapon = "Basic axe"
      if f"{ctx.author}" in bsword:
        weapon = "Basic sword"
      if f"{ctx.author}" in octolord:
        weapon = "Blade of octolord"
      if f"{ctx.author}" in firewings:
        weapon = "Axe of firewings"
      if f"{ctx.author}" in seatrident:
        weapon = "Sea trident"
      if f"{ctx.author}" in bshield:
        shield = "Basic shield"
      if f"{ctx.author}" in nucshield:
        shield = "Nuclear shield"
      if f"{ctx.author}" in magmablade:
        weapon = "Magma blade"
      if f"{ctx.author}" in goldenshield:
        shield = "Golden shield"

  embed = discord.Embed(title = f"**{ctx.author}**",description = f'''
```
Points : {coinpo}
Weapon : {weapon}
Shield : {shield}
```''')
  await ctx.reply(embed = embed)
    
  file = open("database.txt","w+")
  for i in scors:
    file.write(f"{i} \n")
  file.close()

@bot.command()
async def help(ctx):
  embed =discord.Embed(title = "**Haken Bot Help**", description = '''
```
prefix : *
------------------------------------------------------------
stats                  : Check your current status, weapon, shield and points!
------------------------------------------------------------
hack                   : A simple memory game to earn points!
------------------------------------------------------------
guess                  : Guess a random number in 3 tries to earn points!
------------------------------------------------------------
spin                   : Do a lucky wheel spin to earn a random ammount of points!
------------------------------------------------------------
wordle                 : A vocabulary literature game which requires you to guess a 5 letter word in 6 guesses to earn points!
------------------------------------------------------------
rps                    : Play a game of rock paper scissor with the bot to earn points!
------------------------------------------------------------
meme                   : Get a random funny meme!
------------------------------------------------------------
infobook {page number} : Read the info book about different monsters you shall face while travling!
------------------------------------------------------------
travel                 : Travel around different towns , cities and islands to face different monsters, champions, warriors and beasts to unlock new weapons that cannot be bought in the shop!
------------------------------------------------------------
buy {item}             : Buy weapons and shields which will be needed during traveling! Run the command with an empty space in the item value area to view the item shop!
------------------------------------------------------------
pvp {user}             : 1 v 1 another user to test out your weapons and shields. The user with the stronger weapon and shield has the higher chance of winning!
------------------------------------------------------------
roast {user}           : Roast a person you dislike with a prefect ai generated insult!
------------------------------------------------------------
```
  ''',color=0xFF5733)
  await ctx.reply(embed = embed)

@bot.command()
async def roast(ctx, user : discord.Member):
    roasts = ["your birth-certificate says you were born on a highway, dam gotta be the biggest accident in history","how many doctors fainted after seeing an xray of your head? I would have definately fainted after seeing an empty head.","omg its an honor, never thought id meet the first human-donkey breed","hmm.. your brain has an abnormal ammount of cracks in it, no wonder..","how many parents disowned you the day right after they adopted you?","man your an original aren't you? never seen such an idiot like yourself","i was scrolling through google for hours to find a good joke to make myself laugh when all i had to do was look at you.","dude, i always wondered why humans hunted animals, after i saw you, i figured out why","the only intelligent thought that ever existed in your head died of loneliness","are you sure you were born on this planet?","the only thing you attract towards yourself is dogs, poop, stupidity and fart","how many dogs have ran away after seeing your face?","did you loose some nerves that connect your brain? cuz it seriously stopped growing","mistakes are better than accidents cuz atleast they can be fixed","when you die, its not because the doctor didn't treat you properly, its because he didn't want to treat you.","your as useless as the ueue in queue","mirrors cant talk, lucky for you, they cant laugh either","if laughter were the best medicine, noone would ever die as long as they look at you","i bet when you talk, your ass gets jealous of your mouth which gets to spit out all the shit","the only thing i would change when i see your face is the direction i was walking in","if my earning were based on each word you said that was smart, id be broke today","You are what happens when women drink during pregnancy.","You are the sun in my life… my eyes burn whenever i look at you","There is someone out there for everyone. For you, it’s a therapist.","I would smack you, but I’m against animal abuse","I would call you an idiot, but it would be an insult for stupid people.","You were so happy for the negativity of your Covid test, we didn’t want to spoil the happiness by telling you it was IQ test","You are like a software update. every time I see you, I immediately think 'not now'","You can’t imagine how much happiness you can bring… by leaving the room","Somewhere tree is producing oxygen for you. I’m sorry for it","Earth is full. Go home","I am jealous of people who didn’t meet you","I’d tell you to blow your brains out, but I’m pretty certain there’s nothing there"]
    await ctx.send(f"**Hey {user}, {random.choice(roasts)}**")

@bot.command()  
async def hack(ctx):
  try:
    coinpo = scors[scors.index(f"{ctx.author}")+1]
  except:
    scors.append(f"{ctx.author}")
    scors.append(0)
    coinpo = scors[scors.index(f"{ctx.author}")+1]
  
  def check(m): 
        return m.channel == ctx.channel and m.author == ctx.author   
  li = ["initialize sequence","access firewall","break network protection","gain access"]
  ord = []
  for i in range(len(li)):
    r = random.choice(li)
    li.remove(r)
    ord.append(r)
  
  r = await ctx.reply(f'''
`Memorize the following steps!`
`{ord[0]}`
`{ord[1]}`
`{ord[2]}`
`{ord[3]}`
''')
  print(ord)
  await asyncio.sleep(7)
  await r.delete()
  await ctx.reply("`Enter the sequence!`")
  try:
    msg = await bot.wait_for('message', check=check, timeout=9)
    msg = msg.content.lower()
    if msg == ord[0]:
      try:
        msg = await bot.wait_for("message",check = check, timeout = 9)  
        msg = msg.content.lower()
        if msg == ord[1]:
          try:
            msg = await bot.wait_for("message",check = check, timeout = 9)  
            msg = msg.content.lower()
            if msg == ord[2]:
              try:
                msg = await bot.wait_for("message",check = check, timeout = 9)  
                msg = msg.content.lower()
                if msg == ord[3]:
                  await ctx.reply("`Sequence method successful!`")
                  reward = 20
                  await ctx.reply("**Earned 20⭐!**")
                  scors[scors.index(f"{ctx.author}")+1] = coinpo + reward
                else:
                      await ctx.reply("`Incorrect!`")

              except:
                await ctx.reply("`You took too much time to answer!`")
            else:
                      await ctx.reply("`Incorrect!`")

          except:
            await ctx.reply("`You took too much time to answer!`")
        else:
                      await ctx.reply("`Incorrect!`")
      except:
        await ctx.reply("`You took too much time to answer!`")
    else:
                      await ctx.reply("`Incorrect!`")
  except:
    await ctx.reply("`You took too much time to answer!`")
  file = open("database.txt","w+")
  for i in scors:
    file.write(f"{i} \n")
  file.close()

@commands.cooldown(1, 6, commands.BucketType.user)
@bot.command()
async def spin(ctx):
  try:
    coinpo = scors[scors.index(f"{ctx.author}")+1]
  except:
    scors.append(f"{ctx.author}")
    scors.append(0)
    coinpo = scors[scors.index(f"{ctx.author}")+1]

  po = random.choice([0,0,0,0,0,0,0,10,10,10,10,15,15,15, 20,20])
  r = await ctx.reply("`Spinning luck wheel!`")
  m = await ctx.reply("https://media.discordapp.net/attachments/957641660500684820/1004159622774542426/ezgif.com-gif-maker.gif")
  await asyncio.sleep(3)
  l = None
  await m.delete()
  await r.delete()
  if po == 0:
    l = "Sorry,"
  else:
    l = "Congrats!"
  await ctx.reply(f"`{l}You earned {po}⭐`")
  scors[scors.index(f"{ctx.author}")+1] = coinpo + po
@spin.error
async def command_name_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("`please wait before spinning again`")

@bot.command()
async def guess(ctx):
      try:
        coinpo = scors[scors.index(f"{ctx.author}")+1]
      except:
        scors.append(f"{ctx.author}")
        scors.append(0)
        coinpo = scors[scors.index(f"{ctx.author}")+1]
      await ctx.reply("`A random number between 1-10 will be generated, you have 3 guessed and if u guess it right, you get 10 points!`")
      x = random.randint(1,10)

      for i in range(3):     
        def check(msg): 
          return msg.author == ctx.author and msg.channel == ctx.channel
        msg = await bot.wait_for("message", check = check, timeout = 30)
        msg12 = msg.content.lower()
        try:
          msg12 = int(msg12)
        except:
          await ctx.reply("Please enter a valid integer")
          await ctx.reply(l)
        if msg12 == 1 or msg12 == 2 or msg12 == 3 or msg12 == 4 or msg12 == 5 or msg12 == 6 or msg12 == 7 or msg12 == 8 or msg12 == 9 or msg12 == 10:
          if msg12 == x:
            await ctx.reply("Your guess is CORRECT")     
            reward = 20
            await ctx.reply("**Earned 20⭐!**")
            scors[scors.index(f"{ctx.author}")+1] = coinpo + reward
            print(bruh)
          elif msg12 != x:
           if x <= msg12:
             await ctx.reply(f"Wrong guess! The random number is smaller than {msg12}")   
           elif x >= msg12:
             await ctx.reply(f"Wrong guess! The random number is greater than {msg12}")  
        else:
          await ctx.reply("Please enter a valid number between 1 and 10")
          
      
      await ctx.reply(f"You've run out of guesses! The number was {x}!")
      file = open("database.txt","w+")
      for i in scors:
        file.write(f"{i} \n")
      file.close()

  
@bot.command()
async def wordle(ctx):
  try:
    coinpo = scors[scors.index(f"{ctx.author}")+1]
  except:
    scors.append(f"{ctx.author}")
    scors.append(0)
    coinpo = scors[scors.index(f"{ctx.author}")+1]
  word = random.choice(['Anime','Abuse', 'Adult', 'Agent', 'Anger',  'Beach', 'Birth', 'Block',  'Board', 'Brain', 'Bread', 'Break', 'Brown', 'Buyer', 'Cause', 'Chain', 'Chair', 'Chest', 'Chief', 'Child', 'China', 'Claim',  'Coast', 'Court', 'Cover', 'Cream', 'Crime', 'Cross', 'Crowd', 'Crown', 'Cycle', 'Dance', 'Death', 'Depth', 'Doubt', 'Draft', 'Drama', 'Dream', 'Dress', 'Drink', 'Drive', 'Earth', 'Enemy', 'Entry', 'Error', 'Event', 'Faith', 'Fault', 'Field', 'Fight', 'Final', 'Floor', 'Focus', 'Force', 'Frame', 'Frank', 'Front', 'Fruit', 'Glass', 'Grant', 'Grass', 'Green', 'Group', 'Guide', 'Heart', 'Henry', 'Horse', 'Hotel', 'House', 'Image', 'Index', 'Input', 'Issue', 'Japan', 'Jones', 'Judge', 'Knife', 'Laura', 'Layer', 'Level', 'Lewis', 'Light', 'Limit', 'Lunch', 'Major', 'March', 'Match', 'Metal', 'Model', 'Money', 'Month', 'Mouth', 'Music', 'Night', 'Noise', 'North', 'Novel', 'Nurse', 'Offer', 'Order', 'Other', 'Owner', 'Panel', 'Paper', 'Party', 'Peace', 'Phase', 'Phone', 'Piece', 'Pilot', 'Pitch', 'Place', 'Plane', 'Plant', 'Plate', 'Point', 'Pound', 'Power', 'Press', 'Price', 'Pride', 'Prize', 'Proof', 'Queen', 'Radio', 'Range', 'Ratio', 'Reply', 'Right', 'River', 'Round', 'Route', 'Rugby', 'Scale', 'Scene', 'Scope', 'Score', 'Sense', 'Shape', 'Share', 'Sheep', 'Sheet', 'Shift', 'Shirt', 'Shock', 'Sight', 'Simon', 'Skill', 'Sleep', 'Smile', 'Smith', 'Smoke', 'Sound', 'South', 'Space', 'Speed', 'Spite', 'Sport', 'Squad', 'Staff', 'Stage', 'Start', 'State', 'Steam', 'Steel', 'Stock', 'Stone', 'Store', 'Study', 'Stuff', 'Style', 'Sugar', 'Table', 'Taste', 'Terry', 'Theme', 'Thing', 'Title', 'Total', 'Touch', 'Tower', 'Track', 'Trade', 'Train', 'Trend', 'Trial', 'Trust', 'Truth', 'Uncle', 'Union', 'Unity', 'Value', 'Video', 'Visit', 'Voice', 'Waste', 'Watch', 'Water', 'While', 'White', 'Whole', 'Woman', 'World', 'Youth'])
  x = list(word.lower())
  
  await ctx.reply(f'''```
How to play:
-You have 6 tries to guess a 5 letter word!
-If a letter in the word you entered is part of the correct word, it will be shown using a yellow block
-If a letter in the word you entered is part of the correct word and is in the right position, it will be shown using a green block
-Start in 6 seconds!```
''')
  await asyncio.sleep(6)
  await ctx.reply("**Start!**")
  def check(msg): 
   return msg.author == ctx.author and msg.channel == ctx.channel
  try:
   msg = await bot.wait_for("message", check = check, timeout = 30)
   msg12 = list(msg.content.lower())
   await msg.delete()
   ya = msg12
   if len(msg12) == 5:
      memes = ["⬜", "⬜", "⬜", "⬜", "⬜"]
      for i in msg12:
        if i in x: 
            pos = x.index(i)
            mems = msg12.index(i)
            if pos == mems:
              memes[pos] = "🟩"
              
            elif pos != mems:
              memes[mems] = "🟨"
      if x != ya:
        await ctx.reply(f"{memes[0]} {memes[1]} {memes[2]} {memes[3]} {memes[4]} **: {msg.content}**")
      elif x == ya:
        await ctx.reply(f"🟩 🟩 🟩 🟩 🟩 **: {msg.content}**")
        await ctx.reply("`ALL CORRECT!`")        
        reward = 20
        await ctx.reply("**Earned 20⭐!**")
        scors[scors.index(f"{ctx.author}")+1] = coinpo + reward

        await ctx.reply(NUTS)

   else:
      await ctx.reply("`Your word cannot be a made-up one and can only have 5 letters. Please type the command again and restart.`")
      await ctx.reply(k)
  except asyncio.TimeoutError:
    await ctx.reply("`You took too much time to answer`")
    await ctx.reply(mem)
  try:
   msg = await bot.wait_for("message", check = check, timeout = 30)
   msg12 = list(msg.content.lower())
   await msg.delete()
   ya = msg12
   if len(msg12) == 5:
      memes = ["⬜", "⬜", "⬜", "⬜", "⬜"]
      for i in msg12:
        if i in x: 
            pos = x.index(i)
            mems = msg12.index(i)
            if pos == mems:
              memes[pos] = "🟩"
              
            elif pos != mems:
              memes[mems] = "🟨"
      if x != ya:
        await ctx.reply(f"{memes[0]} {memes[1]} {memes[2]} {memes[3]} {memes[4]} **: {msg.content}**")
      elif x == ya:
        await ctx.reply(f"🟩 🟩 🟩 🟩 🟩 **: {msg.content}**")
        await ctx.reply("`ALL CORRECT`")
        reward = 20
        await ctx.reply("**Earned 20⭐!**")
        scors[scors.index(f"{ctx.author}")+1] = coinpo + reward
        await ctx.reply(NUTS)
   else:
      await ctx.reply("`Your word cannot be a made-up one and can only have 5 letters. Please type the command again and restart.`")
      await ctx.reply(k)
  except asyncio.TimeoutError:
    await ctx.reply("`You took too much time to answer`")
    await ctx.reply(mem)
  try:
   msg = await bot.wait_for("message", check = check, timeout = 30)
   await msg.delete()
   msg12 = list(msg.content.lower())
   ya = msg12
   if len(msg12) == 5:
      memes = ["⬜", "⬜", "⬜", "⬜", "⬜"]
      for i in msg12:
        if i in x: 
            pos = x.index(i)
            mems = msg12.index(i)
            if pos == mems:
              memes[pos] = "🟩"
              
            elif pos != mems:
              memes[mems] = "🟨"
      if x != ya:
        await ctx.reply(f"{memes[0]} {memes[1]} {memes[2]} {memes[3]} {memes[4]} **: {msg.content}**")
      elif x == ya:
        await ctx.reply(f"🟩 🟩 🟩 🟩 🟩 **: {msg.content}**")
        await ctx.reply("`ALL CORRECT`")
        reward = 20
        await ctx.reply("**Earned 20⭐!**")
        scors[scors.index(f"{ctx.author}")+1] = coinpo + reward

        await ctx.reply(NUTS)
   else:
      await ctx.reply("`Your word cannot be a made-up one and can only have 5 letters. Please type the command again and restart.`")

      await ctx.reply(k)
  except asyncio.TimeoutError:
    await ctx.reply("`You took too much time to answer`")
    await ctx.reply(mem)
  try:
   msg = await bot.wait_for("message", check = check, timeout = 30)
   await msg.delete()
   msg12 = list(msg.content.lower())
   ya = msg12
   if len(msg12) == 5:
      memes = ["⬜", "⬜", "⬜", "⬜", "⬜"]
      for i in msg12:
        if i in x: 
            pos = x.index(i)
            mems = msg12.index(i)
            if pos == mems:
              memes[pos] = "🟩"
              
            elif pos != mems:
              memes[mems] = "🟨"
      if x != ya:
        await ctx.reply(f"{memes[0]} {memes[1]} {memes[2]} {memes[3]} {memes[4]} **: {msg.content}**")
      elif x == ya:
        await ctx.reply(f"🟩 🟩 🟩 🟩 🟩 **: {msg.content}**")
        await ctx.reply("`ALL CORRECT`")
        reward = 20
        await ctx.reply("**Earned 20⭐!**")
        scors[scors.index(f"{ctx.author}")+1] = coinpo + reward

        await ctx.reply(NUTS)
   else:
      await ctx.reply("`Your word cannot be a made-up one and can only have 5 letters. Please type the command again and restart.`")
      await ctx.reply(k)
  except asyncio.TimeoutError:
    await ctx.reply("`You took too much time to answer`")
    await ctx.reply(mem)
  try:
   msg = await bot.wait_for("message", check = check, timeout = 30)
   msg12 = list(msg.content.lower())
   await msg.delete()
   ya = msg12
   if len(msg12) == 5:
      memes = ["⬜", "⬜", "⬜", "⬜", "⬜"]
      for i in msg12:
        if i in x: 
            pos = x.index(i)
            mems = msg12.index(i)
            if pos == mems:
              memes[pos] = "🟩"
              
            elif pos != mems:
              memes[mems] = "🟨"
      if x != ya:
        await ctx.reply(f"{memes[0]} {memes[1]} {memes[2]} {memes[3]} {memes[4]} **: {msg.content}**")
      elif x == ya:
        await ctx.reply(f"🟩 🟩 🟩 🟩 🟩 **: {msg.content}**")
        await ctx.reply("`ALL CORRECT`")
        reward = 20
        await ctx.reply("**Earned 20⭐!**")
        scors[scors.index(f"{ctx.author}")+1] = coinpo + reward

        await ctx.reply(NUTS)
   else:
      await ctx.reply("`Your word cannot be a made-up one and can only have 5 letters. Please type the command again and restart.`")
      await ctx.reply(k)
  except asyncio.TimeoutError:
    await ctx.reply(" `You took too much time to answer`")
    await ctx.reply(mem)
  try:
   msg = await bot.wait_for("message", check = check, timeout = 30)
   msg12 = list(msg.content.lower())
   await msg.delete()
   ya = msg12
   if len(msg12) == 5:
      memes = ["⬜", "⬜", "⬜", "⬜", "⬜"]
      for i in msg12:
        if i in x: 
            pos = x.index(i)
            mems = msg12.index(i)
            if pos == mems:
              memes[pos] = "🟩"
              
            elif pos != mems:
              memes[mems] = "🟨"
      if x != ya:
        await ctx.reply(f"{memes[0]} {memes[1]} {memes[2]} {memes[3]} {memes[4]} **: {msg.content}**")
        await ctx.reply(F"`YOU RAN OUT OF GUESSES! THE WORD WAS {word}! GOOD TRY!`")
      elif x == ya:
        await ctx.reply(f"🟩 🟩 🟩 🟩 🟩 **: {msg.content}**")
        await ctx.reply("`ALL CORRECT`")
        reward = 20
        await ctx.reply("**Earned 20⭐!**")
        scors[scors.index(f"{ctx.author}")+1] = coinpo + reward

        await ctx.reply(NUTS)

   else:
      await ctx.reply("`Your word cannot be a made-up one and can only have 5 letters. Please type the command again and restart.`")
      await ctx.reply(k)
  except asyncio.TimeoutError:
    await ctx.reply("`You took too much time to answer. Please restart`")
    await ctx.reply(mem)
  file = open("database.txt","w+")
  for i in scors:
    file.write(f"{i} \n")
  file.close()

@bot.command()
async def meme(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.reply(embed=embed)

@bot.command()
async def rps(ctx):
  try:
    coinpo = scors[scors.index(f"{ctx.author}")+1]
  except:
    scors.append(f"{ctx.author}")
    scors.append(0)
    coinpo = scors[scors.index(f"{ctx.author}")+1]
  await ctx.reply('''
`Enter 1 for Rock`
`Enter 2 for Paper`
`Enter 3 for Scissor`
  ''')
  #COME 
  try: #why you leavw da call
    def check(m):#
        return m.channel == ctx.channel and m.author == ctx.author
    msg = await bot.wait_for('message', check=check, timeout=10)
    m = msg.content.lower()
    choises = ["sissor","rock","paper"]
    bc = random.choice(choises)
    ch = None
    em = None
    if m == "1":
      ch = "rock"
      em = "🪨"
    elif m == "2":
      ch = "paper"
      em = "📃"
    elif m == "3":
      ch = "sissor"
      em = "✂️"
    else:
      await ctx.reply("`Sorry, I did not get that, please try again`")
      x = y
    if bc == 'sissor':
      em1 = "✂️"
    elif bc == "rock":
      em1 = "🪨"
    elif bc == "paper":
      em1 = "📃"
    await ctx.reply(f"`{em} - {em1}`")
    if ch != bc:
      if (ch == "sissor" and bc == "rock") or (ch == "paper" and bc == "sissor") or (ch == "rock" and bc == "paper"):
        await ctx.reply("`Sorry, you lost,  before you challenge me in this game again, remember no one has ever beaten me in rock, paper, scissors!`")
      elif (ch == "sissor" and bc == "paper") or (ch == "paper" and bc == "rock") or (ch == "rock" and bc == "sissor"):
        await ctx.reply("`Well looks like someone's got lucky! Well played` ")
        reward = 10
        await ctx.reply("**Earned 10⭐!**")
        scors[scors.index(f"{ctx.author}")+1] = coinpo + reward
    else:
      await ctx.reply("`well well, it looks like its a tie!`")
  except asyncio.TimeoutError:
     await ctx.reply("You took too much time to answer..")
  file = open("database.txt","w+")
  for i in scors:
    file.write(f"{i} \n")
  file.close()

@bot.command()
async def infobook(ctx,page = None):
  if page == None:
    await ctx.send("**Please use the following format : ** `infobook {page number}`")
    xr = rx
  elif page == "1" or page == "page1":
    embed = discord.Embed(title = "**𝒫𝒶𝑔𝑒 𝟣**", description = '''
  ```
𝙲𝚑𝚊𝚙𝚝𝚎𝚛 𝟷 : 𝙲𝚑𝚊𝚖𝚙𝚒𝚘𝚗𝚜

𝙸𝚜𝚕𝚊𝚗𝚍 𝙷𝚞𝚝𝚘𝚙𝚒𝚊:
  
𝙲𝚊𝚙𝚝𝚊𝚒𝚗 𝚆𝚊𝚛𝚝𝚒𝚗
𝙰𝚐𝚎 : 𝟼𝟾
𝙵𝚎𝚊𝚝𝚞𝚛𝚎𝚜 : 𝙲𝚞𝚛𝚜𝚎𝚍 𝚋𝚘𝚍𝚢
  
𝙳𝚒𝚊𝚗𝚊 𝙻𝚎𝚗𝚘𝚢𝚊
𝙰𝚐𝚎 : 𝟼𝟺𝟸
𝙵𝚎𝚊𝚝𝚞𝚛𝚎𝚜 : 𝙱𝚕𝚎𝚜𝚜𝚎𝚍 𝚠𝚒𝚝𝚑 𝚖𝚊𝚐𝚒𝚌

𝙷𝚎𝚗𝚛𝚢 𝙿𝚘𝚔𝚝𝚎𝚋𝚢
𝙰𝚐𝚎 : 𝟸𝟼
𝙵𝚎𝚊𝚝𝚞𝚛𝚎𝚜 : 𝚂𝚞𝚙𝚎𝚛 𝚕𝚊𝚛𝚐𝚎
  ```
    ''', color=0xFF5733)
  elif page == "2" or page == "page2":
    embed = discord.Embed(title = "**𝒫𝒶𝑔𝑒 2**", description = '''
  ```
𝚁𝚊𝚕𝚘𝚗 :

𝙺𝚎𝚗𝚝𝚎𝚛
𝙰𝚐𝚎 : 𝟸𝟹
𝙵𝚎𝚊𝚝𝚞𝚛𝚎 : 𝙷𝚞𝚗𝚝𝚎𝚛

𝙻𝚊𝚛𝚕𝚎𝚢
𝙰𝚐𝚎 : 𝟹𝟻
𝙵𝚎𝚊𝚝𝚞𝚛𝚎 : 𝙰𝚛𝚌𝚑𝚎𝚛

𝙲𝚊𝚛𝚕𝚘𝚜
𝙰𝚐𝚎 : 𝟷𝟿
𝙵𝚎𝚊𝚝𝚞𝚛𝚎 : 𝙶𝚘𝚕𝚍 𝚆𝚊𝚛𝚛𝚒𝚘𝚛
```
    ''', color=0xFF5733)
  elif page == "3" or page == "page3":
    embed = discord.Embed(title = "**𝒫𝒶𝑔𝑒 3**", description = '''
```
𝙲𝚘𝚊𝚜𝚝 𝚘𝚏 𝚝𝚑𝚎 𝚋𝚎𝚊𝚜𝚝

𝙲𝚊𝚙𝚝𝚊𝚒𝚗 𝚂𝚚𝚞𝚒𝚛𝚘𝚗
𝙰𝚐𝚎 : 𝟷𝟶𝟼
𝙵𝚎𝚊𝚝𝚞𝚛𝚎 : 𝚂𝚚𝚞𝚒𝚍

𝙳𝚘𝚌 𝙾𝚌
𝙰𝚐𝚎 : 𝟹𝟽
𝙵𝚎𝚊𝚝𝚞𝚛𝚎 : 𝙾𝚌𝚝𝚘𝚙𝚞𝚜
```    
    ''',color=0xFF5733)
  elif page == "4" or page == "page4":
    embed = discord.Embed(title = "**𝒫𝒶𝑔𝑒 3**", description = '''
```
𝙼𝚘𝚞𝚗𝚝 𝙸𝚔𝚎𝚗

𝙶𝚛𝚒𝚏𝚘𝚗
𝙰𝚐𝚎 : 𝟻𝟼
𝙵𝚎𝚊𝚝𝚞𝚛𝚎 : 𝚟𝚞𝚕𝚝𝚞𝚛𝚎

𝙷𝚊𝚛𝚙𝚢
𝙰𝚐𝚎 : 𝟹𝟷
𝙵𝚎𝚊𝚝𝚞𝚛𝚎 : 𝙴𝚊𝚐𝚕𝚎

𝙻𝚊𝚖𝚖𝚎𝚛𝚐𝚎𝚒𝚎𝚛
𝙰𝚐𝚎 : 𝟺𝟹
𝙵𝚎𝚊𝚝𝚞𝚛𝚎 : 𝚟𝚞𝚕𝚝𝚞𝚛𝚎
``` 
    ''', color = 0xFF5733)
  elif page == "5" or page == "page5":
    embed = discord.Embed(title = "**𝒫𝒶𝑔𝑒 5**", description = '''
```
𝚅𝚎𝚛𝚞𝚜
𝙰𝚐𝚎 : 𝟷𝟼
𝙵𝚎𝚊𝚝𝚞𝚛𝚎 : 𝙶𝚕𝚊𝚍𝚒𝚊𝚝𝚘𝚛

𝙰𝚋𝚍𝚎𝚕 𝙵𝚊𝚝𝚝𝚊𝚑
𝙰𝚐𝚎 : 𝟹𝟹
𝙵𝚎𝚊𝚝𝚞𝚛𝚎 : 𝙰𝚛𝚖𝚢 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚎𝚛

𝙽𝚊𝚜𝚜𝚎𝚛
𝙰𝚐𝚎 : 𝟹𝟻
𝙵𝚎𝚊𝚝𝚞𝚛𝚎 : 𝙻𝚒𝚎𝚞𝚝𝚎𝚗𝚊𝚗𝚝 𝚐𝚎𝚗𝚎𝚛𝚊𝚕
``` 
    ''', color = 0xFF5733)
  elif page == "6" or page == "page6":
    embed = discord.Embed(title = "**𝒫𝒶𝑔𝑒 6**", description = '''
```
𝙷𝚛𝚘𝚔𝚎𝚗

𝙰𝚛𝚜𝚎𝚗𝚊𝚕
𝙰𝚐𝚎 : 𝟷𝟶𝟶𝟻
𝙵𝚎𝚊𝚝𝚞𝚛𝚎 : 𝙻𝚊𝚟𝚊 𝚐𝚘𝚕𝚎𝚖

𝚁𝚊𝚐𝚎
𝙰𝚐𝚎 : 𝟿𝟺𝟹
𝙵𝚎𝚊𝚝𝚞𝚛𝚎 : 𝙼𝚊𝚐𝚖𝚊 𝚑𝚘𝚞𝚗𝚍

𝙻𝚘𝚛𝚍 𝚘𝚋𝚜𝚒𝚍𝚒𝚊𝚗
𝙰𝚐𝚎 : 𝟼𝟻𝟶𝟺𝟹𝟻𝟼𝟷
𝙵𝚎𝚊𝚝𝚞𝚛𝚎 : 𝚏𝚒𝚛𝚎 𝚋𝚎𝚊𝚜𝚝
``` 
    ''', color = 0xFF5733)
  else:
    await ctx.send("`Invalid page number, page number must bee within 1 - 6`")
    xr = trx
  await ctx.reply(embed = embed)

@commands.cooldown(1, 2, commands.BucketType.user)
@bot.command()
async def travel(ctx):
  if f"{ctx.author}" in baxe or f"{ctx.author}" in bsword or f"{ctx.author}" in magmablade or f"{ctx.author}" in firewings or f"{ctx.author}" in octolord or f"{ctx.author}" in seatrident:
    pass
  else:
    await ctx.send("`You must have a weapon while traveling!`")
    x= r = y = z 
  lavaking = False
  cur_loc = None
  try:
    coinpo = scors[scors.index(f"{ctx.author}")+1]
  except:
    scors.append(f"{ctx.author}")
    scors.append(0)
    coinpo = scors[scors.index(f"{ctx.author}")+1]
  won__ = False
  def check(reaction, user): 
        return user == ctx.message.author
  new_loc = ["Ralon, The city of gold!","Ralon, The city of gold!","Hutopia, the land of poor","Hutopia, the land of poor","Hutopia, the land of poor","Hutopia, the land of poor","Hutopia, the land of poor", "Coast of the beast, the home of the mighty kraken", "Coast of the beast, the home of the mighty kraken", "Coast of the beast, the home of the mighty kraken","Mount Iken, the home of the mighty hawk","Mount Iken, the home of the mighty hawk","Mount Iken, the home of the mighty hawk","Retenia, the land of warriors","Retenia, the land of warriors","Retenia, the land of warriors","Mount hroken, home to the fire beast","Retenia, the land of warriors","Mount hroken, home to the fire beast","Mount hroken, home to the fire beast","Hutopia, the land of poor","Hutopia, the land of poor","Hutopia, the land of poor","Hutopia, the land of poor","Hutopia, the land of poor","Hutopia, the land of poor"]
  if f"{ctx.author}" in loc:
    rt = random.randint(0,100)
    bcan = None
    if rt < 10:
      cur_loc = loc[loc.index(f"{ctx.author}")+1]
      for i in new_loc:
        if f"{i}" == f"{cur_loc}":
          new_loc.remove(cur_loc)
      locr = random.choice(new_loc)
      await ctx.reply(f"`You have arrived at {locr}!`")
      loc[loc.index(f"{ctx.author}")+1] = locr
    else:
      xtr  = random.randint(0,100)
      if xtr < 33:
        chances = 0
        weapon = None
        if f"{ctx.author}" in magmablade:
          weapon = magmablade
          chances = 8
          bcan = 4
        elif f"{ctx.author}" in seatrident:
          weapon = seatrident   
          chances = 6
          bcan = 5
        elif f"{ctx.author}" in firewings:
          weapon = firewings
          chances = 5
          bcan = 15
        elif f"{ctx.author}" in octolord:
          weapon = octolord
          chances = 5
          bcan = 15
        elif f"{ctx.author}" in bsword:
          weapon = bsword
          chances = 3
          bcan = 30
        elif f"{ctx.author}" in baxe:
          weapon = baxe
          chances = 3
          bcan = 30
        else:
          chances = 0
          bcan = 0
        if f"{ctx.author}" in goldenshield:
          chances = chances+3
        elif f"{ctx.author}" in nucshield:
          chances = chances + 2

        elif f"{ctx.author}" in bshield:
          chances = chances + 1
        cur_loc = loc[loc.index(f"{ctx.author}")+1]
        bchanse = None
        msger = None
        mr = None
        if "hutopia" in cur_loc.lower():
          bchance = 10 - chances 
          msger = random.choice(["You! You riches have ruined the state of my town, i, Defender of hutopia, challenge you to battle me!","Why have you come here? YOU ARE NOT WELCOME HERE! I SHALL DESTROY YOU!","FILTH! YOUR KIND HAVE ROBBED MY TOWN, I WILL BREAK EACH YOUR BONES!"])
          mr = random.choice(['strange old man',"giant",'witch'])
        elif "ralon" in cur_loc.lower():
          bchance = 11 - chances
          msger = random.choice(["Hey! Traveler! You are in the territory of the gold king now! Who is that? Oh it's me, Anyone who enters my territory must fight me!","Hey!Traveler! I have a challenge for you, fight me! Its been a while since i've had a good challenge!","Hey you! You look strong, wanna fight me?"])
          mr = random.choice(['Gold warrior','hunter','archer','assasin'])
        elif "coast" in cur_loc.lower():
          bchance = 13 - chances
          msger = random.choice(["Heh, look at you, daring to enter master kraken's territory? Wanna travel further, you gotta go through me!","O HO HO HO! What have we got here? A young traveler i see! Well mate, we've got a tradition here, all new comers must battle me to enter the city!",'Uh hey there! SO, you look like a fighter eh? Wanna 1 v 1?'])
          mr = random.choice(['squid',"octopus","catfish"])
        elif "iken" in cur_loc.lower():
          bchance = 13 - chances
          msger = random.choice(["Oh hey there! Dont worry, master hawk respects travelers. But, you know, i was hoping we could have a dual, totally your choice!","h-h-hey the-*cough* *cough*, hey there traveller! How you doing! Wanna dual? Its been a while since i've had a worthy opponent!"])
          mr = random.choice(['vulture','eagle','cassowary','lammergeier'])
        elif "retenia" in cur_loc.lower():
          bchance = 12 - chances
          msger = random.choice(["Oh ho ho! Looks like another warrior's entered retenia! Welcome, welcome! Wanna have a dual?","HEY! HEY YOU! GIVE ME ALL YOUR THINGS NOW!","OH look at that, you look like some who needs to be beaten up he?"])
          mr = random.choice(["gladiator","army commander","theif","street gangster"])
        elif "hroken" in cur_loc.lower():
          vel = random.randint(0,100)
          if vel < 20:
            lavaking = True
            bchance = 20 - chances
            msger = random.choice(['𝒜 𝒩𝒪𝒩 𝐹𝐼𝑅𝐸 𝐵𝐸𝐼𝒩𝒢? 𝒴𝒪𝒰 𝒟𝒜𝑅𝐸 𝐸𝒩𝒯𝐸𝑅 𝑀𝒴 𝒦𝐼𝒩𝒢𝒟𝒪𝑀! 𝐼 𝒲𝐼𝐿𝐿 𝐵𝒰𝑅𝒩 𝒴𝒪𝒰 𝒯𝐼𝐿 𝒴𝒪𝒰𝑅 𝐿𝒜𝒮𝒯 𝒜𝒮𝐻 𝒟𝐼𝒮𝒮𝒜𝒫𝐸𝒜𝑅𝒮!',"𝐻𝑀𝑀, 𝐼 𝒟𝒪𝒩𝒯 𝒯𝐻𝐼𝒩𝒦 𝐼'𝒱𝐸 𝐸𝒱𝐸𝑅 𝒮𝐸𝐸𝒩 𝒜 𝒩𝒪𝒩-𝐹𝐼𝑅𝐸 𝐵𝐸𝐼𝒩𝒢 𝐼𝒩 𝑀𝒴 𝒦𝐼𝒩𝒢𝒟𝒪𝑀 𝐵𝐸𝐹𝒪𝑅𝐸. 𝒴𝒪𝒰'𝑅𝐸 𝒰𝒢𝐿𝐼𝐸𝑅 𝒯𝐻𝒜𝒩 𝐼 𝒯𝐻𝒪𝒰𝒢𝐻𝒯. 𝒢𝐸𝒯 𝒪𝒰𝒯𝒜 𝐻𝐸𝑅𝐸 𝒴𝒪𝒰 𝐿𝐼𝒯𝒯𝐿𝐸 𝒫𝒰𝒩𝒦!","𝐻𝑀𝑀, 𝐻𝒜𝒱𝐸 𝒴𝒪𝒰 𝒞𝒪𝑀𝐸 𝐻𝐸𝑅𝐸 𝐹𝒪𝑅 𝒪𝒰𝑅 𝒮𝒫𝐸𝒞𝐼𝒜𝐿 𝒟𝐸𝒜𝒯𝐻? 𝒴𝒪𝒰 𝒞𝒜𝒩 𝐻𝒜𝒱𝐸 𝐼𝒯 𝐹𝒪𝑅 𝐹𝑅𝐸𝐸!"])
            mr = 'Fire beast'
          else:
            bchance = 15 - chances
            msger = random.choice(["You are now in the territory of hroken! No no-fire beings are permitted here, time for you to perish!","Aww look at that, a non fire dude thinking he can walk up here and we wont do anything? Ha!","Hey! You cant come in here without permission! Get ready to die!"])
            mr = random.choice(["magma hound","lava golem"])

        xr4 = await ctx.reply(f'''
```While roaming around, you are confronted by a {mr} who shouts-
"{msger}"
Do you wish to fight him?
(This command will de activate after a few seconds)
```
        ''')
        await xr4.add_reaction('✅')
        await xr4.add_reaction('❌')
        reaction = await bot.wait_for("reaction_add", check=check, timeout = 10)
        chence = []
        if f"{reaction[0]}" == "✅":
          await ctx.reply("`Fighting..`")
          await asyncio.sleep(3)
          for i in range(chances):
            chence.append("player")
          for i in range(bchance):
            chence.append('npc')
          winner = random.choice(chence)
          if winner == "player":
            await ctx.reply("`You have won!`")
            won__ = True
          else:
            await ctx.reply("`You have lost!`")
          if won__:
            reward = 10
            await ctx.reply("**Earned 10⭐!**")
            scors[scors.index(f"{ctx.author}")+1] = coinpo + reward        
            if lavaking:
              ttr = random.randint (0,100)
              if ttr<70:
                rtrt = await ctx.reply("`You found a magma blade after defeating the lava king!! Would you like to keep it?`")
                await rtrt.add_reaction("✅")            
                await rtrt.add_reaction("❌")
                reaction = await bot.wait_for("reaction_add", check=check, timeout = 10)
                if f"{reaction[0]}" == "✅":
                  embed = discord.Embed(title = "`MAGMA BLADE`", description = "**You have now obtained the magma blade, made out of pure molten lava from the core of an active volcano, this blade burns hotter than real magma, even a cut made by it can burn a body!**")
                  embed. set_image(url="https://media.discordapp.net/attachments/957641660500684820/1005214909874851981/lmao-removebg-preview.png")
                  await ctx.reply(embed = embed)
                  magmablade.append(f"{ctx.author}")
                else:
                  await ctx.send("`You drop the magma blade`")

          else:
              if lavaking:
                if weapon == baxe:
                  baxe.remove(f"{ctx.author}")
                elif weapon == bsword:
                  bsword.remove(f"{ctx.author}")
                elif weapon == octolord:
                  octolord.remove(f"{ctx.author}")
                elif weapon == firewings:
                  firewings.remove(f"{ctx.author}")
                elif weapon == seatrident:
                  seatrident.remove(f"{ctx.author}")
                elif weapon == magmablade:
                  magmablade.remove(f"{ctx.author}")
                if f"{ctx.author}" in goldenshield:
                  goldenshield.remove(f"{ctx.author}")
                elif f"{ctx.author}" in nucshield:
                  nucshield.remove(f"{ctx.author}")
                elif f"{ctx.author}" in bshield:
                  bshield.remove(f"{ctx.author}")
                await ctx.send("`The weapons you were using during the fight were lost and burnt`")
          dxtr = random.randint(0,100)
          if dxtr < bcan and not lavaking:
            await ctx.reply("`You lost your weapon during the fight!`")
            if weapon == baxe:
              baxe.remove(f"{ctx.author}")
            elif weapon == bsword:
              bsword.remove(f"{ctx.author}")
            elif weapon == octolord:
              octolord.remove(f"{ctx.author}")
            elif weapon == firewings:
              firewings.remove(f"{ctx.author}")
            elif weapon == seatrident:
              seatrident.remove(f"{ctx.author}")
            elif weapon == magmablade:
              magmablade.remove(f"{ctx.author}")

        elif f"{reaction[0]}" == "❌":
          await ctx.reply("`You run away!`")
        else:
          await ctx.reply("`invalid reaction`")
      else:
        rt = random.randint(0,100)
        if rt < 10:
          cur_loc = loc[loc.index(f"{ctx.author}")+1]
          rtrrtt = random.randint(0,100)
          if "ralon" in cur_loc.lower() and rtrrtt < 50:
            rtrt = await ctx.reply("`You found a golden shield while roaming around! Would you like to keep it?`")
            await rtrt.add_reaction("✅")            
            await rtrt.add_reaction("❌")
            reaction = await bot.wait_for("reaction_add", check=check, timeout = 10)
            if f"{reaction[0]}" == "✅":
              embed = discord.Embed(title = "`GOLDEN SHIELD`", description = "**You have obtained the golden shield! Originally made for one of the strongest warriors for his champions battle, this shield was made using the gold of the gods, easily dentable but it repairs itself faster than the speed of light!**")
              embed. set_image(url="https://media.discordapp.net/attachments/957641660500684820/1005262001150374019/goldshield-removebg-preview.png?width=399&height=572")
              await ctx.reply(embed = embed)
              goldenshield.append(f"{ctx.author}")
            elif f"{reaction[0]}" == '❌':
              await ctx.reply("`You drop the golden shield`")
          elif "coast" in cur_loc.lower() and rtrrtt < 70:
            rtrt = await ctx.reply("`You found the blade of octolord while roaming around! Would you like to keep it?`")
            await rtrt.add_reaction("✅")            
            await rtrt.add_reaction("❌")
            reaction = await bot.wait_for("reaction_add", check=check, timeout = 10)
            if f"{reaction[0]}" == "✅":
              embed = discord.Embed(title = "`BLADE OF OCTOLORD`", description = "**You have now obtained the blade of octolord, after saving the gods for the 1000th time, the gods awarded kraken with a sword, sharper than the tip of a needle, stronger than a diamond, THE BLADE OF THE OCTOLORD!**")
              embed. set_image(url="https://media.discordapp.net/attachments/957641660500684820/1004807920782946354/bsword-removebg-preview__4_-removebg-preview.png")
              await ctx.reply(embed = embed)
              octolord.append(f"{ctx.author}")
          elif "iken" in cur_loc.lower() and rtrrtt < 70:
            rtrt = await ctx.reply("`You found the axe of firewings while roaming around! Would you like to keep it?`")
            await rtrt.add_reaction("✅")            
            await rtrt.add_reaction("❌")
            reaction = await bot.wait_for("reaction_add", check=check, timeout = 10)
            if f"{reaction[0]}" == "✅":
              embed = discord.Embed(title = "`AXE OF FIRE WINGS`", description = "**You have now obtained the legendary axe of wire wings, made with metal from the core of the earth, smelted in a volcano and crafted in the workshop of The Hawk himself!**")
              embed. set_image(url="https://media.discordapp.net/attachments/957641660500684820/1004744543532486666/bsword-removebg-preview_2.png")
              await ctx.reply(embed = embed)
              firewings.append(f"{ctx.author}")
            elif f"{reaction[0]}" == '❌':
              await ctx.reply("`You drop the blade of octolord`")
          elif "hroken" in cur_loc.lower():
            xtrrrr = random.randint(0,100)
            if xtrrrr < 30:
              rtrt = await ctx.reply("`You found the magma blade while roaming around! Would you like to keep it?`")
              await rtrt.add_reaction("✅")            
              await rtrt.add_reaction("❌")
              reaction = await bot.wait_for("reaction_add", check=check, timeout = 10)
              if f"{reaction[0]}" == "✅":
                embed = discord.Embed(title = "`MAGMA BLADE`", description = "**You have now obtained the magma blade, made out of pure molten lava from the core of an active volcano, this blade burns hotter than real magma, even a cut made by it can burn a body!**")
                embed. set_image(url="https://media.discordapp.net/attachments/957641660500684820/1005214909874851981/lmao-removebg-preview.png")
                await ctx.reply(embed = embed)
                magmablade.append(f"{ctx.author}")
 
        else:
          await ctx.reply("`You roam around..`")
  else:
    loc.append(f"{ctx.author}")
    locr = random.choice(new_loc)
    loc.append(f"{locr}")
    await ctx.reply(f"`You travel and arrive at {locr}`")
  file = open("location.txt","w+")
  for i in loc:
    file.write(f"{i} \n")
  file.close()
  file = open("baxe.txt","w+")
  for i in baxe:
    file.write(f"{i} \n")
  file.close()
  file = open("bsword.txt","w+")
  for i in bsword:
    file.write(f"{i} \n")
  file.close()
  file = open("bshield.txt","w+")
  for i in bshield:
    file.write(f"{i} \n")
  file.close()
  file = open("nucshield.txt","w+")
  for i in nucshield:
    file.write(f"{i} \n")
  file.close()
  file = open("magmablade.txt","w+")
  for i in magmablade:
    file.write(f"{i} \n")
  file.close()
  file = open("seatrident.txt","w+")
  for i in seatrident:
    file.write(f"{i} \n")
  file.close()
  file = open("firewings.txt","w+")
  for i in firewings:
    file.write(f"{i} \n")
  file.close()
  file = open("octolord.txt","w+")
  for i in octolord:
    file.write(f"{i} \n")
  file.close()
@travel.error
async def command_name_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("`You have exhausted your energy, please wait a few seconds!`")

@bot.command()
async def pvp(ctx, user : discord.Member):
    c = []
    try:
        coinpo = scors[scors.index(f"{ctx.author}")+1]
    except:
        scors.append(f"{ctx.author}")
        scors.append(0)
        coinpo = scors[scors.index(f"{ctx.author}")+1]
    try:
        coinpo2 = scors[scors.index(f"{user}")+1]
    except:
        scors.append(f"{user}")
        scors.append(0)
        coinpo2 = scors[scors.index(f"{user}")+1]
    
    fight = False
    if ctx.author != user:
      await ctx.send(f"<@!{user.id}>! `You have been challenged by {ctx.author} to a duel! Do you accept the challenge? Type 'yes' to accept and 'no' to decline`")
      def check(m): 
        return m.channel == ctx.channel and m.author == user
      try: 
          msg = await bot.wait_for('message', check=check, timeout=30)
          if f"{msg.content.lower()}" == "yes":
            fight = True
          elif f"{msg.content.lower()}" == "no":
            await ctx.send("You have declined the challenge")
            await ctx.send(stop)
          else:
            await ctx.send("Please send the invitation again and only reply with 'yes' or 'no'")
            await ctx.send(stop)
      except:
        await ctx.send(f"{user} took too much time to reply")
        await ctx.send(stop)
    else:
      await ctx.send("You cannot fight yourself!")
      await ctx.send(nthg)
    if fight:
        embed = discord.Embed(title = f"{user} VS {ctx.author}", description = "**FIGHT!!**")
        embed.set_image(url="https://thumbs.gfycat.com/LittleFilthyKodiakbear-size_restricted.gif")
      
        await ctx.send(embed = embed)
        await asyncio.sleep(2)
        if f"{ctx.author}" in magmablade:
          for i in range(5):
            c.append(1)
        elif f"{ctx.author}" in seatrident:
          for i in range(4):
            c.append(1)
        elif f"{ctx.author}" in firewings:
          for i in range(3):
            c.append(1)
        elif f"{ctx.author}" in octolord:
          for i in range(3):
            c.append(1)
        elif f"{ctx.author}" in bsword:
          for i in range(1):
            c.append(1)
        elif f"{ctx.author}" in baxe:
          for i in range(1):
            c.append(1)
        else:
          await ctx.send(f"`{ctx.author} must have a weapon to pvp!`")
          rx = tr
        if f"{ctx.author}" in goldenshield:
          for i in range(3):
            c.append(1)
        elif f"{ctx.author}" in nucshield:
          for i in range(2):
            c.append(1)

        elif f"{ctx.author}" in bshield:
          for i in range(1):
            c.append(1)
            
        if f"{user}" in magmablade:
          for i in range(5):
            c.append(2)
        elif f"{user}" in seatrident:
          for i in range(4):
            c.append(2)
        elif f"{user}" in firewings:
          for i in range(3):
            c.append(2)
        elif f"{user}" in octolord:
          for i in range(3):
            c.append(2)
        elif f"{user}" in bsword:
          for i in range(1):
            c.append(2)
        elif f"{user}" in baxe:
          for i in range(1):
            c.append(2)
        else:
          await ctx.send(f"`{user} must have a weapon to pvp!`")
          rx = tr
        if f"{user}" in goldenshield:
          for i in range(3):
            c.append(2)
        elif f"{user}" in nucshield:
          for i in range(2):
            c.append(2)

        elif f"{user}" in bshield:
          for i in range(1):
            c.append(2)
        await asyncio.sleep(4)
        y = 1
        if y == 1:
          ran = random.choice(c)
          if ran == 1:
            await ctx.send(f"**{ctx.author} HAS WON THE DUEL**")
            reward = 10
            await ctx.reply(f"**{ctx.author} earned 10⭐!**")
            scors[scors.index(f"{ctx.author}")+1] = coinpo + reward
          elif ran == 2:
            await ctx.send(f"**{user} HAS WON THE DUEL**")
            reward = 10
            await ctx.reply(f"**{user} earned 10⭐!**")
            scors[scors.index(f"{user}")+1] = coinpo2 + reward
immortal.keep_alive()
bot.run(token)