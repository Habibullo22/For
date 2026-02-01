import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3

BOT_TOKEN = "8161107014:AAGBWEYVxie7-pB4-2FoGCPjCv_sl0yHogc"
ADMIN_ID = 5815294733

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# DB
db = sqlite3.connect("users.db")
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    usdt REAL DEFAULT 0,
    rub REAL DEFAULT 0,
    uzs INTEGER DEFAULT 0
)
""")
db.commit()

@dp.message(CommandStart())
async def start(msg: types.Message):
    user_id = msg.from_user.id
    username = msg.from_user.username or ""

    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)",
        (user_id, username)
    )
    db.commit()

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🌐 Brauzerda ochish",
            web_app=WebAppInfo(url="https://YOUR-REPLIT-URL.repl.co")
        )]
    ])

    await msg.answer(
        "🎰 Xush kelibsiz!\nReal kazino mini-ilovasi.",
        reply_markup=kb
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
