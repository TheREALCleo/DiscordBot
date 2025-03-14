import discord


def embed_help():
    embed = discord.Embed(
        title="Commands List:", color=discord.Color.from_rgb(233, 30, 99)
    )
    embed.set_author(name="🌸Kawaii_Bot🌸\nv2.0")
    embed.set_thumbnail(url="https://i.redd.it/8evh7ppgoqjc1.jpeg")
    embed.add_field(name="**!funny**", value="Returns a funny Quote", inline=False)
    embed.add_field(
        name="**!rolldie (args->number of dices)**", value="Rolls Dice", inline=False
    )
    embed.add_field(name="**!quote**", value="Quotes Messages", inline=False)
    embed.add_field(
        name="**!anime (arg->Name of the Anime)**",
        value="Returns details about the Anime",
        inline=False,
    )
    embed.add_field(
        name="**!manga (arg->Name of the Manga)**",
        value="Returns details about the Manga",
        inline=False,
    )
    embed.add_field(
        name="**!genre (arg->Genre name)**",
        value="Returns Top 5 Animes with the aforementioned genre",
        inline=False,
    )
    embed.add_field(
        name="**!image (arg->Image of an Anime Scene)**",
        value="Returns Metadata of Image and its Anime Details",
        inline=False,
    )
    embed.add_field(name="**ADMIN COMMANDS**", value=f"{'-'*21}", inline=False)
    embed.add_field(name="**!isWorking**", value="Checks Working Status", inline=False)
    embed.add_field(name="**!close**", value="Closes the Bot Application", inline=False)
    return embed


def embed_anime_search(found: dict):
    embed = discord.Embed(
        title=f"{found["title_romaji"]}",
        url=f"{found["url"]}",
        description=f"{found["title_english"]}",
        color=discord.Color.from_rgb(233, 30, 99),
    )
    embed.set_author(name="🌸From AniList🌸")
    if found["cover_image_url"]:
        embed.set_thumbnail(url=f"{found["cover_image_url"]}")
    embed.add_field(name="**Episodes**", value=f"{found["episodes"]}", inline=True)
    embed.add_field(name="**Status**", value=f"{found["status"]}", inline=True)
    embed.add_field(
        name="**Season**",
        value=f"{found["season"]} {found["season_year"]}",
        inline=True,
    )
    embed.add_field(
        name="**Studio**", value=f"{" ".join(found["studios"])}", inline=True
    )
    embed.add_field(name="**Score**", value=f"{found["average_score"]}", inline=True)
    embed.add_field(
        name="**User Ratings**", value=f"{found["popularity"]}+", inline=True
    )
    embed.add_field(name="**Genres**", value=f"{found["genres"]}", inline=False)
    embed.add_field(
        name="**Description**", value=f"{found["description"]}", inline=False
    )
    if found["banner"]:
        embed.set_image(url=f"{found["banner"]}")
    return embed


def embed_manga_search(found: dict):
    embed = discord.Embed(
        title=f"{found["title_romaji"]}",
        url=f"{found["url"]}",
        description=f"{found["title_english"]}",
        color=discord.Color.from_rgb(233, 30, 99),
    )
    embed.set_author(name="🌸From AniList🌸")
    if found["cover_image_url"]:
        embed.set_thumbnail(url=f"{found["cover_image_url"]}")
    embed.add_field(name="**Chapters**", value=f"{found["chapters"]}", inline=True)
    embed.add_field(name="**Volumes**", value=f"{found["volumes"]}", inline=True)
    embed.add_field(name="**Status**", value=f"{found["status"]}", inline=False)
    embed.add_field(name="**Score**", value=f"{found["average_score"]}", inline=True)
    embed.add_field(
        name="**User Ratings**", value=f"{found["popularity"]}+", inline=True
    )
    embed.add_field(name="**Genres**", value=f"{found["genres"]}", inline=False)
    embed.add_field(
        name="**Description**", value=f"{found["description"]}", inline=False
    )
    if found["banner"]:
        embed.set_image(url=f"{found["banner"]}")
    return embed


def embed_genre_search(anime: dict):
    embed = discord.Embed(
        title=f"{anime["title"]}",
        url=f"{anime["url"]}",
        description=f"{anime["english_title"]}",
        color=discord.Color.from_rgb(233, 30, 99),
    )
    if anime["cover_image_url"]:
        embed.set_thumbnail(url=f"{anime["cover_image_url"]}")
    embed.set_author(name="🌸From AniList🌸")
    embed.add_field(name="**Score**", value=f"{anime["score"]}", inline=True)
    embed.add_field(
        name="**User Reviews**", value=f"{anime["popularity"]}+", inline=True
    )
    return embed


