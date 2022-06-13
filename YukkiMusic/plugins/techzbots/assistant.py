from pyrogram import Client, filters
from YukkiMusic.misc import SUDO_USERS as SUDOERS
from YukkiMusic.core.userbot import assistants
from YukkiMusic.utils.database import get_client

if 1 in assistants:
    ASS1 = await get_client(1)

if 2 in assistants:
    ASS2 = await get_client(2)

if 3 in assistants:
    ASS3 = await get_client(3)

if 4 in assistants:
    ASS4 = await get_client(4)

if 5 in assistants:
    ASS5 = await get_client(5)

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
