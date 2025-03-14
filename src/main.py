from typing import Final
import os
from dotenv import load_dotenv
import discord
from Extensions import AnimeSearch
from discord.ext import commands
from Discord_Messages import commands_file
from Discord_Messages import embeds
from Extensions import image_search


load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(
    command_prefix="!", intents=intents, help_command=None
)  # instance of a client, connection to discord


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f"[{channel}] {username}: {user_message}")

    await client.process_commands(message)  # for using commands

    if message.content.startswith("kawaii"):
        await message.channel.send(
            f"🌸Hello {message.author}!, I'm Kawaii and am here to assist you🌸\n🌸Type **!help** for commands list🌸"
        )


@client.command()
async def isWorking(ctx):
    embed = embeds.embed_working()
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    embed = embeds.embed_help()
    await ctx.send(embed=embed)


@client.command()
async def anime(ctx, *args):
    arguement = " ".join(args)
    found = AnimeSearch.fetch_anime_details(arguement)

    if not found:
        await ctx.send(f"No Entries Found")
        return
    else:
        embed = embeds.embed_anime_search(found)

    await ctx.send(embed=embed)


@client.command()
async def manga(ctx, *args):
    arguement = " ".join(args)
    found = AnimeSearch.fetch_manga_details(arguement)

    if not found:
        await ctx.send(f"No Entries Found")
        return
    else:
        embed = embeds.embed_manga_search(found)

    await ctx.send(embed=embed)


@client.command()
async def genre(ctx, args):
    found = AnimeSearch.genre_search(str(args))

    if not found:
        await ctx.send(f"No Entries Found")
        return
    else:
        for anime in found:  # anime is dict and found is a list
            embed = embeds.embed_genre_search(anime)
            await ctx.send(embed=embed)


@client.command()
@commands.cooldown(4, 60, commands.BucketType.user)
async def image(ctx):
    url = ctx.message.attachments[0].url
    search_result: tuple = image_search.image_searching(str(url))
    if search_result is None:
        await ctx.send(
            "Not Found\nPlease provide a higher quality image or the image is not in the Database"
        )
        return

    details = AnimeSearch.decide(search_result[0]["data"]["source"], search_result[1])

    if details is None:
        await ctx.send(
            "Not Found\nPlease provide a higher quality image or the image is not in the Database"
        )
        return
    embed = embeds.embed_image_search(search_result, details)

    await ctx.send(embed=embed)


@client.command()
async def funny(ctx):
    await ctx.send(commands_file.return_joke())


@client.command()
async def rolldie(ctx, arg=1):
    await ctx.send(commands_file.roll_die(int(arg)))


@client.command()
async def quote(ctx):
    channel = ctx.channel  # get channel where command was used
    msg = await channel.fetch_message(
        ctx.message.reference.message_id
    )  # fetching message which command replied to
    quote_message = f"“{msg.content}”\n\t — {msg.author.display_name}"
    await ctx.send(f"{quote_message}")


# error handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print("User Entered Unknown Command")
        await ctx.send("Invalid command. Please try again.")
    if isinstance(error, commands.MissingRole):
        print("Role 'Admin' is required to run this command.")
        await ctx.send("You do not have the required role to use this command.")
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            f"Please wait {error.retry_after:.2f} seconds before using this command again."
        )
    else:
        print(f"An error occurred: {error}")


# closing the bot
@client.command()
@commands.has_permissions(administrator=True)
async def close(ctx):
    embed = embeds.embed_close()
    await ctx.send(embed=embed)
    print(f"{ctx.author} has shut the Bot down")
    await client.close()


def main():
    client.run(TOKEN)


if __name__ == "__main__":
    main()
