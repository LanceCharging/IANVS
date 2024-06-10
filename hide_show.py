from win32gui import FindWindow, GetWindowLong, SetWindowLong, ShowWindow
from win32con import GWL_EXSTYLE, WS_EX_TOOLWINDOW, SW_HIDE, SW_SHOW

from pygetwindow import getAllWindows  # 백그라운드 윈도우들은 무시함

from IANVS_setting import env_update


def hide_one(hwnd, previous_styles):

    if hwnd != 0:
        try:
            style = GetWindowLong(hwnd, GWL_EXSTYLE)
            previous_styles[hwnd] = style

            style |= WS_EX_TOOLWINDOW  # 비트연산을 하는 이유 -> '스타일'의 이진수 각 비트마다 다른 속성을 가리킴. 가령, WS_EX_TOOLWINDOW가 참인 경우는 2^7인 128이 됨 -> 2진수 1000000 -> 고로, 각 비트는 독립적임

            SetWindowLong(hwnd, GWL_EXSTYLE, style)
            ShowWindow(
                hwnd, SW_HIDE
            )  # 요게 WS_EX_TOOLWINDOW와 같이 쓰여야 하는 이유 -> 느낌이 좀 다르긴 한데 설정 적용 이후 F5(새로고침)하는 것과 비슷함 -- 껍데기를 숨기는 거라고 해야 하나..
        except:
            pass


def show_one(hwnd, previous_styles):

    if hwnd in previous_styles:
        try:
            SetWindowLong(hwnd, GWL_EXSTYLE, previous_styles[hwnd])
            ShowWindow(hwnd, SW_SHOW)

            del previous_styles[hwnd]
        except:
            pass


def hide_all(previous_styles):
    hwnds = [_._hWnd for _ in getAllWindows() if _.title != "" and _._hWnd != 0]
    for hwnd in hwnds:
        try:
            hide_one(hwnd, previous_styles)
        except:
            pass


def show_all(previous_styles):

    every_keys = [
        _ for _ in previous_styles.keys() if _ != 0
    ]  # 이터레이션 중에 딕셔너리 사이즈가 바뀌면 안 되나 봄 -> keys().copy()도 안 먹힘
    for hwnd in every_keys:
        try:
            SetWindowLong(hwnd, GWL_EXSTYLE, previous_styles[hwnd])
            ShowWindow(hwnd, SW_SHOW)

            del previous_styles[hwnd]
        except:
            pass


def current_visible_windows():
    return [_._hWnd for _ in getAllWindows() if _.title != "" and _._hWnd != 0]
