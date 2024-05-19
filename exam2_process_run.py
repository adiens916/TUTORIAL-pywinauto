from pywinauto import findwindows
from pywinauto.application import Application


def main():
    # title = "인증서 선택창"
    # proc = get_process_by_title(title)

    # XXX: 대상 프로그램이 관리자 권한으로 실행된 경우,
    # 파이썬도 관리자 권한으로 실행시켜야 함
    # (안 그러면 대상 프로세스 find는 되는데, connect가 안 됨)
    app = Application().connect(process=7528)

    # 디버깅용: 해당 앱의 모든 윈도우 가져옴
    # XXX: backend 인자가 uia면 []로 뜨는데,
    # backend 기본 값인 win32면 17개가 뜸.
    # windows = app.windows()
    # print(windows)

    # dlg = app.window(class_name="#32770")
    dlg = app.window(title="인증서 선택창")
    # dlg.print_control_identifiers()

    # 확인 버튼
    button = dlg.child_window(handle=5965892)
    button.print_control_identifiers()

    # 인증서 비밀번호 Edit 창
    edit = dlg["인증서 비밀번호Edit"]
    edit.print_control_identifiers()


def get_process_by_title(title: str):
    procs = findwindows.find_elements()
    for proc in procs:
        if title in str(proc):
            return proc


main()
