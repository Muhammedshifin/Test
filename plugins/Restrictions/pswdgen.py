import random 

from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


Lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
symb =  "@#₹&%*-=()~±×÷°•´´}££¥;><"

ans = Lower_case + upper_case + num + symb

Length = 8

PASSWORD_GEN = ""join.(random.sample(ans,length))
