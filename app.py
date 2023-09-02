
from core.ubidots import Ubidots as Ubi
from core.telegram import Telegram
from core.Database import DB
from sensors.mic import mic
from dotenv import load_dotenv
import time
import os

SOUND_PIN_1 = 17
SOUND_PIN_2 = 27
DEVICE_LABEL = "burberry"

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
UBIDOTS = os.getenv('UBIDOTS_TOKEN')


def INFORMATION_BROADCAST(mic_1, mic_2):
    return f"""
    INFO: Kondisi kelas sekarang bising
    Mic 1 : {mic_1},
    Mic 2 : {mic_2}
    """


class App:
    def __init__(self) -> None:
        Mic1 = mic(SOUND_PIN_1)
        Mic2 = mic(SOUND_PIN_2)
        db = DB()
        TelegramBot = Telegram(db, TOKEN)
        TelegramBot.start()
        ubi = Ubi(DEVICE_LABEL, UBIDOTS)

        while True:
            current_time = time.time()
            mic_result_1 = Mic1.calculate()
            mic_result_2 = Mic2.calculate()

            if mic_result_1 >= 400 or mic_result_2 >= 400:
                db.insert_logs(mic_result_1, SOUND_PIN_1,
                               mic_result_2, SOUND_PIN_2)
                TelegramBot.send_notification(
                    INFORMATION_BROADCAST(mic_result_1, mic_result_2))
            ubi.request(
                {"MIC 1": mic_result_1, "MIC 2": mic_result_2}, current_time)


App()
