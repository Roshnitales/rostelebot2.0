import os
import requests
from pyrogram.types import Message

def shorten_link(link):
    try:
        api_key = os.environ.get("TNSHORT_API_KEY")
        res = requests.get(f"https://tnshort.net/api?api={api_key}&url={link}")
        return res.json().get("shortenedUrl", link)
    except:
        return link

async def search_movie(client, message: Message):
    query = message.text.strip()
    if not query:
        await message.reply("❌ Please enter a movie name.")
        return

    movie_channel_id = int(os.environ.get("MOVIE_CHANNEL_ID"))
    results = []

    async for msg in client.search_messages(chat_id=movie_channel_id, query=query):
        if msg.text:
            results.append(msg.text)

    if not results:
        await message.reply("❌ No results found.")
        return

    for result in results[:5]:
        await message.reply(shorten_link(result))
      
