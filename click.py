import threading
import time

from pynput import keyboard
from pynput.mouse import Button, Controller

mouse = Controller()
clicking = False


class Clicker:
    def __init__(self, buttom, time_sleep, hot_key):
        self.buttom = buttom
        self.time_sleep = time_sleep
        self.hot_key = hot_key
        self.clicking = False
        self.listener = None

    def start(self):
        print('начался старт программы')
        button_map = {
            'right click': Button.right,
            'left click': Button.left,
        }
        hot_key_map = {
            'space': keyboard.Key.space,
            'ctrl': keyboard.Key.ctrl,
        }
        self.buttom = button_map[self.buttom]
        self.hot_key = hot_key_map[self.hot_key]

        def on_press(key):
            if key == self.hot_key:
                self.clicking = not self.clicking

        def clicker():
            while True:
                if self.clicking:
                    mouse.click(self.buttom)
                    time.sleep(self.time_sleep)

        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()
        threading.Thread(target=clicker).start()

    def stop(self):
        if self.listener is not None:
            self.listener.stop()
