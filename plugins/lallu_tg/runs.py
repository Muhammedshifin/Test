import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


RUN_STRINGS = (
    "ഓ.. ധിക്കാരം... പഴേപോലെ തന്നെ....ഒരു മാറ്റോമില്ല.....ചുമ്മാതല്ല ഗതി പിടിക്കാത്തത്....!!!",
    "അള്ളാ... പിള്ളേരുടെ ഓരോ... പെഷനെ...",
    "എനിക്ക് എഴുതാൻ അല്ലെ അറിയൂ സാറേ.... വായിക്കാൻ അറിയില്ലല്ലോ....",
    "ഇന്ന് ഇനി നീ മിണ്ടരുത്... ഇന്നത്തെ കോട്ട കഴിഞ്ഞ്.....",
    "ചാരമാണെന്ന് കരുതി ചെകയാൻ നിൽക്കണ്ട കനൽ കെട്ടിട്ടില്ലെങ്കിൽ പൊള്ളും.",
    "ഒറ്റ ജീവിതമേ ഉള്ളു മനസിലാക്കിക്കോ, സ്വർഗ്ഗമില്ല നരകമില്ല, 'ഒറ്റ ജീവിതം', അത് എവിടെ എങ്ങനെ വേണമെന്ന് അവനവൻ തീരുമാനിക്കും",
    "വാട്ട് എ ബോംബെസ്റ്റിക് എക്സ്പ്ലോഷൻ! സച് എ ടെറിഫിക് ഡിസ്ക്ലോസ്!!",
    "ഗോ എവേ സ്ടുപ്പിഡ് ഇൻ ദി ഹൗസ് ഓഫ് മൈ വൈഫ്‌ ആൻഡ് ഡോട്ടർ യൂവിൽ നോട്ട് സി എനി മിനിറ്റ് ഓഫ് ദി ടുഡേ... ഇറങ്ങി പോടാ..",
    "ഐ കാൻ ഡു ദാറ്റ്‌ ഡു കാൻ ഐ ദാറ്റ്‌",
    "ക്രീം ബിസ്കറ്റിൽ ക്രീം ഉണ്ടന്ന് കരുതി ടൈഗർ ബിസ്കറ്റിൽ ടൈഗർ ഉണ്ടാകണമെന്നില്ല. പണി പാളും മോനെ...",
    "പട പേടിച്ചു പന്തളത്തു ചെന്നപ്പോ പന്തോം കുത്തി പട പന്തളത്തോട്ടെന്ന് പറഞ്ഞ പോലെ ആയല്ലോ.",
    "എന്റ കർത്താവെ.... എന്നെ നീ നല്ലവനാകാൻ സമ്മതിക്കൂല്ല അല്ലെ.",
    "കാർ എൻജിൻ ഔട്ട് കംപ്ലീറ്റ്‌ലി......",
    "തള്ളെ കലിപ്പ് തീരണില്ലല്ലോ!!",
    "പാതിരാത്രിക്ക് നിന്റെ അച്ഛൻ ഉണ്ടാക്കി വെച്ചിരിക്കുന്നോ പൊറോട്ടയും ചിക്കനും....",
    "ഓ പിന്നെ നീ ഒക്കെ പ്രേമിക്കുമ്പോൾ അത് പ്രണയം.... നമ്മൾ ഒക്കെ പ്രേമിക്കുമ്പോൾ അത് കമ്പി....",
    "ദൈവമേ എന്നെ മാത്രം രക്ഷിക്കണേ....",
    "അവളെ ഓർത്ത് കുടിച്ച കള്ളും നനഞ്ഞ മഴയും വേസ്റ്റ്....",
    "ഇത്രേം കാലം എവിടെ ആയിരുന്നു....!",
    "ഇൻഗ്ലീഷ് തീരെ പിടി ഇല്ല അല്ലെ....",
    "ആൾ ദി ഡ്രീംസ്‌ ലൈക്‌ ട്വിങ്കിൽ സ്റ്റാർസ്...",
    "എന്റെ പ്രാന്തൻ മുത്തപ്പാ അവനെ ഒരു വഴിയാക്കി തരണേ",
    "പെങ്ങളെ കെട്ടിയ സ്ത്രീധന തുക തരുമോ അളിയാ",
    "നീ വല്ലാതെ ക്ഷീണിച്ചു പൊയി",
    "കണ്ണിലെണ്ണയൊഴിച്ചു കാത്തിരിക്കുവായിരുന്നളിയാ.",
    "ചെല്ലാക്കണ്ടു എന്നിച്ചു പോടാ തടി.യാ .\
    ഷട്ട് ഉഒ യുവർ മൗത് ബ്ലഡി gramavasis.",
    "പോയി ചാവട .\
    നിന്നെ കൊണ്ട് ചാവാൻ patto.",
    "നിന്നെ കൊണ്ട് നാട്ടുകാർക്കും ഗുണോല്ല്യ വിട്ടുകാർക്കും ഗുണോല്ല്യ എന്തിനാ ഇങ്ങനെ നാണം കേട്ടു ജീവിക്കുന്നട പാട് വാഴെ ചെങ്കതളി വാഴ .", 
)


@Client.on_message(
    filters.command("runs", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

        
        
PROPOSES_TRINGS = (
    "Found the reason for my smile, the day I found you. Will you let me be the reason for your smile?"
    "In you, my life becomes whole, with you my days become bright. In your hands I would love to lay, this night and for the rest of my life!"
    "You deserve the world and all the good things it has to offer. If I fail to find that world for you, I promise to give you mine!"
    "Are you Google search engine? Because you’ve got everything I’ve been searching for in life."
    "You are my North, my South, my East and West, the sun of my morning and the night to my day!"
    "I would love for you to grow old with me! The best is yet to be and it begins from the moment you say yes!"
    "I love the feeling and the butterflies I get when I see you smiling. I would love to smile for the rest of my life too. So, I say it's a yes?"
    "You are the one I wanted to find, to tell that I need you all my life, from this day on till the rest of my life."
    "Only you, you’re the only thing I’ll see forever. In my eyes, in my words, and in everything I do, your sight is the only sight that will ever bring me peace!"
    "Because every long lost road, led me to where you are; others who broke my heart, they were like northern stars, guiding me on my way, into your loving arms, this much I know is true. God bless the broken road that led me straight to you."
    "I love you just the way you are."
    "Having you by my side is what completes me, makes me and fulfils me. You complete me. So marry me and complete the circle with me!"
    "I want to be with you forever and ever. We are meant to be together."
)

@Client.on_message(
    filters.command("propose", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /propose strings """
    effective_string = random.choice(PROPOSES_TRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

