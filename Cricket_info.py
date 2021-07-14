# 


import urllib.request
from Petercord_Userbot.helper_func.basic_helpers import edit_or_reply, get_text
from bs4 import BeautifulSoup
from pyrogram import filters
from Petercord_Userbot.core.decorators import ilhammansiz_on_cmd


@ilhammansiz_on_cmd(
    ["cs"],
    cmd_help={
        "help": "Get live cricket score info",
        "example": "{ch}cs",
    },
)
async def _(client, message):
    score_page = "http://static.cricinfo.com/rss/livescores.xml"
    page = urllib.request.urlopen(score_page)
    soup = BeautifulSoup(page, "html.parser")
    result = soup.find_all("description")
    Sed = ""
    for match in result:
        Sed += match.get_text() + "\n\n"
    await edit_or_reply(
        message,
        f"<b><u>Match information gathered successful</b></u>\n\n\n<code>{Sed}</code>",
        parse_mode="html",
    )

