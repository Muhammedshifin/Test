"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "ചത്തിട്ടില്ല മുത്തേ ഇവിടെ തന്നെ ഉണ്ട്.. നിനക്ക് ഇപ്പൊ എന്നോട് ഒരു സ്നേഹവും ഇല്ല. കൊള്ളാം.. നീ പാഴെ പോലെയേ അല്ല മാറിപോയി..😔 ഇടക്ക് എങ്കിലും ചുമ്മാ ഒന്ന് /start ചെയ്തു നോക്ക്..🙂" 
REPO = "ആകാശത്തു നോക്കി ഇരുന്നോ ഇപ്പൊ വരും ☺️"
CHANNEL = "<b>𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻</b> ›› https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA\n\n<b>𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ›› https://t.me/OpusTechz</b>\n\n<b>𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ›› https://t.me/MWUpdatez</b>"
AJAX = "<b>𝙱𝙾𝚃 ›› https://t.me/Elsaa_MsT_bot</b>"
MYRE = "പോടാ മൈരേ പൊലയാടി മോനെ"
PURE = "പൂമാനം"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("ajax", COMMAND_HAND_LER) & f_onw_fliter)
async def ajax(_, message):
    await message.reply_text(AJAX)
    
    
@Client.on_message(filters.command("myre", COMMAND_HAND_LER) & f_onw_fliter)
async def myre(_, message):
    await message.reply_text(MYRE)
    
    
@Client.on_message(filters.command("pure", COMMAND_HAND_LER) & f_onw_fliter)
async def pure(_, message):
    await message.reply_text(PURE)
   

@Client.on_message(filters.command("ikka", COMMAND_HAND_LER) & f_onw_fliter)
async def ikka(_, message):
    await message.reply_sticker(
        sticker="CAACAgUAAxkBAAJocmNfp7_K_XweKlB5zhPQ5Dh_Dy__AAL_AwACddYwVK1NaogVUwOJHgQ"
    )
    
@Client.on_message(filters.command("dogs", COMMAND_HAND_LER) & f_onw_fliter)
async def dog(_, message):
    await message.reply_sticker(
        sticker="CAACAgUAAxkBAAJsR2NhBAx7HMFYJcsAAQcrJGLVI0mzSAACLQoAAhv-GFU4KAPM8AJJGx4E"
    )
    

@Client.on_message(filters.command("sunny", COMMAND_HAND_LER) & f_onw_fliter)
async def sunny(_, message):
    await message.reply_sticker(
        sticker="CAACAgEAAxkBAAJsSmNhBdv6S1sjxd1aisw1dEaxoTMBAALfAgACa5ahRXcu73ZIf8_iHgQ"
    )
        
   









