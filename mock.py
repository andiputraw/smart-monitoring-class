from dotenv import load_dotenv
from core.telegram import Telegram
from core.Database import DB
from core.ubidots import Ubidots
import time
import os
import random

SOUND_PIN_1 = 17
SOUND_PIN_2 = 27
DEVICE_LABEL = "smart-class-monitoring-system"

SENSOR_LABEL_1 = 'mic-1-17'
SENSOR_LABEL_2 = 'mic-2-27'

load_dotenv()

TOKEN = os.getenv('UBIDOTS_TOKEN')


class App:
    def __init__(self) -> None:
        ubidots = Ubidots(DEVICE_LABEL, TOKEN)
        loop_count = 0

        while loop_count != 100:
            current_time = time.time()

            if loop_count > 10 and loop_count < 30:
                print(
                    f"MIC 1: {self.random_from_0_80()}, MIC 2: {self.random_from_0_80()}")
            else:
                print(f"MIC 1: 0, MIC 2: 0")
            # print(mic_2_result, mic_1_result)
            # ubidots.request({SENSOR_LABEL_1: mic_1_result,
            #                 SENSOR_LABEL_2: mic_2_result}, current_time)
            loop_count += 1
            time.sleep(0.1)

    def random_from_0_80(self):
        chance = random.random() * 1000
        if chance > 950:
            return random.randrange(60, 80)
        elif chance > 600:
            return random.randrange(30, 60)
        elif chance > 300:
            return random.randrange(20, 25)
        else:
            return random.randrange(0, 20)


App()
