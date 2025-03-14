# Kawaii Discord Bot

## Overview
Kawaii is a feature-rich Discord bot designed to enhance user interaction by providing anime recommendations using machine learning, general chat capabilities with a locally hosted LLM, and various fun commands. It supports anime/manga search using AniList, image-based anime search using SauceNAO, joke-telling, dice rolling, and more.

## Features
- **Anime & Manga Search**: Fetch details about anime and manga from AniList.
- **Anime Recommendation**: Uses machine learning to suggest anime based on user preferences.
- **Image Search**: Identify anime using an image through SauceNAO.
- **Chatbot**: Engage in general conversations with a locally hosted LLM.
- **Fun Commands**: Tell jokes, roll dice, and quote messages.
- **Admin Commands**: Close the bot with administrator privileges.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required dependencies

### Clone the Repository
```sh
git clone https://github.com/TheREALCleo/DiscordBot.git
cd DiscordBot
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Environment Setup
Create a `.env` file in the root directory and add your Discord bot token:
```
DISCORD_TOKEN=your_bot_token_here
```

## Running the Bot
To start the bot, run:
```sh
python main.py
```

## Commands
| Command | Description |
|---------|-------------|
| `!help` | Displays available commands |
| `!isWorking` | Checks if the bot is online |
| `!anime <name>` | Searches for anime details |
| `!manga <name>` | Searches for manga details |
| `!genre <genre>` | Lists anime from a specific genre |
| `!image` | Identifies anime from an uploaded image |
| `!funny` | Tells a joke |
| `!rolldie [number]` | Rolls a die with the specified number of sides (default: 1) |
| `!quote` | Quotes a replied-to message |
| `!close` | Shuts down the bot (Admin only) |

## Error Handling
- **Unknown Command**: Displays an error message if the command is not recognized.
- **Missing Role**: Informs the user if they lack the required role.
- **Command Cooldown**: Prevents spamming by enforcing cooldowns.

## Dependencies
- **Core**: `discord.py`, `python-dotenv`
- **Web Scraping**: `requests`, `beautifulsoup4`, `urllib3`

## Contact
For any issues or suggestions, please open an issue in the repository.

