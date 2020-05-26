"""Emoji

Available Commands:

.wtf"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 14)
    input_str = event.pattern_match.group(1)
    if input_str == "wtf":
        await event.edit(input_str)
        animation_chars = [
            "What",
            "What The",
            "What The F",
            "What The Fuck",
            "What The Fuck Bruh",
            "**What The Fuck Bruh**",
            "What The Fuck Bruh",
            "**What The Fuck Bruh**",
            "What The Fuck Bruh",
            "**What The Fuck Bruh**",
            "What The Fuck Bruh",
            "**What The Fuck Bruh**",
            "What The Fuck Bruh",
            "**What The Fuck Bruh**"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i])

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 14)
    input_str = event.pattern_match.group(1)
    if input_str == "pay2":
        await event.edit(input_str)
        animation_chars = [
            "`8455015107indus@indus`👈 \n👆 Click here to Copy👆 \n\nPay on this UPI ID through Phone Pe/Google Pay",
            "`8455015107indus@indus` 👈\n 👆__Click here to Copy__ 👆\n\n**Pay** on this UPI ID through Phone Pe/Google Pay",
            "`8455015107indus@indus`👈 \n👆 Click here to Copy👆 \n\nPay on this UPI ID through Phone Pe/Google Pay",
            "`8455015107indus@indus` 👈\n 👆__Click here to Copy__ 👆\n\n**Pay** on this UPI ID through Phone Pe/Google Pay",
            "`8455015107indus@indus`👈 \n👆 Click here to Copy👆 \n\nPay on this UPI ID through Phone Pe/Google Pay",
            "`8455015107indus@indus` 👈\n 👆__Click here to Copy__ 👆\n\n**Pay** on this UPI ID through Phone Pe/Google Pay",
            "`8455015107indus@indus`👈 \n👆 Click here to Copy👆 \n\nPay on this UPI ID through Phone Pe/Google Pay",
            "`8455015107indus@indus` 👈\n 👆__Click here to Copy__ 👆\n\n**Pay** on this UPI ID through Phone Pe/Google Pay",
            "`8455015107indus@indus`👈 \n👆 Click here to Copy👆 \n\nPay on this UPI ID through Phone Pe/Google Pay",
            "`8455015107indus@indus` 👈\n 👆__Click here to Copy__ 👆\n\n**Pay** on this UPI ID through Phone Pe/Google Pay",
            "`8455015107indus@indus`👈 \n👆 Click here to Copy👆 \n\nPay on this UPI ID through Phone Pe/Google Pay",
            "`8455015107indus@indus` 👈\n 👆__Click here to Copy__ 👆\n\n**Pay** on this UPI ID through Phone Pe/Google Pay",
            "`8455015107indus@indus`👈 \n👆 Click here to Copy👆 \n\nPay on this UPI ID through Phone Pe/Google Pay",
            "`8455015107indus@indus` 👈\n 👆__Click here to Copy__ 👆\n\n**Pay** on this UPI ID through Phone Pe/Google Pay"
]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i])