def embed_close():
    embed = discord.Embed(
        title="🌸Shutting Down...🌸",
        description="🌸Thank You🌸",
        color=discord.Color.from_rgb(233, 30, 99),
    )
    embed.set_image(
        url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f314df3c-fe3a-4d05-a059-8aac06af49af/dg3n7ft-a9882377-7256-43c3-a9e8-37958f74f211.png/v1/fill/w_1192,h_670,q_70,strp/naa__20__by_rosedie91_dg3n7ft-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NzIwIiwicGF0aCI6IlwvZlwvZjMxNGRmM2MtZmUzYS00ZDA1LWEwNTktOGFhYzA2YWY0OWFmXC9kZzNuN2Z0LWE5ODgyMzc3LTcyNTYtNDNjMy1hOWU4LTM3OTU4Zjc0ZjIxMS5wbmciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.hrQHz2ZMM-GAmUuLo2TELIBquaaD_Jlr7FsDu6iuH9o"
    )
    return embed


def embed_working():
    embed = discord.Embed(
        title="🌸Bot is Working...🌸",
        description="🌸Hello Everyone🌸",
        color=discord.Color.from_rgb(233, 30, 99),
    )
    embed.set_image(url="https://pbs.twimg.com/media/Fl5phkDWQAAleAA.jpg")
    return embed


def embed_image_search(saucenao: tuple[dict, int], anilist):
    embed = discord.Embed(
        title=f"{anilist["title_romaji"]}",
        url=f"{anilist["url"]}",
        description=f"{anilist["title_english"]}",
        color=discord.Color.from_rgb(233, 30, 99),
    )
    embed.set_author(name="🌸From saucenao.com🌸")
    embed.add_field(
        name="**Accuracy**",
        value=f"{saucenao[0]["header"]["similarity"]}%",
        inline=True,
    )

    if saucenao[1] == 0:
        embed.add_field(
            name="**Episode**", value=f"{saucenao[0]["data"]["part"]}", inline=True
        )
        try:
            if saucenao[0]["data"]["est_time"]:
                embed.add_field(
                    name="**TimeStamp**",
                    value=f"{saucenao[0]["data"]["est_time"]}",
                    inline=True,
                )
        except:
            pass
        embed.add_field(name="", value=f"{'-'*24}", inline=False)
        embed.add_field(
            name="**Anime Details**", value=f"🌸From AniList🌸", inline=False
        )
        if saucenao[0]["header"]["thumbnail"]:
            embed.set_thumbnail(url=f"{saucenao[0]["header"]["thumbnail"]}")

        embed.add_field(
            name="**Episodes**", value=f"{anilist["episodes"]}", inline=True
        )
        embed.add_field(name="**Status**", value=f"{anilist["status"]}", inline=True)
        embed.add_field(
            name="**Season**",
            value=f"{anilist["season"]} {anilist["season_year"]}",
            inline=True,
        )
        embed.add_field(
            name="**Studio**", value=f"{" ".join(anilist["studios"])}", inline=True
        )
        embed.add_field(
            name="**Score**", value=f"{anilist["average_score"]}", inline=True
        )
        embed.add_field(
            name="**User Ratings**", value=f"{anilist["popularity"]}+", inline=True
        )
        embed.add_field(name="**Genres**", value=f"{anilist["genres"]}", inline=False)
        embed.add_field(
            name="**Description**", value=f"{anilist["description"]}", inline=False
        )
        if anilist["cover_image_url"]:
            embed.set_image(url=f"{anilist["cover_image_url"]}")
    else:
        embed.add_field(
            name="**From**", value=f"{saucenao[0]["data"]["part"]}", inline=True
        )
        embed.add_field(name="", value=f"{'-'*24}", inline=False)
        embed.add_field(
            name="**Manga Details**", value=f"🌸From AniList🌸", inline=False
        )
        embed.set_thumbnail(url=f"{saucenao[0]["header"]["thumbnail"]}")
        embed.add_field(
            name="**Chapters**", value=f"{anilist["chapters"]}", inline=True
        )
        embed.add_field(name="**Volumes**", value=f"{anilist["volumes"]}", inline=True)
        embed.add_field(name="**Status**", value=f"{anilist["status"]}", inline=False)
        embed.add_field(
            name="**Score**", value=f"{anilist["average_score"]}", inline=True
        )
        embed.add_field(
            name="**User Ratings**", value=f"{anilist["popularity"]}+", inline=True
        )
        embed.add_field(name="**Genres**", value=f"{anilist["genres"]}", inline=False)
        embed.add_field(
            name="**Description**", value=f"{anilist["description"]}", inline=False
        )
        if anilist["cover_image_url"]:
            embed.set_image(url=f"{anilist["cover_image_url"]}")

    return embed
