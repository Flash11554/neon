import asyncio
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from BrandrdXMusic import app
from BrandrdXMusic.utils.branded_ban import admin_filter

SPAM_CHATS = {}
lock = asyncio.Lock()  # Lock for thread-safe updates to SPAM_CHATS

@app.on_message(
    filters.command(["utag", "uall"], prefixes=["/", "@", ".", "#"]) & admin_filter
)
async def tag_all_users(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id

    if len(message.text.split()) == 1:
        await message.reply_text(
            "**Provide some text to tag all, like »** `@utag Hi Friends`"
        )
        return

    text = message.text.split(None, 1)[1]
    await message.reply_text(
        "**Tagging started successfully!**\n\n"
        f"**Tagging every user with a delay of 7 seconds.**\n\n"
        f"**Stop tagging using » /stoputag**"
    )

    async with lock:
        SPAM_CHATS[chat_id] = True  # Start tagging

    while True:
        async with lock:
            if not SPAM_CHATS.get(chat_id):
                await message.reply_text("**Tagging stopped successfully.**")
                break

        usernum = 0
        usertxt = ""
        try:
            async for m in app.get_chat_members(chat_id):
                if m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})"
                if usernum == 5:
                    await app.send_message(chat_id, f"{text}\n{usertxt}")
                    usernum = 0
                    usertxt = ""
                    await asyncio.sleep(7)
        except Exception as e:
            print(f"Error: {e}")
            break


@app.on_message(
    filters.command(
        ["stoputag", "stopuall", "offutag", "offuall", "utagoff", "ualloff"],
        prefixes=["/", ".", "@", "#"],
    )
    & admin_filter
)
async def stop_tagging(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id

    async with lock:
        if SPAM_CHATS.get(chat_id, False):
            SPAM_CHATS[chat_id] = False
            await message.reply_text("**Stopping the tagging process...**")
        else:
            await message.reply_text("**No tagging process is currently active.**")
