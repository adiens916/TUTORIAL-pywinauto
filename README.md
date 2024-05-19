# TUTORIAL-pywinauto

윈도우 프로그램들을 자동화할 수 있는 프로그램 중에 **pywinauto**라는 파이썬 패키지가 있다.

일반적으로 자동화하는 방법엔 이미지 인식이 있다. 예를 들면 원하는 버튼 이미지를 인식한 후, 해당 버튼을 클릭하는 식이다.

반면 이 pywinauto는 프로그램에 있는 여러 버튼들을 객체로 인식할 수 있다. 그래서 **이미지가 필요없고**, 이미지가 가려지거나 위치가 달라지는 것도 신경쓸 필요가 없다.

다만 **원하는 객체를 찾는 과정**이 생각보다는 잘 안 된다.  
그래서 이 과정에 익숙해고자 이 저장소에서 여러 테스트를 해볼 예정이다.

## 참고
https://inpa.tistory.com/entry/pywinauto-%E2%9A%A1-%EC%9C%88%EB%8F%84%EC%9A%B0-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%9E%90%EB%8F%99%ED%99%94-%EC%82%AC%EC%9A%A9%EB%B2%95

## 팁
- 원하는 객체를 GUI 형태로 보여주는 **py_inspect**가 있다. 이걸 꼭 먼저 깔아서 실행해보는 걸 추천한다. 프로세스 정보들을 쉽게 볼 수 있어서 감을 익히는 데 도움이 된다.
  - [다운로드 링크](https://github.com/pywinauto/py_inspect)
  - 실행시킬 때는 cmd나 bash 같은 걸 열어서,  
  `python py_inspect.py` 입력하기.

- 원하는 프로그램이 **관리자 권한**으로 실행된 경우,  
pywinauto가 돌아가는 프로그램 (예: VS Code)도  
관리자 권한으로 실행되어야 함.
  - 안 그러면 app.connect()에서 해당 프로세스를 찾을 수 없다고 함.
  - [참고](https://stackoverflow.com/questions/68109824/getting-error-as-pywinauto-application-processnotfounderror-process-mmc-exe-n)
  - py_inspect를 실행시키는 cmd나 bash도  
  마찬가지로 관리자 권한으로 실행시켜야  
  좀 더 많은 객체를 볼 수 있음.

- 원하는 프로그램이 안 찾아지는 경우, app을 찾을 때 `Application(backend='uia')` 대신에 그냥 `Application()`을 쓰자.
  - 인자가 uia인 경우, app.windows() 결과가 하나도 안 뜬다.
  - 반면 그냥 빈 값 (기본값 win32)인 경우, 여러 개가 뜬다.
  - 이유는 아마 아래 내용에 있는 것 같은데, 추후 보완 필요.
  - [관련 내용?](https://stackoverflow.com/questions/61298283/pywinauto-find-read-text-in-a-dialog-popup-that-is-not-part-of-any-control-of#comments-61298283)

## 객체 찾는 법 관련 글들 모음
- https://m.blog.naver.com/bhb414/222281750237
- [공식 문서 - How to's](https://pywinauto.readthedocs.io/en/latest/HowTo.html#how-to-specify-a-dialog-of-the-application)
- [공식 문서 - 모듈 설명](https://pywinauto.readthedocs.io/en/latest/code/pywinauto.application.html)

## 기타
- https://stackoverflow.com/questions/42213490/pywinauto-how-to-select-this-dialog-which-spying-tool-to-use-what-information