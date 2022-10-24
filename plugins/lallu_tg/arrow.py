# codes added by @lallu_tg
# use with proper credits

from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# EMOJI CONSTANTS
DART_E_MOJI = "https://telegra.ph/file/9a33ba9ab6b3b3352e276.jpg"
# EMOJI CONSTANTS


@Client.on_message(
    filters.command(["throw", "dart"], COMMAND_HAND_LER) &
    f_onw_fliter
)
async def throw_dart(client, message):
    """ /throw an @AnimatedDart """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DART_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

