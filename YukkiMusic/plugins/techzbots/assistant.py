from pyrogram import Client, filters
from YukkiMusic.misc import SUDO_USERS as SUDOERS
from YukkiMusic.core.userbot import assistants
from YukkiMusic.utils.database import get_client

if 1 in assistants:
    ASS1 = userbot.one

if 2 in assistants:
    ASS2 = userbot.two

@Client.on_message(
    filters.private
    & filters.incoming
    & ~filters.service
    & ~filters.edited
    & ~filters.me
    & ~filters.bot
    & ~filters.via_bot)
async def assistant_(client, message):
    await client.send_message(chat_id=message.from_user.id,text="test")
