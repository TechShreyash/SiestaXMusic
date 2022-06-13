from pyrogram import Client, filters
from YukkiMusic.misc import SUDO_USERS as SUDOERS

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
