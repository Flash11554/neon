from BrandrdXMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [   "🌙 𝗚𝗲𝗰ə𝗻𝗶𝘇 𝘅𝗲𝘆𝗶𝗿.𝗨𝗹𝗱𝘂𝘇𝗹𝗮𝗿 𝘀𝗶𝘇𝗶𝗻 üçü𝗻 𝗽𝗮𝗿𝗹𝗮𝘀ı𝗻, 𝘆𝘂𝘅𝘂𝗹𝗮𝗿ı𝗻ı𝘇 𝗴ö𝘇ə𝗹 𝗼𝗹𝘀𝘂𝗻! 🌟✨",
"🌌 𝗚𝗲𝗰ə𝗻𝗶𝘇 𝘅𝗲𝘆𝗶𝗿.𝗛ə𝗿 𝗯𝗶𝗿 𝗮𝗿𝘇𝘂 𝘀𝗮𝗯𝗮𝗵 𝗴𝗲𝗿çə𝗸 𝗼𝗹𝗺𝗮𝗾 üçü𝗻 𝘆𝘂𝘅𝘂𝗻𝘂𝘇𝗱𝗮 𝘀𝗶𝘇ə 𝗶𝗹𝗵𝗮𝗺 𝗴ə𝘁𝗶𝗿𝘀𝗶𝗻! 💭🌙",
"🌠 𝗚𝗲𝗰ə𝗻𝗶𝘇 𝘅𝗲𝘆𝗶𝗿.𝗦𝗮𝗸𝗶𝘁 𝘃ə 𝗿𝗮𝗵𝗮𝘁 𝗯𝗶𝗿 𝗴𝗲𝗰ə 𝗱𝗶𝗹ə𝘆𝗶𝗿ə𝗺! 𝗦𝗮𝗯𝗮𝗵 𝘆𝗲𝗻𝗶 𝘂ğ𝘂𝗿𝗹𝗮𝗿𝗹𝗮 𝗼𝘆𝗮𝗻ı𝗻! 🌺✨",
"🛏️ 𝗚𝗲𝗰ə𝗻𝗶𝘇 𝘅𝗲𝘆𝗶𝗿.𝗚ö𝘇ə𝗹 𝘅ə𝘆𝗮𝗹𝗹𝗮𝗿𝗹𝗮 𝗱𝗼𝗹𝘂 𝗱𝗶𝗻𝗰 𝗯𝗶𝗿 𝘆𝘂𝘅𝘂 𝘀𝗶𝘇𝗶𝗻𝗹ə 𝗼𝗹𝘀𝘂𝗻! 💤🌙",
"⭐ 𝗚𝗲𝗰ə𝗻𝗶𝘇 𝘅𝗲𝘆𝗶𝗿.𝗨𝗹𝗱𝘂𝘇𝗹𝗮𝗿 𝘀𝗶𝘇ə ə𝗻 𝗴ö𝘇ə𝗹 𝗻𝗮ğı𝗹𝗹𝗮𝗿ı 𝗱𝗮𝗻ış𝘀ı𝗻, 𝘀𝗮𝗯𝗮𝗵 𝗺ö𝗵𝘁əşə𝗺 𝗯𝗶𝗿 𝗴ü𝗻 𝗼𝗹𝘀𝘂𝗻! 🌟💫",
"🌛 𝗚𝗲𝗰ə𝗻𝗶𝘇 𝘅𝗲𝘆𝗶𝗿.𝗛ü𝘇𝘂𝗿𝗹𝘂 𝗯𝗶𝗿 𝗴𝗲𝗰ə, 𝗽𝗮𝗿𝗹𝗮𝗾 𝗯𝗶𝗿 𝘀𝗮𝗯𝗮𝗵 𝗱𝗶𝗹ə𝘆𝗶𝗿ə𝗺! 𝗬𝗮𝘅şı 𝗶𝘀𝘁𝗶𝗿𝗮𝗵ə𝘁 𝗲𝗱𝗶𝗻! 💕🌙",
"🕊️ 𝗚𝗲𝗰ə𝗻𝗶𝘇 𝘅𝗲𝘆𝗶𝗿.𝗦𝗮𝗸𝗶𝘁𝗹𝗶𝗸 𝘃ə 𝗿𝗮𝗵𝗮𝘁𝗹ı𝗾 𝘀𝗶𝘇𝗶𝗻𝗹ə 𝗼𝗹𝘀𝘂𝗻! 𝗦𝗮𝗯𝗮𝗵ı𝗻ı𝘇 𝘆𝗲𝗻𝗶 𝗳ü𝗿𝘀ə𝘁𝗹ə𝗿𝗹ə 𝗱𝗼𝗹𝘀𝘂𝗻! 🌿🌟",
           ]


@app.on_message(filters.command(["grtag", "tagmember" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ Bu komanda ancaq qruplar üçündür")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ Siz admin deyilsiniz,ancaq adminlər tag edə bilər ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall Gᴇᴄəɴɪᴢ Xᴇʏʀə Bᴇʟə ʏᴀᴢıɴ /Nöᴠʙəᴛɪ ᴅəғə ɪsᴛəɴɪʟəɴ ᴍᴇsᴀJᴀ ᴄᴀᴠᴀʙ ᴠᴇʀɪɴ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagallil ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏᴛ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("/tagalllil ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    if chat_id in spam_chats:
        return await message.reply("๏ Ilk olaraq tag etme prosesini başlatın...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += "<a href='tg://user?id={}'>{}</a>".format(usr.user.id, usr.user.first_name)

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["grtag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ Bu komanda ancaq qruplar üçündür")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ Siz admin deyilsiniz,ancaq adminlər tag edə bilər ")
    if chat_id in spam_chats:
        return await message.reply("๏ Ilk olaraq tag etme prosesini başlatın...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += "<a href='tg://user?id={}'>{}</a>".format(usr.user.id, usr.user.first_name)

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["grstop", "cancel"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("Hal hazırda qrupda tag prosesi başladılmayıb")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("Siz admin deyilsiniz,ancaq adminlər tag edə bilər")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("𝗧𝗔𝗚 𝗘𝗧𝗠𝗘 𝗣𝗥𝗢𝗦𝗘𝗦𝗜 𝗗𝗔𝗬𝗔𝗡𝗗𝗜𝗥𝗜𝗟𝗗𝗜")
