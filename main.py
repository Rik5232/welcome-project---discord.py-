import discord

from discord.ext import commands



client = commands.Bot(command_prefix=">") # ur prefix here!

@client.event
async def on_ready():
  print("bot is ready")
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')


  @client.command()
  async def hello(ctx):
    await ctx.send("Hi")

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    guild = client.get_guild(759707492170465283) # YOUR INTEGER GUILD ID HERE
    welcome_channel = guild.get_channel(759707492170465286) # YOUR INTEGER CHANNEL ID HERE
    embed = discord.Embed(title="Welcome to the server", colour=discord.Colour(0x2ecc71), url="https://discord.gg/devs", description=f'Welcome {member.mention} you just joined {guild.name}. Have a nice time over! <3')


    embed.set_image(url="https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif")
    embed.set_thumbnail(url=f'{guild.icon_url}')
    embed.set_author(name=f'{member.name}', icon_url=f'{member.avatar_url}')
    await welcome_channel.send(embed=embed)



client.run("ur token here")  
