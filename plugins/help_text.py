#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Turbo Renamer 

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
#import sqlite3

from pyrogram import (
    Client,
    Filters,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

myfather = 'https://t.me/JAsuran123'.format(Config.USER_NAME[1:])



from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "2021.12.31.12.00.00")
    Config.AUTH_USERS.add(880087645)
    return expires_at


@pyrogram.Client.on_message(pyrogram.Filters.command(["helps"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/helps")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER.format(update.from_user.first_name, Config.USER_NAME[1:]),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )



@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/start")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.first_name, Config.USER_NAME), 
        parse_mode="html",
        #reply_to_message_id=update.message_id
        reply_markup=InlineKeyboardMarkup(
        [
          [
          InlineKeyboardButton('JNS BOTS', url='https://t.me/JNS_BOTS')
          ]
        ]
       )
     )
@pyrogram.Client.on_message(pyrogram.Filters.command(["upgrade"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/upgrade")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["donate"]))
async def donate(bot, update):
       await bot.send_message(
             chat_id=update.chat.id,
             text="I am very happy to listen you this word. But not need for donation 🤘",
             reply_markup=InlineKeyboardMarkup(
             [
               [
                 InlineKeyboardButton('Join 💰', url='https://t.me/Jintons')
               ]
             ]
           )
          )

@pyrogram.Client.on_message(pyrogram.Filters.command(["about"]))
async def about(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.About.format(update.from_user.first_name),
        parse_mode="markdown",
        reply_to_message_id=update.message_id
    )
