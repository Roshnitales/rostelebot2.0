import os
from pyrogram import Client, filters
from pyrogram.types import Message
from modules.movie_handler import search_movie

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_NAME = os.environ.get("BOT_NAME")
ADMIN_ID = int(os.environ.get("ADMIN_ID"))
WELCOME_IMG_URL = os.environ.get("WELCOME_IMG_URL")

bot = Client("rosmoviebot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    await message.reply_photo(
        photo=WELCOME_IMG_URL,
        caption=f"👋 Welcome to **{BOT_NAME}**!\n\n🔍 Send any movie name to search.\n📥 You’ll get the download link directly!"
    )

@bot.on_message(filters.private & filters.text & ~filters.command("start"))
async def movie_search_handler(client, message: Message):
    await search_movie(client, message)

bot.run()