import tkinter as tk
import pyperclip
import pyautogui
import keyboard
import threading

def type_clipboard_contents():
    clipboard_contents = pyperclip.paste()
    for char in clipboard_contents:
        pyautogui.write(char, interval=0.05)

def listen_for_f8():
    keyboard.add_hotkey('f8', type_clipboard_contents)
    keyboard.wait('esc')

def create_gui():
    root = tk.Tk()
    root.title("Clipboard Typer")

    info_label = tk.Label(root, text="Press F8 to type clipboard contents. Close window or press ESC to exit.")
    info_label.pack(pady=20)

    f8_listener_thread = threading.Thread(target=listen_for_f8)
    f8_listener_thread.daemon = True
    f8_listener_thread.start()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
