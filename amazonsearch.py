# 
import requests
from Petercord_Userbot.core.decorators import ilhammansiz_on_cmd
from Petercord_Userbot.helper_func.basic_helpers import edit_or_reply, get_text


@ilhammansiz_on_cmd(
    ["amsearch"],
    cmd_help={
        "help": "Search Products From Amazon!",
        "example": "{ch}amsearch Iphone",
    }
)

async def _am_search_by_lackhac(client,message):
    query = get_text(message)
    msg_ = await edit_or_reply(message, "`Searching Product!`")
    if not query:
        await msg_.edit("`Please, Give Input!`")
        return
    product = ""
    r = requests.get(f"https://amznsearch.vercel.app/api/?query={query}").json()
    for products in r:
        link = products['productLink']
        name = products['productName']
        price= products['productPrice']
        product += f"<a href='{link}'>• {name}\n{price}</a>\n"
    await msg_.edit(product, parse_mode="HTML")
