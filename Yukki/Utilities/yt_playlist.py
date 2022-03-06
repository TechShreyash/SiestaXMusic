from Yukki import BOT_USERNAME
from youtubesearchpython import Playlist, ResultMode
import json
from Yukki.Database.spotifylimit import get_playlist_limit_sudoers
from config import PL_LIMIT
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def pl_buttons(id):
    buttons = [
            [
                InlineKeyboardButton(
                    text="🔀 Shuffle Play", callback_data=f"ytpls {id}"
                ),                                                   
            ],   
            [
                InlineKeyboardButton(
                    text="🎵 Play", callback_data=f"ytpl {id}"
                ),
                InlineKeyboardButton(
                    text="🗑 Close", callback_data="close_btn"
                ),                                   
            ],                
        ]
    return buttons

async def get_yt_playlist(url,user):
    try:
        if PL_LIMIT == "TRUE":
            sudos = await get_playlist_limit_sudoers()
        r = Playlist.get(url, mode = ResultMode.json)
        data = json.loads(r)
        pl_name = data["info"]["title"]
        ch_name = data["info"]["channel"]["name"]        
        vid_link = data["info"]["link"]
        vid_count = data["info"]["videoCount"]        
        video_list = data["videos"]
        final_list = []
        for i in video_list:
            title = str(i["title"])
            channel = str(i["channel"]["name"])
            search = title + " " + channel
            search = search.replace("|","").strip()
            final_list.append(search)
        if PL_LIMIT == "TRUE":
            if user not in sudos:
                tracks_list = final_list[0:20]
        return [pl_name,ch_name,vid_count,vid_link,final_list]
    except Exception as e:
        print(str(e))
        return "errrorrr"
    
async def play_yt_playlist(message):
    playlist_url = message.text.replace("/play","").replace(f"/play@{BOT_USERNAME}","").strip()
    data = await get_yt_playlist(playlist_url,message.from_user.id)
    pl_id = data[3].replace("http://www.youtube.com/playlist?list=","").strip()
    text = f"🔮 **Playlist Name:** `{data[0]}`\n🧿 **Playlist By:** `{data[1]}`\n🎰 **Number of Videos:** `{data[2]}`"
    await message.reply_photo("Utils/ytplaylist.jpg",caption=text,reply_markup=InlineKeyboardMarkup(pl_buttons(pl_id)))
