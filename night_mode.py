# 

from Petercord_Userbot.core.decorators import ilhammansiz_on_cmd
from Petercord_Userbot import bot, Petercord_Userbot, Config
from Petercord_Userbot.helper_func.basic_helpers import edit_or_reply, get_text
from xtraPetercordUserbot.dB.nightmodedb import is_night_chat_in_db, get_all_night_chats, rm_night_chat, add_night_chat
from pyrogram.types import ChatPermissions
from Petercord_Userbot.helper_func.logger_s import LogIt
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging

@ilhammansiz_on_cmd(
    ["scgrp"],
    is_official=False,
    only_if_admin=True,
    group_only=True,
    cmd_help={
        "help": "Activate Nightmode In Group",
        "example": "{ch}scgrp",
    },
)
async def scgrp(client, message):
    pablo = await edit_or_reply(message, "`Processing...`")
    lol = await is_night_chat_in_db(message.chat.id)
    if lol:
        await pablo.edit("This Chat is Has Already Enabled Night Mode.")
        return
    await add_night_chat(message.chat.id)
    await pablo.edit(f"**Added Chat {message.chat.title} With Id {message.chat.id} To Database. This Group Will Be Closed On 12Am(IST) And Will Opened On 06Am(IST)**")


@ilhammansiz_on_cmd(
    ["rsgrp"],
    is_official=False,
    only_if_admin=True,
    group_only=True,
    cmd_help={
        "help": "Deactivate Nightmode In Group",
        "example": "{ch}rsgrp",
    },
)
async def scgrp(client, message):
    pablo = await edit_or_reply(message, "`Searching For Anime.....`")
    lol = await is_night_chat_in_db(message.chat.id)
    if not lol:
        await pablo.edit("This Chat is Has Not Enabled Night Mode.")
        return
    await rm_night_chat(message.chat.id)
    await pablo.edit(f"**Removed Chat {message.chat.title} With Id {message.chat.id} From Database. This Group Will Be No Longer Closed On 12Am(IST) And Will Opened On 06Am(IST)**")


async def job_close():
    lol = await get_all_night_chats()
    if len(lol) == 0:
        return
    for warner in lol:
        try:
            await Petercord_Userbot.send_message(
              int(warner.get("chat_id")), "`12:00 Am, Group Is Closing Till 6 Am. Night Mode Started !` \n**Powered By @ilhammansiez**"
            )
            await Petercord_Userbot.set_chat_permissions(warner.get("chat_id"), ChatPermissions())
            async for member in Friday.iter_chat_members(warner.get("chat_id")):
             if member.user.is_deleted:
                try:
                    await Petercord_Userbot.kick_chat_member(warner.get("chat_id"), member.user.id)
                except:
                    pass
        except Exception as e:
            logging.info(str(e))
            ido = warner.get("chat_id")
            try:
                await Petercord_Userbot.send_message(Config.LOG_GRP, f"[NIGHT MODE]\n\nFailed To Close The Group {ido}.\nError : {e}")
            except:
                pass


scheduler = AsyncIOScheduler(timezone="Asia/Jakarta")
scheduler.add_job(job_close, trigger="cron", hour=23, minute=55)
scheduler.start()

async def job_open():
    lol = await get_all_night_chats()
    if len(lol) == 0:
        return
    for warner in lol:
        try:
            await Petercord_Userbot.send_message(
              int(warner.get("chat_id")), "`06:00 Am, Group Is Opening.`\n**Powered By @FRidayOT**"
            )
            await Petercord_Userbot.set_chat_permissions(
                        warner.get("chat_id"),
                        ChatPermissions(
                            can_send_messages=True,
                            can_send_media_messages=True,
                            can_send_stickers=True,
                            can_send_animations=True
                         )
            )
            
        except Exception as e:
            logging.info(str(e))
            ido = warner.get("chat_id")
            try:
                await Friday.send_message(Config.LOG_GRP, f"[NIGHT MODE]\n\nFailed To Open The Group {ido}.\nError : {e}")
            except:
                pass
            

scheduler = AsyncIOScheduler(timezone="Asia/Jakarta")
scheduler.add_job(job_open, trigger="cron", hour=6, minute=10)
scheduler.start()
