from pynput.keyboard import Key, Listener
import time, sys

def on_press(key):
    print(f"Press: {key.char if hasattr(key, 'char') else key.name}")

def on_release(key):
 print(f"release: {key.char if hasattr(key, 'char') else key.name}")


def main(duration):
    global listener
    listener = Listener(on_press=on_press, on_release=on_release)
    print("Test Start")
    listener.start()
    time.sleep(5)
    listener.stop()
    print("Test End")


if __name__ == '__main__':
    timer = int(sys.argv[1])
    main(timer)
