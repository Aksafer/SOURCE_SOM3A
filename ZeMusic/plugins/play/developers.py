import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["اسبايد","المبرمج اسبايد","مبرمج السورس","مبرمج"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/108f3b057ff88b20bbbe0.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪Ꭵ᥉ ρᎥძᥱᖇ❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @Y_D_ll ❫
◉ 𝙸𝙳      : ❪ `6092147148` ❫
◉ 𝙱𝙸𝙾    : ❪ وتبقي أنتي وحدك #تكفيني عن الجميع ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Ꭵ᥉ ρᎥძᥱᖇ", url=f"https://t.me/Y_D_ll"), 
                 ],[
                   InlineKeyboardButton(
                        "𝗦𝗼𝗨𝗿𝗖𝗲 𝗦𝗼𝗠𝟯𝗮", url=f"https://t.me/SOURCE_SOM3A"),
                ],

            ]

        ),

    )
