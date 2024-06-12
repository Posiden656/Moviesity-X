#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Auto Delete
AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", ""))
AUTO_DELETE_MSG = "<b>✍️ Nᴏᴛᴇ : Aʙᴏᴠᴇ Fɪʟᴇ Wɪʟʟ Bᴇ Dᴇʟᴇᴛᴇᴅ Wɪᴛʜɪɴ 05 Mɪɴᴜᴛᴇs..\nPʟᴇᴀsᴇ Mᴀᴋᴇ Sᴜʀᴇ Tʜᴀᴛ Yᴏᴜ Fᴏʀᴡᴀʀᴅ ⏩ Tʜɪs Fɪʟᴇ Tᴏ Yᴏᴜʀ Sᴀᴠᴇᴅ Mᴇssᴀɢᴇs ᴏʀ Fʀɪᴇɴᴅs.\n\n✍️ नोट : ऊपर दिया गया Fɪʟᴇ 5 मिनट बाद डिलीट हो जाएगा\nइसलिए कृपया इस Fɪʟᴇ को अपने किसी दोस्त को या Sᴀᴠᴇᴅ Mᴇssᴀɢᴇs में Fᴏʀᴡᴀʀᴅ ⏩ कर ले ।</b>"

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "👋 Hᴇʟʟᴏ {first}\n✨I'ᴍ Aɴ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ🤖\n━━━━━━━━━━━━━━━━━━━━━━━━━\n● Mʏ Jᴏʙ Is Tᴏ Sᴇɴᴅ Yᴏᴜ Fɪʟᴇs.\n● Yᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Oᴜʀ Cʜᴀɴɴᴇʟs.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = "<b>Hᴇʟʟᴏ {first}\n\nYᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Mʏ Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Mᴇ\n\nKɪɴᴅʟʏ Pʟᴇᴀsᴇ Jᴏɪɴ Cʜᴀɴɴᴇʟ</b>"

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>Bᴏᴛ Uᴘᴛɪᴍᴇ</b>\n{uptime}"
USER_REPLY_TEXT = "👋 Hᴇʟʟᴏ {first}\n✨I'ᴍ Aɴ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ🤖\n━━━━━━━━━━━━━━━━━━━━━━━━━\n● Mʏ Jᴏʙ Is Tᴏ Sᴇɴᴅ Yᴏᴜ Fɪʟᴇs.\n● Yᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Oᴜʀ Cʜᴀɴɴᴇʟs."

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
