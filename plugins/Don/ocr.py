import os
import shutil
from pyrogram import Client, filters
from telegram import ChatAction,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext.dispatcher import run_async
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler,PicklePersistence
import logging
import os
from functools import wraps
import requests


API_KEY = "c48ac0c94388957"

TOKEN = "5725740361:AAFY0btKkJ5bPMk_jaap7DwJGkVX4nCTDBc"








@Client.on_message(
    filters.command("ocr") &
    f_onw_fliter
)
async def ocr(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙿𝙷𝙾𝚃𝙾 𝙾𝚁 𝚅𝙸𝙳𝙴𝙾 𝚄𝙽𝙳𝙴𝚁 𝟻𝙼𝙱.")
        return
    def convert_image(update,context):
        file_id = update.message.photo[-1].file_id
        newFile=context.bot.get_file(file_id)
        file= newFile.file_path
        context.user_data['filepath']=file
        keyboard =  [[InlineKeyboardButton("Arabic", callback_data='ara'),
                      InlineKeyboardButton("Bulgarian", callback_data='bul'),
                      InlineKeyboardButton("Chinese", callback_data='chs')
                     ],
                     [
                     InlineKeyboardButton("Croatian", callback_data='hrv'),
                     InlineKeyboardButton("Danish", callback_data='dan'),
                     InlineKeyboardButton("Dutch", callback_data='dut')
                     ],
                     [
                     InlineKeyboardButton("English", callback_data='eng'),
                     InlineKeyboardButton("Finnish", callback_data='fin'),
                     InlineKeyboardButton("French", callback_data='fre')
                     ],
                     [
                     InlineKeyboardButton("German", callback_data='ger'),
                     InlineKeyboardButton("Greek", callback_data='gre'),
                     InlineKeyboardButton("Hungarian", callback_data='hun')
                     ],
                     [
                     InlineKeyboardButton("Korean", callback_data='kor'),
                     InlineKeyboardButton("Italian", callback_data='ita'),
                     InlineKeyboardButton("Japanese", callback_data='jpn')
                     ],
                     [
                     InlineKeyboardButton("Polish", callback_data='pol'),
                     InlineKeyboardButton("Portuguese", callback_data='por'),
                     InlineKeyboardButton("Russian", callback_data='rus')
                     ],
                     [
                     InlineKeyboardButton("Spanish", callback_data='spa'),
                     InlineKeyboardButton("Swedish", callback_data='swe'),
                     InlineKeyboardButton("Turkish", callback_data='tur')
                     ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("Select the Language Here 👇", reply_markup=reply_markup)

@run_async
def button(update,context):
    filepath=context.user_data['filepath']
    query = update.callback_query
    query.answer()
    query.edit_message_text("Extracting Text....")
    data=requests.get(f"https://api.ocr.space/parse/imageurl?apikey={API_KEY}&url={filepath}&language={query.data}&detectOrientation=True&filetype=JPG&OCREngine=1&isTable=True&scale=True")
    data=data.json()
    if data['IsErroredOnProcessing']==False:
        message=data['ParsedResults'][0]['ParsedText']
        query.edit_message_text(f"{message}")
    else:
        query.edit_message_text(text="⚠️ Something went wrong")

persistence=PicklePersistence('userdata')
def main():
    token=TOKEN 
    updater = Updater(token,use_context=True,persistence=persistence)
    dp=updater.dispatcher
    dp.add_handler(MessageHandler(Filters.photo, convert_image))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling(clean=True)
    updater.idle()
 
	
if __name__=="__main__":
	main()


    



    

 

	





    

    

 



 

	





    

    















