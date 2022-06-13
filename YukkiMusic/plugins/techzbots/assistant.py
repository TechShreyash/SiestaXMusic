from pyrogram import Client, filters
from YukkiMusic.misc import SUDO_USERS as SUDOERS

@Client.on_message(
    filters.private
    & filters.incoming
    & ~filters.service
    & ~filters.edited
    & ~filters.me
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.user(SUDOERS)
)
async def assistant_(client, message):
    await message.reply_text("test")
