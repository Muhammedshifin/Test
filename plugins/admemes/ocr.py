

from telegram import ChatAction,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext.dispatcher import run_async
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler,PicklePersistence
from plugins.helper_functions.cust_p_filters import f_onw_fliter
import logging
import os
from functools import wraps
import requests

API_KEY = os.environ.get("API_KEY","") 

def send_typing_action(func)
    """Sends typing action while processing func command."""
    
    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return func(update, context,  *args, **kwargs)

    return command_func


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


@run_async
@send_typing_action
@Client.on_message(
    filters.command("ocr") &
    f_onw_fliter
)
async def ocr(client, message):
