""".admin Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.utils import admin_cmd


@borg.on(admin_cmd("join"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`━━━━━┓ \n┓┓┓┓┓┃\n┓┓┓┓┓┃　ヽ○ノ ⇦ Me When You Joined \n┓┓┓┓┓┃.     /　 \n┓┓┓┓┓┃ ノ) \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

@borg.on(admin_cmd("pay"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "UPI ID Name: __Mallidi Srinivas Reddy__\n\n`8455015107indus@indus` \n 👆Tap on this to Copy👆 \n\nPay on this UPI ID using Phone pe/Google Pay"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()    

    
@borg.on(admin_cmd("uc"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "PUBG UC Price \n \n8100 UC - Rs 3500 ($ 50) \n16000 UC - Rs 6000 ($ 80) \n24000 UC - Rs 9000 ($ 120)"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete() 
    

@borg.on(admin_cmd("method"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**The following Payment methods are accepted:** \n \nPhone Pe \nGoogle Pay \nPaytm(only KYC verified) \nBitcoins \nPayPal \nSkrill \n\nAny other method ?"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete() 
    
    
@borg.on(admin_cmd("rdp"))
async def _(event):
    if event.fwd_from:
        return
    mentions = (
        "RDP For Sale\n\n🟢 WINDOWS\n\n"

:radio_button:" 4 GB - ₹100 / $1.5\n"
:radio_button:" 8 GB - ₹200 / $3\n"
:radio_button:" 16 GB - ₹300 / $4.5\n"
:radio_button:" 32 GB - ₹400 / $6\n"
:radio_button:" 64 GB - ₹500 / $7.5 (10 Gbit speed)\n"
:radio_button:" 128 GB - ₹700 / $10 (12 Gbit speed)\n\n"
:radio_button:" Higher Configuration RDP with GPU\n      also available !!\n\n"

:white_check_mark:" ESCROW accepted\n"
:white_check_mark:" 100% Guarantee (For 1 month)\n\n"
:white_check_mark: "Payment via:\n            PayTM\n            Phone Pe\n            Google Pay\n            BTC"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete() 
   
