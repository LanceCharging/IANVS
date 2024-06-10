from IANVS_setting import *
from hide_show import *
from shaking_up import *
from keyboard import add_hotkey


def main():

    previous_styles = {}  # 숨김 목록 -> 핸들 : 기존 상태
    current_face = ["L"]
    left_face = []
    right_face = []

    hot_keys = hot_key_dict()

    print(hot_keys)

    add_hotkey(
        hot_keys["SHAKING_UP_RIGHT"],
        lambda: (
            shaking_right_face_up(
                previous_styles, current_face, left_face, right_face, mod="1"
            )
            if current_face[0] == "L"
            else None
        ),
    )
    add_hotkey(
        "q+w+d",
        lambda: (
            shaking_left_face_up(
                previous_styles, current_face, left_face, right_face, mod="1"
            )
            if current_face[0] == "R"
            else None
        ),
    )
    add_hotkey(
        hot_keys["SUMMON_IANVS"],
        lambda: print(
            "previous_styles :",
            previous_styles,
            current_face[0],
            "left_face :",
            left_face,
            "right_face",
            right_face,
            sep="\n",
        ),
    )
    """
    while True:
        pass
    """
    from keyboard import wait as kwait

    kwait("esc")


if __name__ == "__main__":
    main()
