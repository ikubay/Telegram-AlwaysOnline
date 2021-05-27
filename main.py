# -*- coding: utf-8 -*-

import logging
from login import client
from telethon.tl.functions.account import UpdateStatusRequest
import time
from data import delay_seconds
import asyncio

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    )

async def update_status():
    async with client:
        auth_status = await client.is_user_authorized()
        if auth_status:
            logging.info("You are now authorized and will be always online.")
            while True:
                try:
                    await client(UpdateStatusRequest(offline=False))
                    logging.info("Updated online status successfully.")
                except Exception as e:
                    logging.error("Could not update online status: " + str(e))
                logging.info("Sleeping for " + str(delay_seconds) + " seconds.")
                time.sleep(delay_seconds)
        else:
            logging.fatal("Login Failed, please retry... 失败，请重试！")

loop = asyncio.get_event_loop()
loop.run_until_complete(update_status())
loop.close()