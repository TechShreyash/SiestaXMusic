from pyrogram import Client, filters
from YukkiMusic.misc import SUDO_USERS as SUDOERS
from YukkiMusic.core.userbot import assistants
from YukkiMusic.utils.database import get_client
from YukkiMusic import userbot

ASS1 = userbot.one

ASS2 = userbot.two

filtero = filters.private & filters.incoming & ~filters.service & ~filters.edited & ~filters.me & ~filters.bot & ~filters.via_bot

@Client.on_message(filtero)
async def assistant_(client, message):
    await message.reply_text("hi")
