from keyboard import add_hotkey as add_hotkey, wait as kwait, clear_all_hotkeys
from keyboard import unhook_all, on_press, read_key, unhook_all_hotkeys


def s():
    print("sex")


add_hotkey("s", s)
kwait("z")
