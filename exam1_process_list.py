from pywinauto import findwindows


f = open("process_list_sample.txt", "w", encoding="UTF-8")

# 현재 윈도우 화면에 있는 프로세스 목록 반환
procs = findwindows.find_elements()

for proc in procs:
    # 프로세스 ID, 핸들 값, 이름 등의 정보 보유
    message = f"{proc} / 프로세스: {proc.process_id}\n"
    f.write(message)

f.close()
