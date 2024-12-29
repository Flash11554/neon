from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pᴀᴜsᴇ",
            description=f"**hal hazırdaki yayımı saxlatmaq**",
            thumb_url="https://te.legra.ph/file/df8fa2868f8a277718a47.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Rᴇsᴜᴍᴇ",
            description=f"**hal hazırdaki yayımı dəvam elətdimək**",
            thumb_url="https://te.legra.ph/file/df8fa2868f8a277718a47.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Sᴋɪᴩ",
            description=f"hal hazırdaki yayımı keçid elətdirmək**",
            thumb_url="https://te.legra.ph/file/df8fa2868f8a277718a47.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="Eɴᴅ",
            description="**hal hazırdaki bitirmək**",
            thumb_url="https://te.legra.ph/file/df8fa2868f8a277718a47.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="Sʜᴜғғʟᴇ",
            description="**hal hazırdaki yayımı qarışdırmaq**",
            thumb_url="https://te.legra.ph/file/df8fa2868f8a277718a47.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Lᴏᴏᴩ",
            description="**hal hazırdaki yayımı döndərmək**",
            thumb_url="https://te.legra.ph/file/df8fa2868f8a277718a47.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
