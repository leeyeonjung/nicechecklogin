# ☕️ niceCheck Automation Login Code

</br>
</br>
</br>

## 📎프로젝트 소개
Appium, Selenium, Python을 이용하여 코드를 작성하였고 Pytest를 이용하여 test 코드를 실행 후 Pytest-Html 라이브러리를 이용하여 HTML 형식으로 Report를 확인할 수 있게 진행하였습니다.

Appium Version 2.5.1</br>
Appium-Python-Client 4.0.0</br>
Python 3.12.2</br>
Selenium Version: 4.19.0
</br>
</br>

## ✅ 어떻게 구현 했는지?
​
- ### 코드 구조
  -  2가지의 회원 유형에 따라 공통 로직과 개별 로직을 각각의 파일로 Logic 폴더 내에 구현 하였습니다.
  - 회원 유형에 따른 main 파일을 따로 구성하여 내용에 따른 부분만 import 하는 형식으로 작성 하였습니다.
  - 각 테스트 케이스를 하나의 def 로 구현하여 pytest를 통해 실행하는 방식입니다.
- ### 데이터
  - 회원 데이터는 엑셀 파일로 관리하여 openpyxl을 이용하여 데이터를 읽어 올 수 있습니다.
- ### 실행방식
  - pytest 를 통해 test 코드로 구현 되어 있는 부분을 실행 후, HTML 형식으로 Report 확인 가능 합니다.

</br>

​
## ✅ 구현하는 과정에서 어려웠던 점
​
- ### 버전 호환성
  - Appium의 최신 버전에 따른 코드가 많이 변경 되었고 특정 Appium / Appium-Python-Client / Selenium의 버전 호환 부분에서 어려움을 느꼈고,
    이를 구글링을 통하여 버전 호환을 맞추었습니다.
- ### 테스트 결과의 기준
  - 테스트 케이스 결과 값 판정 기준을 어떻게 설계해야 할지에 대해 많이 고민 하였고, UI 자동화 코드임으로 이미지 비교와 화면의 문구 노출을 기준으로 하였습니다. 그 이외에는 하단의 다양한 방법으로 진행하도록 지속적으로 고민 하고 있습니다. <br />
    1. 이미지 비교<br />
    2. 특정 문구 노출<br />
    3. 특정 API 값 <br />

</br>

​
## ✅ 이번 프로젝트를 통해 새로 배운 점
​
  - 테스트케이스 설계 <br />
    자동화 테스트 케이스 설계 상세 기준의 필요성과 그에 따른 다양한 방향성을 지속적으로 공부하고, 관련 많은 지식을 습득 하도록 할 것입니다.
​
  - Report <br />
    Pytest-Html Library 를 통한 HTML Report 출력 방법에 대해 배웠습니다.
</br>

​
## ✅ 내가 구현한 것 중에서 가장 잘했다고 생각하는 점(어필 포인트)
</br>

​
 이미지 비교, 특정 문구 노출처럼 단순 코드 실행만이 아닌 여러가지 Pass와 Fail의 기준에 대해 고려하였고 그를 구현해 내었습니다.
</br>
</br>
</br>

