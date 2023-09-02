from datetime import datetime
from telepot import Bot
from telepot.loop import MessageLoop
from core.Database import DB
import os
import time

EACH_REQUEST_DELAY = 40


class Telegram:

    bot: Bot
    db: DB
    token: str
    last_request_time: time

    def __init__(self, db: DB, token) -> None:
        self.token = token
        self.bot = Bot(self.token)
        self.db = DB()
        self.last_request_time = 0

    def send_notification(self, message: str, current_time: time):

        if current_time - self.last_request_time > EACH_REQUEST_DELAY:
            self.last_request_time = current_time
            return

        chats = self.db.get_chat()
        for chat in chats:
            self.bot.sendMessage(chat_id=chat["chat_id"], text=message)

    def start(self):
        print("[INFO]: Bot is starting")

        def _handle(message):
            print("[INFO]: Sending message to all registered user ")
            msg = message['text']
            id = message['from']['id']

            if msg == '/ping':
                self.bot.sendMessage(chat_id=id, text="Pong")
            elif msg == '/daftar':
                self.db.insert_chat(id)
                self.bot.sendMessage(chat_id=id, text="Success")
            else:
                self.bot.sendMessage(
                    chat_id=id, text="Error: Command is not supported")

        MessageLoop(self.bot, _handle).run_as_thread()
