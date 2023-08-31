
from core.ubidots import Ubidots as Ubi
from sensors.mic import mic
from dotenv import load_dotenv
import time
import os

SOUND_PIN_1 = 27
SOUND_PIN_2 = 17
DEVICE_LABEL = "burberry"

load_dotenv()


class App:
    def __init__(self) -> None:
        Mic1 = mic(SOUND_PIN_1)
        Mic2 = mic(SOUND_PIN_2)

        while True:
            mic_result_1 = Mic1.calculate()
            mic_result_2 = Mic2.calculate()

            print("MIC 1 : ", mic_result_1)
            print("MIC 2 : ", mic_result_2)


App()
