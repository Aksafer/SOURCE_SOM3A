import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›","سمعه","السورس", "سورس مين"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e6f815307a347ec6e17d5.mp4",
        caption=f"""⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ժᥱ᥎ Ⴆ᥆ƚ", url=f"https://t.me/Y_D_ll"), 
                    
                
                    InlineKeyboardButton(
                        "‹ ᘜᖇ᥆υρ ›", url=f"https://t.me/YR_HC"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "‹ ᥉᥆υᖇᥴᥱ ›", url=f"https://t.me/SOURCE_SOM3A"),
                
        ],

            ]

        ),

    )

