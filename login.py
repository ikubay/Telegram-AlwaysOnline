# -*- coding: utf-8 -*-

from telethon import TelegramClient
from data import *
import logging
import getpass
import asyncio

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    )

if api_id == '' or api_hash == '':
    logging.fatal("You must assign a API before using this script! 在登录前你必须给定ID和HASH @ data.py")

logging.info("Trying to Login to Telegram... 正在尝试登录...")
client = TelegramClient('session_file', api_id, api_hash)

async def auth_client():
    async with client:
        await client.connect()
        auth_status = await client.is_user_authorized()
        if auth_status is True:
            logging.info("User is authorized.")
        else:
            logging.info('You have not login yet, Trying to log you in... 没有活跃的登录Session，尝试登录...')
            logging.info(
                'if you have 2FA password, please enter right now. This Password will not be stored | 如果你有两步认证密码，请现在输入。这个密码不会被保存')
            password = getpass.getpass()
            if password != '':
                client.start(password=password)
            else:
                client.start()

loop = asyncio.get_event_loop()
loop.run_until_complete(auth_client())