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
    mentions = "**The following para 2 Payment methods are accepted:** \n \nPhone Pe \nGoogle Pay \nPaytm(only KYC verified) \nBitcoins \nPayPal \nSkrill \n\nAny other method ?"
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
    mentions = "🟢 RDP For Sale 🟢\n\n🟢 WINDOWS\n\n🟢 4 GB - ₹100 / $1.5\n🟢 8 GB - ₹200 / $3\n🟢 16 GB - ₹300 / $4.5\n🟢 32 GB - ₹400 / $6\n🟢 64 GB - ₹500 / $7.5 (10 Gbit speed)\n🟢 128 GB - ₹700 / $10 (12 Gbit speed)\n\n🟢 Higher Configuration RDP with GPU\n   also available !!\n\n🟢 ESCROW accepted\n🟢 100% Guarantee (For 1 month)\n\n🟢 Payment via:\n            __PayTM__\n            __Phone Pe__\n            __Google Pay__\n            __Bitcoins__\n            __PayPal__"
    
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
   
