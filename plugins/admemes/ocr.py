

from telegram import ChatAction,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext.dispatcher import run_async
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler,PicklePersistence
import logging
import os
from functools import wraps
import requests

API_KEY = os.environ.get("API_KEY","") 

def send_typing_action(func)
    """Sends typing action while processing func command."""
