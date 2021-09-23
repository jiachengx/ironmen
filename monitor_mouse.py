# mouse monitoring within the duration timer
from pynput.mouse import Listener
import time

def moveTo(x, y):
 print(f"moveTo: ({x}, {y})")


def click(x, y, button, is_press):
 print(f"Mouse button: {button} in ({x}, {y}) {'press' if is_press else 'release'}")


def scroll(x1, y1, x2, y2):
 if x2:
  print(f"scroll from ({x1}, {y1}) into { 'right' if x2 > 0 else 'left'}")
 else:
  print(f"scroll from ({x1}, {y1}) into { 'buttom' if y2 > 0 else 'upper'}")

def main(duration):
    listener = Listener(
    on_move=moveTo,
    on_click=click,
    on_scroll=scroll)
    print("Test Start")
    listener.start()
    time.sleep(duration)
    listener.stop()
    print("Test Finish")


if __name__ == '__main__':
    main(5)
    
