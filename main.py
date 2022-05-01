import discord
from discord.ext import commands

TOKEN = 'OTcwMTQwMzUzNzE1OTE2ODQw.Ym3nnA.qf80KxyvCE3x9BbJDlLiTXX-wM4'
items = []  # global list to store the user's searches
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
    """ Command to search and add computer parts to the users cart.

    > !add
    Please enter your item:
    > RTX 2080
    Added to list: RTX 2080
    """
    await ctx.send("Please enter your item: ")  # prompt user to input the item
    msg = await client.wait_for('message')  # collect user input
    items.append(msg.content.strip())  # adding part to our global list
    await ctx.send("Added to list: " + msg.content)  # confirm item to user

    # we process user input by writing to a csv file and forwarding the file
    # with the inputs to our UIpath program to scrape websites and find
    # available input items.
    with open('testing.csv', 'a') as f:
        f.write(msg.content + '\n')


@client.command()
async def price(ctx):
    """ Command to get price and available stocks for all the items in the cart.
    The PriceTracker bot will also output the total cost of all the items.

    > !price
    EK-Vector RTX 2080 Ti RGB - Nickel + Plexi --- stock: 0 --- price: $249.99
    Total Cost: $249.99
    """
    cost = 0  # to accumulate the total cost
    for item in items:  # we must go through each item and output its info.
        print(items)

        # each file has a unique filepath and must be read accordingly.
        filepath = r'C:\Users\adi2m\Documents\\' + item + '.csv'
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.readlines()
            result = []

        # grab the available stock amount, full item name, price and potential
        # saving amount from the csv file and output the information.
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

        if not result:  # when no such item is found
            await ctx.send('Invalid Search')
        else:  # output its corresponding information
            await ctx.send(result[1] + ' --- stock: ' + result[0] + ' --- price: ' + result[2])
    await ctx.send('Total Cost: $' + str(cost))  # output total cost


@client.command()
async def help(ctx):
    """ Command to get the description and demo of all the other commands.
    """
    await ctx.send('!add:'
                   'search and add computer parts to cart'
                   '> !add'
                   'Please enter your item:'
                   '> RTX 2080'
                   'Added to list: RTX 2080'
                   ''
                   '!price:'
                   'get price and available stocks for all the items in the cart.'
                   'The PriceTracker bot will also output the total cost of all the items.'
                   '> !price'
                   'EK-Vector RTX 2080 Ti RGB - Nickel + Plexi --- stock: 0 - -- price: $249.99'
                   'Total Cost: $249.99')


client.run(TOKEN)
