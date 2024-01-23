from configuration import webDriver
import time
import aboutLogin.m_phone
import aboutLogin.m_kakao
import aboutLogin.a_phone
import aboutLogin.a_kakao

webDriver.cal()

# aboutLogin.m_phone()

# webDriver.wd.close_app() # 앱 종료
# time.sleep(5.0)

# webDriver.wd.launch_app() # 앱 백그라운드에서 재시작
# time.sleep(5.0)

# aboutLogin.m_kakao()

# webDriver.wd.close_app() # 앱 종료
# time.sleep(5.0)

# webDriver.wd.launch_app() # 앱 백그라운드에서 재시작
# time.sleep(5.0)

aboutLogin.a_phone()

webDriver.wd.close_app() # 앱 종료
time.sleep(5.0)

webDriver.wd.launch_app() # 앱 백그라운드에서 재시작
time.sleep(5.0)

aboutLogin.m_phone()

webDriver.wd.quit()
