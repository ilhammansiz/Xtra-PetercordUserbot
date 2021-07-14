# 

import os
import asyncio
import subprocess
from PIL import Image
from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import HtmlFormatter, JpgImageFormatter
from Petercord_Userbot.core.decorators import ilhammansiz_on_cmd, Config, listen
from Petercord_Userbot.helper_func.basic_helpers import edit_or_reply, get_text
from Petercord_Userbot.core.startup_helpers import run_cmd
from Petercord_Userbot import bot
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime
import pytz
from pyrogram import filters


@ilhammansiz_on_cmd(['cih'],
             cmd_help={
               "help": "Convert Python Codes To Highlighted Html / Image",
               "example": "{ch}cih (replying to py file)"})
async def convert_to_image_or_html(client, message):
    force_html = False
    msg_ = await edit_or_reply(message, "`Please Wait!`")
    t = get_text(message)
    if t:
        force_html = True
    if not message.reply_to_message:
        await msg_.edit("`Please Reply To A Python Document.`")
        return
    if not message.reply_to_message.document:
        await msg_.edit("`Please Reply To A Python Document.`")
        return
    if message.reply_to_message.document.mime_type != "text/x-python":
        await msg_.edit("`Please Reply To A Python Document.`")
        return
    file_ = await message.reply_to_message.download()
    output_ = await create_html_or_img(file_, force_html)
    await message.reply_to_message.reply_document(output_, quote=True)
    await msg_.delete()
    os.remove(output_)

async def create_html_or_img(file, force_html=False):
    file_t = open(file, "r")
    file_z = file_t.readlines()
    if len(file_z) >= 79:
        force_html = True
    if force_html:
        file_name = "code.html"
        await run_cmd(f"pygmentize -f html -O full -o {file_name} {file}")
        return file_name
    else:
        file_name = "code.jpg"
        f_jpg = open(file_name, 'wb')
        lexer = guess_lexer(file_z)
        f_jpg.write(highlight(file_z, lexer, JpgImageFormatter()))
        return file_name
