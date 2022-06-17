import sys

from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING1),
        )
        self.two = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING2),
        )
        self.three = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING3),
        )
        self.four = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING4),
        )
        self.five = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING5),
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistant Clients")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("TechZBots")
                await self.one.join_chat("TechZBots_Support")                
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Started as {self.one.name}"
            )
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("TechZBots")
                await self.two.join_chat("TechZBots_Support")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Two Started as {self.two.name}"
            )
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("TechZBots")
                await self.three.join_chat("TechZBots_Support")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Three Started as {self.three.name}"
            )
        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("TechZBots")
                await self.four.join_chat("TechZBots_Support")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Four Started as {self.four.name}"
            )
        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("TechZBots")
                await self.five.join_chat("TechZBots_Support")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Five Started as {self.five.name}"
            )
    async def funcs(
      self,
      msg=None
      reply_msg_id=None,
      chat_id=None
      type="text",
      markup=None,
      caption=None,
      text=None
      media=None
    ):
      """
      All userbots will do this work can be done without errors ig
      PARAMS :
        type-> Type msg content : text|document|video|photo|gif|sticker
        caption -> needed you want to add caption to message if type is other than text
        text -> add if type is text
        markup -> if reply markup else None
        media -> if type is not text give id or url of media
        reply_msg_id -> id of msg you want to reply else None
        chat_id -> if chat_id other than current chat id
        msg -> current msg
      """
      
        if not chat_id:
            chat = msg.chat.id 
        else:
            chat = chat_id
        try:
            if type == "text":
                if not text:
                    return print("Nigga didn't gib text while mode is text")
                else:
                    for x in [self.one, self.two, self.three, self.four, self.five]:
                        await x.send_message(chat_id=chat, reply_to_message=reply_msg_id, text=text, reply_markup=markup)
                    return print("Done")
            elif type == "gif":
                if not media:
                    return print("bitch didnt give media url or id")
                else:
                    for x in [self.one, self.two, self.three, self.four, self.five]:
                        await x.send_animation(chat_id=chat, reply_to_message=reply_msg_id, animation=media, caption=caption, reply_markup=markup)
                    return print("Done")
            elif type == "photo":
                if not media:
                    return print("bitch didnt give media url or id")
                else:
                    for x in [self.one, self.two, self.three, self.four, self.five]:
                        await x.send_photo(chat_id=chat, reply_to_message=reply_msg_id, photo=media, caption=caption, reply_markup=markup)
                    return print("Done")
            elif type == "video":
                if not media:
                    return print("bitch didnt give media url or id")
                else:
                    for x in [self.one, self.two, self.three, self.four, self.five]:
                        await x.send_animation(chat_id=chat, reply_to_message=reply_msg_id, animation=media, caption=caption, reply_markup=markup)
                    return print("Done")
            elif type == "sticker":
                if not media:
                    return print("print bitch didnt give id or url for media")
                else:
                    for x in [self.one, self.two, self.three, self.four, self.five]:
                        await x.send_sticker(chat_id=chat, reply_to_message=reply_msg_id, sticker=media, reply_markup=markup)
                    return print("done")
            else:
                if not media:
                    return print("bitch didnt give media")
                else:
                    for x in [self.one, self.two, self.three, self.four, self.five]:
                        await x.send_document(chat_id=chat, reply_to_message=reply_msg_id, document=media, caption=caption, reply_markup=markup)
                     return print("done")
        except Exception as e:
            return print(e)
