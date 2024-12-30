import os
import shutil
import re
from bing_image_downloader import downloader
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, Message
from BrandrdXMusic import app

@app.on_message(filters.command(["imgs", "cek"], prefixes=["/", "!"]))
async def google_img_search(client: Client, message: Message):
    chat_id = message.chat.id

    try:
        query = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply("Şəkilləri hazır etmək üçün istədiyinizi yazın!")

    query = re.sub(r"[^\w\s]", "", query).strip()  # Sanitize query
    lim = re.findall(r"lim=\d+", query)
    try:
        lim = int(lim[0].replace("lim=", ""))
        query = query.replace(f"lim={lim}", "")
    except IndexError:
        lim = 5  # Default limit to 5 images

    download_dir = "downloads"

    try:
        downloader.download(query, limit=lim, output_dir=download_dir, adult_filter_off=True, force_replace=False, timeout=60)
        images_dir = os.path.join(download_dir, query)
        if not os.path.exists(images_dir) or not os.listdir(images_dir):
            raise Exception("No images were downloaded.")
        lst = [os.path.join(images_dir, img) for img in os.listdir(images_dir)][:lim]
    except Exception as e:
        return await message.reply(f"Şəkilləri göndərərkən səhv baş verdi: {e}")

    msg = await message.reply("𝔹𝕣𝕒𝕟𝕕𝕖𝕕𝕏𝕄𝕒𝕟𝕒𝕘𝕖𝕞𝕖𝕟𝕥 Scrapping images...")

    for i, img in enumerate(lst, start=1):
        await msg.edit(f"=> Effect şəkilləri hazırlayır {i}/{lim}")

    try:
        media = [InputMediaPhoto(media=img) for img in lst]
        await app.send_media_group(chat_id=chat_id, media=media, reply_to_message_id=message.id)
    except Exception as e:
        return await message.reply(f"Şəkilləri göndərərkən səhv baş verdi: {e}")
    finally:
        if os.path.exists(images_dir):
            shutil.rmtree(images_dir)
        await msg.delete()
