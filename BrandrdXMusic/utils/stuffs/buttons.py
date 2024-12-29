from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("**ChatGPT**", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("**İstifadəçi Tarixi**", callback_data="mplus HELP_History"),InlineKeyboardButton("**Relslər**", callback_data="mplus HELP_Reel")],
    [InlineKeyboardButton("**Tag-etme**", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("**Info**", callback_data="mplus HELP_Info"),InlineKeyboardButton("**Fotonu-Linkə**", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("**Cütlüklər**", callback_data="mplus HELP_Couples"),
    InlineKeyboardButton("**Funksiyaları**", callback_data="mplus HELP_Action"),InlineKeyboardButton("**Axtarış**", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("**Font", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("**Qrupdaki Botlar**", callback_data="mplus HELP_Bots"),InlineKeyboardButton("**Telegraf**", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("**Bot**", callback_data="mplus HELP_Source"),
    InlineKeyboardButton("**Doğru-Cəsarət**", callback_data="mplus HELP_TD"),InlineKeyboardButton("**Suallar**", callback_data="mplus HELP_Quiz")], 
    [InlineKeyboardButton("**Mətni-sesə**", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("**Radio**", callback_data="mplus HELP_Radio"),InlineKeyboardButton("**Ses-vermə**", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("◁", callback_data=f"settings_back_helper"),
     InlineKeyboardButton("↻ Geri ↻", callback_data=f"mbot_cb"), 
    InlineKeyboardButton("▷", callback_data=f"managebot123 settings_back_helper"),
    ]]
