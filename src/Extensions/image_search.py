import requests
import urllib.parse
import json
from typing import Final
from dotenv import load_dotenv
import os

load_dotenv()
API: Final[str] = os.getenv("Sauce_NAO_API")

# trace.moe searcher
"""def anime_image_search(url: str):
    data=requests.get("https://api.trace.moe/search?url={}"
    .format(urllib.parse.quote_plus(f"{url}"))
    ).json()

    top_result:dict=data["result"][0]
    
    result={}
    result["id"]=top_result["anilist"]
    result["result_accuracy"]=f"{top_result["similarity"]:.4f}"
    result["episode"]=top_result["episode"] or "N/A"

    minutes = int(top_result["from"] // 60)
    seconds = int(top_result["from"] % 60)

    result["timestamp"]=f"{minutes:02}:{seconds:02}"
    result["image"]=top_result["image"]

    if result:
        return result
    return None
    """


def image_searching(url: str) -> tuple[dict, int]:
    # Image URL or file
    image_url_1 = "https://preview.redd.it/p3om6h0kp9b81.jpg?width=640&crop=smart&auto=webp&s=320670a2406571581e3374028daa86f9075817e6"
    image_url_2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqUoFuKftVE-CMKalMi6R798W443lIcsdOng&s"
    image_url_3 = "https://static.wikia.nocookie.net/jjba/images/5/50/GiornoMafiaBoss.png/revision/latest/scale-to-width-down/985?cb=20210303144939&path-prefix=fr"

    # SauceNAO API endpoint
    endpoint = "https://saucenao.com/search.php"

    # Parameters for the API request
    params = {
        "output_type": 2,  # JSON output
        "api_key": API,
        "url": url,
    }

    # Send the request
    response = requests.get(endpoint, params=params)

    # Check for successful response
    if response.status_code == 200:
        data = response.json()
        # Display the closest result
        best_result = data["results"][0]
        print(best_result)
        try:
            if best_result["data"]["source"]:
                if any(
                    word.find("manga") != -1 for word in best_result["data"]["ext_urls"]
                ):
                    return (best_result, 1)  # flag 1 for manga
                else:
                    return (best_result, 0)  # flag 0 for anime
        except:
            return None


if __name__ == "__main__":
    # print(anime_image_search("https://pbs.twimg.com/media/Fl5phkDWQAAleAA.jpg"))
    # print(requests.get("https://api.trace.moe/me").json()) #request remaining
    print(
        image_searching(
            "https://static1.srcdn.com/wordpress/wp-content/uploads/2024/09/dandadan-episode-1-serpoian-banana.jpg"
        )
    )
