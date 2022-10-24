import os
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from script import script

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# -- Constants -- #
PHOTO = "https://telegra.ph/file/9a33ba9ab6b3b3352e276.jpg"
CRUSH_TXT = """MY CRUSH DETAILS..❤️
Name : Fathima
Nick : Pathusz
Age : 3 months 
Father : Not Available 
Notice : She is My Girl Freind
Not propose She
Thank You"""
# -- Constants End -- #


@Client.on_message(filters.command("crush"))
async def aboutcrush(client, message):
        buttons= [[
             InlineKeyboardButton('♥️  𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 𝐛𝐮𝐲 ♥️', url='https://youtu.be/kB9TkCs8cX0')
             ],[
             InlineKeyboardButton('🏠 𝙷𝙾𝙼𝙴 🏠', callback_data='start'),
             InlineKeyboardButton('🔐 𝙲𝙻𝙾𝚂𝙴 🔐', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
           photo=(PHOTO),
           caption=crush.CRUSH_TXT.format(message.from_user.mention),
           reply_markup=reply_markup,
        )
          

