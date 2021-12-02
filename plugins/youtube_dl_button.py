import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import asyncio
import json
import os
import shutil
import time

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from datetime import datetime
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from pyrogram.types import InputMediaPhoto

from translation import Translation
from helper_funcs.help_Nekmo_ffmpeg import generate_screen_shots
from helper_funcs.display_progress import progress_for_pyrogram, humanbytes
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image


async def youtube_dl_call_back(bot, update):
    

            )
        else:
            if Config.SCREENSHOTS:
                is_w_f = False
                images = await generate_screen_shots(
                    download_directory,
                    tmp_directory_for_each_user,
                    is_w_f,
                    Config.DEF_WATER_MARK_FILE,
                    300,
                    9
                )
            try:
                await bot.edit_message_text(text=Translation.UPLOAD_START, chat_id=update.message.chat.id, message_id=update.message.message_id)
            except:
                pass
            # get the correct width, height, and duration for videos greater than 10MB
            width = 0
            height = 0
            duration = 0
            if tg_send_type != "file":
                metadata = extractMetadata(createParser(download_directory))
                if metadata is not None:
                    if metadata.has("duration"):
                        duration = metadata.get('duration').seconds

            if os.path.exists(thumb_image_path):
                width = 0
                height = 0
                metadata = extractMetadata(createParser(thumb_image_path))
                if metadata.has("width"):
                    width = metadata.get("width")
                if metadata.has("height"):
                    height = metadata.get("height")
                if tg_send_type == "vm":
                    height = width
                Image.open(thumb_image_path).convert(
                    "RGB").save(thumb_image_path)
                img = Image.open(thumb_image_path)
                if tg_send_type == "file":
                    img.resize((320, height))
                else:
                    img.resize((90, height))
                img.save(thumb_image_path, "JPEG")
            else:
                thumb_image_path = None

            start_time = time.time()
            if tg_send_type == "audio":
                await update.message.reply_to_message.reply_chat_action("upload_audio")
                await bot.send_audio(
                    chat_id=update.message.chat.id,
                    audio=download_directory,
                    caption=description,
                    parse_mode="HTML",
                    duration=duration,
                    # performer=response_json["uploader"],
                    # title=response_json["title"],
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/All_Movie_Rocker')]]),
                    thumb=thumb_image_path,
                    progress=progress_for_pyrogram,
                    progress_args=(
                        Translation.UPLOAD_START,
                        update.message,
                        start_time
                    )
                )
            elif tg_send_type == "file":
                await update.message.reply_to_message.reply_chat_action("upload_document")
                await bot.send_document(
                    chat_id=update.message.chat.id,
                    document=download_directory,
                    thumb=thumb_image_path,
                    caption=description,
                    parse_mode="HTML",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/All_Movie_Rocker')]]),
                    reply_to_message_id=update.message.reply_to_message.message_id,
                    progress=progress_for_pyrogram,
                    progress_args=(
                        Translation.UPLOAD_START,
                        update.message,
                        start_time
                    )
                )
            elif tg_send_type == "vm":
                await update.message.reply_to_message.reply_chat_action("upload_video_note")
                
                await bot.send_video_note(
                    chat_id=update.message.chat.id,
                    video_note=download_directory,
                    duration=duration,
                    length=width,
                    thumb=thumb_image_path,
                    reply_to_message_id=update.message.reply_to_message.message_id,
                    progress=progress_for_pyrogram,
                    progress_args=(
                        Translation.UPLOAD_START,
                        update.message,
                        start_time
                    )
                )
            elif tg_send_type == "video":
                await update.message.reply_to_message.reply_chat_action("upload_video")
                await bot.send_video(
                    chat_id=update.message.chat.id,
                    video=download_directory,
                    caption=description,
                    parse_mode="HTML",
                    duration=duration,
                    width=width,
                    height=height,
                    supports_streaming=True,
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/All_Movie_Rocker')]]),
                    thumb=thumb_image_path,
                    reply_to_message_id=update.message.reply_to_message.message_id,
                    progress=progress_for_pyrogram,
                    progress_args=(
                        Translation.UPLOAD_START,
                        update.message,
                        start_time
                    )
                )
            else:
                logger.info("Did this happen? :\\")
            end_two = datetime.now()
            time_taken_for_upload = (end_two - end_one).seconds

            media_album_p = []
            if Config.SCREENSHOTS:
                if images is not None:
                    i = 0
                    caption = ""
                    if is_w_f:
                        caption = ""
                    for image in images:
                        if os.path.exists(image):
                            if i == 0:
                                media_album_p.append(
                                    InputMediaPhoto(
                                        media=image,
                                        caption=caption,
                                        parse_mode="html"
                                    )
                                )
                            else:
                                media_album_p.append(
                                    InputMediaPhoto(
                                        media=image
                                    )
                                )
                            i = i + 1
                    await bot.send_media_group(
                        chat_id=update.message.chat.id,
                        disable_notification=True,
                        reply_to_message_id=update.message.message_id,
                        media=media_album_p
                    )
            try:
                shutil.rmtree(tmp_directory_for_each_user)   
            except:
                pass
            try:
                os.remove(thumb_image_path)
            except:
                pass
            await bot.edit_message_text(
                text=Translation.AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS.format(time_taken_for_download, time_taken_for_upload),
                chat_id=update.message.chat.id,
                message_id=update.message.message_id,
                disable_web_page_preview=True
            )
