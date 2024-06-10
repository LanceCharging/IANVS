from hide_show import *


def shaking_right_face_up(
    previous_styles,
    current_face,
    left_face,
    right_face,
    mod="1",
):
    if current_face[0] == "R":
        return None  # 반환값을 명시하지 않은 함수랑 return None은 둘 다 None을 반환한다
    current_face[0] = "R"

    if mod == "1":
        print("shaking_right_face_up")
        left_face.clear()
        """
        리스트 같은 가변 객체는 함수 밖에서 선언되었다 하더라도, 함수 안에서 '수정'할 수 있다는 점을 이용하고 싶은데(인자로 받든 직접 하든),

        내용물을 비우는 과정을 left_face = [] 이딴 식으로 하면 left의 해당 객체 참조가 풀려버리니까 이렇게.

        전역변수 쓰기 매우 싫음
        """
        """
        for window in current_visible_windows():
            left_face.append(window)  --> 걍 이렇게 하지 말고
        """
        left_face.extend(current_visible_windows())

        show_all(previous_styles)

    elif mod == "2":
        pass


def shaking_left_face_up(
    previous_styles,
    current_face,
    left_face,
    right_face,
    mod="1",
):
    if current_face == "L":
        return None
    current_face[0] = "L"

    if mod == "1":
        print("shaking_left_face_up")
        right_face.clear()
        right_face.extend([_ for _ in current_visible_windows() if _ not in left_face])

        for hwnd in right_face:
            hide_one(hwnd, previous_styles)
        print("\n\n\nleft face already worke up\n\n\n")

    elif mod == "2":
        pass
