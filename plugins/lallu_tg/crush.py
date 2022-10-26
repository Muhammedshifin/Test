import os
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging

PHOTO = 

@Client.on_message(filters.command("crush"))
async def aboutme(client, message):
    b
