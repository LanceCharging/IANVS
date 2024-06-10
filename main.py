from IANVS_setting import *
from hide_show import *
from keyboard import add_hotkey


def main():

    current_face = "L"
    previous_styles = {}  # 숨김 목록 -> 핸들 : 기존 상태

    hot_keys = hot_key_dict()

    print(hot_keys)

    add_hotkey(hot_keys["SHAKING_UP_RIGHT"], lambda: print("right"))
    add_hotkey(hot_keys["SHAKING_UP_LEFT"], lambda: print("left"))
    add_hotkey(hot_keys["SUMMON_IANVS"], lambda: print("summon"))

    while True:
        pass


if __name__ == "__main__":
    main()
