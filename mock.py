from dotenv import load_dotenv
from core.telegram import Telegram
from core.Database import DB
import time
import os

SOUND_PIN_1 = 17
SOUND_PIN_2 = 27
DEVICE_LABEL = "burberry"

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')


class App:
    def __init__(self) -> None:
        db = DB()
        telegramBot = Telegram(db, TOKEN)
        telegramBot.start()

        since_last_request = time.time()
        while True:
            current_time = time.time()

            if current_time - since_last_request > 20:
                since_last_request = current_time

                telegramBot.send_notification("Hei. This is broadcast.")


App()
