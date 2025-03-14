import requests
import re
from bs4 import BeautifulSoup


url = "https://graphql.anilist.co"


def remove_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


# Function to truncate text if it exceeds a certain length
def truncate_text(text, max_length=1024):
    return text if len(text) <= max_length else text[: max_length - 3] + "..."


# which function to call
def decide(name: str, flag: int):
    if flag == 0:
        return fetch_anime_details(name)
    else:
        return fetch_manga_details(name)


def fetch_manga_details(data):
    url = "https://graphql.anilist.co"

    query = """
    query ($search: String) {
          Media(search: $search, type: MANGA) {
            id
            title {
              romaji
              english
            }
            status
            chapters
            volumes
            averageScore
            genres
            description
            popularity
            coverImage {
              extraLarge
            }
            bannerImage
            siteUrl      
        }
    }
    """
    variables = {"search": str(data)}

    response = requests.post(url, json={"query": query, "variables": variables})
    data = response.json()

    found = data["data"]["Media"]

    if found:
        media = data["data"]["Media"]
        result = {}

        result["title_romaji"] = media["title"]["romaji"] or "N/A"
        result["title_english"] = media["title"]["english"] or "N/A"
        result["chapters"] = media["chapters"] or "N/A"
        result["status"] = media["status"] or "N/A"
        result["volumes"] = media["volumes"] or "N/A"
        result["average_score"] = media["averageScore"] or "N/A"
        result["genres"] = ", ".join(media["genres"]) or "N/A"
        result["description"] = (
            truncate_text(remove_html_tags(media["description"])) or "N/A"
        )
        result["popularity"] = media["popularity"] or "N/A"
        result["cover_image_url"] = media["coverImage"]["extraLarge"]
        result["url"] = media["siteUrl"]
        result["banner"] = media["bannerImage"]
    else:
        return None
    return result


def fetch_anime_details(data):
    url = "https://graphql.anilist.co"

    query = """
    query ($id: Int $search: String) {
          Media(id: $id search: $search, type: ANIME) {
            id
            title {
              romaji
              english
            }
            episodes
            status
            season
            seasonYear
            studios{
              edges{
                isMain
                  node{
                    name
                    }
                }
            }
            averageScore
            genres
            description
            popularity
            coverImage {
              extraLarge
            }
            bannerImage
            siteUrl      
        }
    }
    """
    variables = {"search": str(data)}

    response = requests.post(url, json={"query": query, "variables": variables})
    data = response.json()

    found = data["data"]["Media"]

    if found:
        media = data["data"]["Media"]
        result = {}

        result["title_romaji"] = media["title"]["romaji"]
        result["title_english"] = media["title"]["english"] or "N/A"
        result["episodes"] = media["episodes"] or "N/A"
        result["status"] = media["status"] or "N/A"
        result["season"] = media["season"] or "N/A"
        result["season_year"] = media["seasonYear"] or "N/A"
        result["studios"] = [
            studio["node"]["name"]
            for studio in media["studios"]["edges"]
            if studio["isMain"]
        ] or "N/A"
        result["average_score"] = media["averageScore"] or "N/A"
        result["genres"] = ", ".join(media["genres"]) or "N/A"
        result["description"] = (
            truncate_text(remove_html_tags(media["description"])) or "N/A"
        )
        result["popularity"] = media["popularity"] or "N/A"
        result["cover_image_url"] = media["coverImage"]["extraLarge"]
        result["url"] = media["siteUrl"]
        result["banner"] = media["bannerImage"]
    else:
        return None
    return result


def genre_search(genre: str):
    url = "https://graphql.anilist.co"

    query = """
    query ($genre: String) {
      Page(page: 1, perPage: 5) {
        media(genre_in: [$genre], type: ANIME, sort: SCORE_DESC) {
          id
          title {
            romaji
            english
          }
          averageScore
          popularity
          genres
          siteUrl
          coverImage {
              extraLarge
            }
        }
      }
    }
    """

    variables = {"genre": genre}

    response = requests.post(url, json={"query": query, "variables": variables})
    data = response.json()
    list = data["data"]["Page"]["media"]

    res = []
    if list:
        for anime in list:
            temp = {}
            temp["title"] = anime["title"]["romaji"]
            temp["english_title"] = anime["title"]["english"] or "N/A"
            temp["score"] = anime["averageScore"] or "N/A"
            temp["popularity"] = anime["popularity"] or "N/A"
            temp["url"] = anime["siteUrl"]
            temp["cover_image_url"] = anime["coverImage"]["extraLarge"]
            res.append(temp)
    else:
        return None

    return res


if __name__ == "__main__":
    # print(genre_search("horror"))
    # print(fetch_anime_details("22", True))
    # print(search_by_id(154887))
    print(decide("JoJo no Kimyou na Bouken: Ougon no Kaze", 1))
