import discord
from discord.ext import commands

TOKEN = ''
items = []
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix ='!', intents=intents)
text_channel_list = []


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for guild in client.guilds:
        for channel in guild.text_channels:
            text_channel_list.append(channel)
    for channel in text_channel_list:
        if channel.name == 'bot':
            await channel.send('Bot is now online')


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    await client.process_commands(message)


@client.command()
async def add(ctx):
    await ctx.send("Please enter your item: ")
    msg = await client.wait_for('message')
    items.append(msg.content.strip())
    await ctx.send("Added to list: " + msg.content)

    with open('testing.csv', 'a') as f:
        f.write(msg.content + '\n')


@client.command()
async def price(ctx):
    cost = 0
    for item in items:
        print(items)
        filepath = r'C:\Users\adi2m\Documents\\' + item + '.csv'
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.readlines()
            result = []
        for i in range(len(content)):
            line = content[i].strip()
            if line.isdigit() or line == '5+' or line == '-':
                if line == '-':
                    result.append('0')
                else:
                    result.append(line)
            elif 'Item Code:' in line:
                result.append(content[i + 1].strip())

            elif '$' in line:
                if '$' in content[i + 1].strip():
                    cost += float(content[i + 1][1:])
                    result.append(content[i + 1].strip() + ' (' + content[i + 2].strip() + ")")
                else:
                    cost += float(content[i][1:])
                    result.append(line)
                break

        if not result:
            await ctx.send('Invalid Search')
        else:
            await ctx.send(result[1] + ' --- stock: ' + result[0] + ' --- price: ' + result[2])
    await ctx.send('Total Cost: $' + str(cost))


client.run(TOKEN)

