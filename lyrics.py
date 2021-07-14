# 
import io
import os
from tswift import Song

from Petercord_Userbot.config_var import Config
from Petercord_Userbot.core.decorators import ilhammansiz_on_cmd
from Petercord_Userbot.helper_func.basic_helpers import edit_or_reply, get_text, edit_or_send_as_file



@ilhammansiz_on_cmd(
    ["lyrics"],
    cmd_help={
        "help": "This plugin searches for song lyrics with song name",
        "example": "{ch}lyrics alone",
    }
)
async def _(client,message):
    query = get_text(message)
    lel = await edit_or_reply(message, "`Searching For Lyrics.....`")
    if not query:
        await lel.edit("`Give Me Input!`")
        return
    song = None
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "`Lyrics Not Found! Please Work On Your English!`"
    else:
        reply = "`Lyrics Not Found! Please Work On Your English!`"
    await edit_or_send_as_file(reply, lel, client, f"Result For {query}", query)
