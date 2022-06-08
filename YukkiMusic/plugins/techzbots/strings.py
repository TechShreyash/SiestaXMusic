from YukkiMusic import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MUSIC_BOT_NAME as BOT_NAME

BOT_USERNAME = app.username
START_TEXT = f"""
✨ **ها يحلوو هياتني  🌚♥️ !**
**يمكنك استخدام [{BOT_NAME}](https://t.me/{BOT_USERNAME}) لتشغيل الاغاني والفيديوهات في مجموعتك.**
💡 **اكتشف جميع اوامر البوت وفهمها من خلال الضغط على زر  ➤ 📚 الاوامر **
"""

COMMANDS_TEXT = f"""
✨ **هلا حبب 🌚💞 !**
**اضفط على الزر ادناه لمعرفة اوامري .**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="📚 الاوامر", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔧 الاعدادات", callback_data="settings_helper"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="📣 قناة التحديثات", url="https://t.me/trztb"
            ),
            InlineKeyboardButton(
                text="💬 اصنع بوتك الخاص", url="https://t.me/ov_tr"
            ),                       
        ],        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="➕ اضفني لمجموعة ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),            
        ],
        [   
            InlineKeyboardButton(
                text="📚 الاوامر", callback_data="command_menu"
            ),                       
        ],
        [
            InlineKeyboardButton(
                text="📣 قناة التحديثات", url="https://t.me/trztb"
            ),
            InlineKeyboardButton(
                text="💬 مطور السورس", url="https://t.me/ov_tr"
            ),                       
        ],        
    ]
)

COMMANDS_BUTTON_USER = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="اوامر الادمن", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="اوامر البوت", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="اوامر التشغيل", callback_data="play_cmd"
            ),            
            InlineKeyboardButton(
                text="اوامر اضافية", url="https://telegra.ph/SiestaXMusic-Commands-03-13-2"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ عودة", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 اغلاق", callback_data="close_btn"
            ),            
        ],                
    ]
)

COMMANDS_BUTTON_SUDO = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="اوامر الادمن", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="اوامر البوت", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="اوامر التشغيل", callback_data="play_cmd"
            ),
            InlineKeyboardButton(
                text="اوامر المطورين", url="https://telegra.ph/SiestaXMusic-Commands-03-13"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="اوامر اضافية", url="https://telegra.ph/SiestaXMusic-Commands-03-13-2"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ عودة", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 اغلاق", callback_data="close_btn"
            ),            
        ],                
    ]
)

BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ عودة", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 اغلاق", callback_data="close_btn"
            ),            
        ],                        
    ]
)

SUDO_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="اوامر المطورين", url="https://telegra.ph/SiestaXMusic-Commands-03-13"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ عودة", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 اغلاق", callback_data="close_btn"
            ),            
        ],                        
    ]
)


ADMIN_TEXT = f"""
✅--**اوامر الادمنية:**--
c ضع الحرف قبل الامر لتنفيذه في المجموعة.
/pause أو /cpause - توقف الموسيقى المُشغلة.
/seek [ عدد ثواني ] - للتقدم في الاغنية حسب الوقت المعطى
/seekback [ عدد الثواني ] - للعودة في الاغنية حسب الوقت المعطى 
/resume or /cresume- استئناف الموسيقى المشغلة.
/mute or /cmute- كتم صوت الموسيقى.
/unmute or /cunmute- الغاء الكتم عن البوت.
/skip or /cskip- التخطي للاغنية التالية في قائمة التشغيل.
/stop or /cstop- ايقاف كل الاغاني.
/shuffle or /cshuffle- ترتيب عشوائي للاغاني في قائمة التشغيل.
✅--**التخطي المحدد:**--
/skip or /cskip [رقم (مثلا : 3)] 
    - يتخطى الموسيقى إلى الرقم المحدد في قائمة الانتظار.  مثال: سيتخطى / skip 3 الموسيقى إلى الموسيقى في قائمة الانتظار الثالثة ويتجاهل الموسيقى 1 و 2 في قائمة الانتظار
✅--**وضع الحلقة:**--
/loop or /cloop [enable/disable] or [رقم بين  1-10] 
    - عند التنشيط ، يقوم البوت بتكرار تشغيل الموسيقى الحالية إلى 1-10 مرات في الدردشة الصوتية.  افتراضي إلى 10 مرات.
"""
AUTH_TEXT = """
✅--**اوامر المعتمدين:**--
المستخدمين المعتمدون سيستطيعون استخدام جميع اوامر المشرفين بدون رفعهم مشرف في المجموعة 
/auth [اليوزر] - اضف شخص لقائمة المعتمدين.
/unauth [اليوزر] - لحذف شخص من القائمة.
/authusers - جلب قائمة المعتمدين.
"""

AUTH_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ عودة", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 اغلاق", callback_data="close_btn"
            ),            
        ],                        
    ]
)

BOT_TEXT = """
✅--**اوامر البوت:**--
/stats - الحصول على توب 10 محادثات و توب 10 اغاني وتوب 10 اغاني الخ...
/sudolist - فحص قائمه المطورين 
/lyrics [اسم الاغنية] - لجلب كلمات الاغاني من الويب.
/song [اسم الاغنية] or [الرابط] - لتحميل اغنية من اليوتيوب.
c ضع الحرف قبل الامر لتنفيذه في القناة
/queue or /cqueue- تفقد قائمة الانتظار.
"""

PLAY_TEXT = """
✅--**اوامر التشغيل:**--
الاوامر المتوفرة = play , vplay , cplay
c ضع الحرف قبل الامر لتنفيذه في القناة.
v ضع الحرف قبل الامر لتنفيذ في الفيديو.
/play or /vplay or /cplay  - سيبدأ البوت بتشغيل الصوت او الفيديو في مجموعتك أو قناتك.
/channelplay [يوزر القناة ] or [Disable] - اربط القناة مجموعتك او ارفع البوت مشرف على قناتك وقم بتشغيل الاغاني على القناة من خلال مجموعتك .
✅--**قائمة تشغيلك في السيرفر:**--
/playlist  - لتفقد الاغاني المضافه في قائمة التشغيل .
/deleteplaylist - لحذف قائمة التشغيل المضافه
/play  - بدأ تشغيل قائمة تشغيلك المضافه.
"""


BASIC_TEXT = """
💠 **اوامر اساسية:**
/start - تشغيل البوت
/help - الحصول على مساعدة
/play - بدأ تشغيل اغنية او فيديو 
/vplay - بدأ تشغيل فيديو 
/settings - تفقد الاعدادات في مجموعتك 
**بعض الاوامر المفيدة  :** 
/pause /resume /skip /end /loop /shuffle
"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ عودة", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 اغلاق", callback_data="close_btn"
            ),            
        ],                        
    ]
)

ADMIN_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="اوامر المعتمدين", callback_data="auth_cmds"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ عودة", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 اغلاق", callback_data="close_btn"
            ),            
        ],                        
    ]
)

COMMAND_MENU_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🔍 الاوامر الاساسية", callback_data="basic_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="📚 اوامر اضافية", callback_data="advanced_cmd"
            ),
        ],
        [
            InlineKeyboardButton(
                text="↪️ عودة", callback_data="open_start_menu"
            ),
            InlineKeyboardButton(
                text="🔄 اغلاق", callback_data="close_btn"
            ),            
        ],                        
    ]
)
