from os import environ,sys,mkdir,path
import logging
from sys import executable

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(message)s",
    handlers = [logging.FileHandler('bot.log'), logging.StreamHandler()]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


try:
    API_ID = int(environ['API_ID'])
    API_HASH = environ['API_HASH']
    BOT_TOKEN = environ['BOT_TOKEN']
    OWNER_ID = 1957296068 #int(environ['OWNER_ID'])
except KeyError:
    pass
# Optional Variable
SUDO_USERS = environ.get("SUDO_USERS",None)
AUTH_CHATS = environ.get('AUTH_CHATS',None )
LOG_GROUP = environ.get("LOG_GROUP", None)
if LOG_GROUP:
    LOG_GROUP = int(LOG_GROUP)
BUG = environ.get("BUG", None)
if BUG:
    BUG = int(BUG)
