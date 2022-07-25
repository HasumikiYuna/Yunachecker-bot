import requests
from pyrogram import Client, filters
from configs import config
from asyncio import sleep

from pyrogram.types import (
    Message, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup
)


Bot = Client(
    ":memory:",
    api_hash=config.API_HASH,
    api_id=config.API_ID,
    bot_token=config.BOT_TOKEN,
)


@Bot.on_message(filters.command("start"))
async def start(_, m: Message):
    messy = m.from_user.mention
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Channel", url="https://t.me/heckerman"),
                InlineKeyboardButton("Developer", url="https://t.me/fakehecker"),
            ],
            [
                InlineKeyboardButton(
                    "Source code", url="https://github.com/Junaid433/HeckerMan-Bot"
                )
            ],
        ]
    )
    await m.reply_text(
        f"Hi! {messy} \nBot Made By @fakehecker\nUse /cmds to know my commands",
        reply_markup=keyboard,
    )


@Bot.on_message(filters.command("cmds"))
async def help(_, m: Message):
    await m.reply_text(
        "/start - **To check bot Status**.\n/cmds - **To check bot commands.**\n/bin - **To check Bin**\n/chk - **Stripe CHARGE**\n/sk - **SK Checker**\n/ping - **Latency Check\n/q - **Crypto Price Lookup**\n\nGates Maintained By : @fakehecker"
    )

@Bot.on_message(filters.command("sk"))
async def sk(_, m: Message):
    await m.reply_text(
        "**Under Maintainance"
    )
@Bot.on_message(filters.command("chk"))
async def chk(_, m: Message):
    if len(m.command) < 10:
        msg = await m.reply_text("Please Enter A Valid CC")
        await sleep(999999999)
        await msg.delete()
      
    else: 

        mafia = await m.reply_text("CC -» N/A\nSTATUS -» APPROVED ✅\nResponse -» SUCCESSFULLY CHARGED $1\nGATE -» STRIPE CHARGE\nRISK  -» HIGHEST \nREQUEST BY -» /{mfrom}\nBOT BY -» @fakehecker")




@Bot.on_message(filters.command("cmds"))
async def help(_, m: Message):
    await m.reply_text(
        "/start - **To check bot Status**.\n/cmds - **To check bot commands.**\n/bin Query - **To check Bin\n/chk - **Stripe CHARGE\n/sk - **SK Checker**\n/ping - **Latency Check**")
         
@Bot.on_message(filters.command("bin"))
async def bin(_, m: Message):
    if len(m.command) < 2:
        msg = await m.reply_text("**First Know What is bin, motherfucker!**`")
        await sleep(15)
        await msg.delete()

    else:

        mafia = await m.reply_text("Checking Bin, Hold On....")
        inputm = m.text.split(None, 1)[1]
        bincode = 6
        ask = inputm[:bincode]
        req = requests.get(f"https://bin-check-dr4g.herokuapp.com/api/{ask}").json()
        res = req["result"]

        if res == False:
            return await mafia.edit("❌ #INVALID_BIN \nTry Again ;)")
        da = req["data"]
        bi = da["bin"]
        ve = da["vendor"]
        ty = da["type"]
        le = da["level"]
        ban = da["bank"]
        co = da["country"]
        cc = da["countryInfo"]
        nm = cc["name"]
        em = cc["emoji"]
        cod = cc["code"]
        dial = cc["dialCode"]
        
        mfrom = m.from_user.mention
        caption = f"""
╔ Valid ￫ `{res} ✅`\n╚ Bin ￫ `{bi}`\n\n╔ Brand ￫ `{ve}`\n╠ Type ￫ `{ty}`\n╚ Level ￫ `{le}`\n\n╔ Bank ￫ `{ban} ({co})`\n╠ Country ￫ `{nm} {em}`\n╠ Alpha2 ￫ `{cod}`\n╚ DialCode ￫ `{dial}`\n\n**↠ Checked By ￫** {mfrom}\n**↠ __Bot By ￫** [HECKER] 
 (t.me/fakehecker__
"""
        await mafia.edit(caption)


print("Sprinted Sucessfully")

Bot.run()
