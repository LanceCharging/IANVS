from os import environ
from os.path import dirname, abspath

from dotenv import set_key, load_dotenv, unset_key

from keyboard import unhook_all, on_press

from tkinter import Tk, Label

IANVS_dirrectory = dirname(abspath(__file__))

env_path = IANVS_dirrectory + "/.env"
initial_env_path = IANVS_dirrectory + "/initial_env.txt"

left_face_path = IANVS_dirrectory + "/faces/left_face.txt"
right_face_path = IANVS_dirrectory + "/faces/right_face.txt"

load_dotenv(env_path)


def env_update(key, value, env_path=env_path, mod="set"):
    if mod == "set":
        set_key(env_path, key, value)
    elif mod == "unset":
        unset_key(env_path, key)
    load_dotenv(env_path, override=True)


def env_search(key):
    return environ.get(key)


def initialize_env():
    with open(initial_env_path, "r") as file:
        initial_value = file.read()

    with open(env_path, "w") as file:
        file.write(initial_value)

    load_dotenv(env_path, override=True)


def update_initial_env():
    pass


# ----------------------------------


def hot_key_dict():
    return {
        "SHAKING_UP_RIGHT": env_search("SHAKING_UP_RIGHT"),
        "SHAKING_UP_LEFT": env_search("SHAKING_UP_LEFT"),
        "SUMMON_IANVS": env_search("SUMMON_IANVS"),
    }


def update_hot_key_0(witch_hot_key):

    hot_key_ui = Tk()
    hot_key_ui.overrideredirect(True)
    hot_key_ui.attributes("-topmost", True)

    screen_width = hot_key_ui.winfo_screenwidth()
    screen_height = hot_key_ui.winfo_screenheight()

    hot_key_ui.geometry(f"{screen_width}x100+{0}+{screen_height//2 - 50}")

    label = Label(hot_key_ui, text="단축키 재할당 : " + witch_hot_key)
    label.pack()

    keys_label = Label(hot_key_ui, text="Pressed Keys:")
    keys_label.pack()

    def update_hot_key():
        keys = []

        def on_key_press(event, keys=keys):
            if event.name == "enter" and len(keys) > 0:
                unhook_all()
                env_update(witch_hot_key, value="+".join(keys), mod="set")
                # update_initial_env()
                hot_key_ui.destroy()
            elif event.name == "backspace" and len(keys) > 0:
                keys.pop()
            elif event.name == "enter" or event.name == "backspace":
                pass
            elif len(keys) < 5:
                keys.append(event.name)

            keys_label.config(text="Pressed Keys:" + " ".join(keys))

        on_press(on_key_press)

    hot_key_ui.after(300, update_hot_key)
    hot_key_ui.mainloop()
