import discord

with open('C:\\Users\\Yan\\Desktop\\Scripting\\discord_keys.txt','r') as f:
	secret_data = f.readlines()

client_id = secret_data[0]
secret_id = secret_data[1]
acess_token = secret_data[2]
role_int = secret_data[3]

client = discord.Client()

@client.event
async def on_ready():
	print('Logged as {client.user}')

@client.event
async def on_message(message):
	print('Incoming msg: {message.channel}: {message.author}: {message.content}')

client.run(acess_token)