**_1st_** place out of **_140_** participants at **_DeerHacks 2022_**: https://devpost.com/software/pricetracker 

## Overview
Tech4U is an innovative discord bot that implements web scrapping with UIPath software and allows you to keep track of the prices and stocks of your most desired tech products.

## Inspiration
Since this was the first hackathon for most of our group, we wanted to work on a project where we could learn something new while sticking to familiar territory. Thus we settled on programming a discord bot, something all of us have extensive experience using, that works with UiPath, a tool equally as intriguing as it is foreign to us. We wanted to create an application that will allow us to track the prices and other related information of tech products in order to streamline the buying process and enable the user to get the best deals. We decided to program a bot that utilizes user input, web automation, and web-scraping to generate information on various items, focusing on computer components.

## What it does
Once online, our PriceTracker bot runs under two main commands: !add and !price. Using these two commands, a few external CSV files, and UiPath, this stores items input by the user and returns related information found via UiPath's web-scraping features. A concise display of the product’s price, stock, and sale discount is displayed to the user through the Discord bot.

## How we built it
We programmed the Discord bot using the comprehensive discord.py API. Using its thorough documentation and a handful of tutorials online, we quickly learned how to initialize a bot using Discord's personal Development Portal and create commands that would work with specified text channels. To scrape web pages, in our case, the Canada Computers website, we used a UiPath sequence along with the aforementioned CSV file, which contained input retrieved from the bot's "!add" command. In the UiPath process, each product is searched on the Canada Computers website and then through data scraping, the most relevant results from the search and all related information are processed into a csv file. This csv file is then parsed through to create a concise description which is returned in Discord whenever the bot's "!prices" command was called.

## Challenges we ran into
The most challenging aspect of our project was figuring out how to use UiPath. Since Python was such a large part of programming the discord bot, our experience with the language helped exponentially. The same could be said about working with text and CSV files. However, because automation was a topic none of us hardly had any knowledge of; naturally, our first encounter with it was rough. Another big problem with UiPath was learning how to use variables as we wanted to generalize the process so that it would work for any product inputted. Eventually, with enough perseverance, we were able to incorporate UiPath into our project exactly the way we wanted to.

## Accomplishments that we're proud of
Learning the ins and outs of automation alone was a strenuous task. Being able to incorporate it into a functional program is even more difficult, but incredibly satisfying as well. Albeit small in scale, this introduction to automation serves as a good stepping stone for further research on the topic of automation and its capabilities.

## What we learned
Although we stuck close to our roots by relying on Python for programming the discord bot, we learned a ton of new things about how these bots are initialized, the various attributes and roles they can have, and how we can use IDEs like Pycharm in combination with larger platforms like Discord. Additionally, we learned a great deal about automation and how it functions through UiPath which absolutely fascinated us the first time we saw it in action. As this was the first Hackathon for most of us, we also got a glimpse into what we have been missing out on and how beneficial these competitions can be. Getting the extra push to start working on side-projects and indulging in solo research was greatly appreciated.

## What's next for Tech4U
We went into this project with a plethora of different ideas, and although we were not able to incorporate all of them, we did finish with something we were proud of. Some other ideas we wanted to integrate include: scraping multiple different websites, formatting output differently on Discord, automating the act of purchasing an item, taking input and giving output under the same command, and more.
