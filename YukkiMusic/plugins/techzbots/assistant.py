from pyrogram import Client, filters
from YukkiMusic.misc import SUDO_USERS as SUDOERS
from YukkiMusic.core.userbot import assistants
from YukkiMusic.utils.database import get_client
from YukkiMusic import userbot

ASS1 = userbot.one

ASS2 = userbot.two

filtero = filters.private & filters.incoming & ~filters.service & ~filters.edited & ~filters.me & ~filters.bot & ~filters.via_bot

@ASS1.on_message(filtero)
@ASS2.on_message(filtero)
async def assistant_(client, message):
    await client.send_message(chat_id=message.from_user.id,text="test")
