import os, serial, time, discord, sys, bot_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
users = ["Geg#3469"]

def check_role(user, role):
    for r in user.roles:
        if r.id == role:
            return True
    return False

@client.event
async def on_ready():
    print(f'{client.user} is connected with Discord.py')
    
@client.event
async def on_message(message):
    if message.author == client.user and (message.author.name + message.author.discriminator) in users:
        return

    if "/help " in message.content.lower():
        await bot_commands.c_help(message)

    if "/move " in message.content.lower():
        await bot_commands.c_move(message)

    if "/turn " in message.content.lower():
        await bot_commands.c_rotate(message)
        
    # if "/log " in message.content.lower():
    #     await bot_commands.c_log(message)

    # if "/rotate " in message.content.lower() and len(message_array) > 2:
    #     await bot_commands.c_rotate(message)
        
client.run(TOKEN)