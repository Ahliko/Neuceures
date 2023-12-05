import discord
import token

with open('token.txt', 'r') as token:
    token = token.read()

# Create a new Discord client
intents = discord.Intents.default()  # Create a default set of intents
intents.typing = False  # Disable typing events for simplicity, adjust as needed

client = discord.Client(intents=intents)

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'Bot online : {client.user}')

# Event handler for when a message is received
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'neuceures':
        await message.channel.send('va niquer ta race')

client.run(token)
