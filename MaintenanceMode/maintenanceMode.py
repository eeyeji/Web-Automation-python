# Normal ↔ Maintenance mode 전환 웹 자동화 script

# #!/usr/bin/python3 -> 리눅스에서 사용시 필요한 샤뱅
 
# Selenium 설치: pip install selenium
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
 
 
#팝업창 관련
from selenium.webdriver.common.alert import Alert
 
#time.sleep
import time
 
#정해진 시간마다 작업해주기 위해서 cron job 설정 -> 리눅스에서
#분 시 일 월 요일 /파이썬의 위치 /실행파일의 위치
#분 시 일 월 요일 /파이썬의_절대경로/python3 /크롤링_파이썬_스크립트의_절대경로/script.py
 
 
 
# 크롤링 옵션 생성
#options = webdriver.ChromeOptions()
 
# 백그라운드 실행 옵션 추가
#options.add_argument("headless")
 
#사이트 접속(SystemAdmin 탭으로 바로 진입)
driver = webdriver.Chrome()
#driver = webdriver.Chrome(options=options)
#url = ''
url = '주소 작성'
driver.get(url)
 
#크롬창 최대화
driver.maximize_window()
 
# 214서버 로그인 구현
#-------------------------------------------------------------------------------------------------
# 라이선스 초과로 인해 로그인 실패 시 계속 로그인 시도하기 위해 while문으로 작성
#while(True):
#    #id 버튼 클릭 및 id 입력
#    id_input = driver.find_element(By.ID, "user")
#    ActionChains(driver).send_keys_to_element(id_input, "ID작성").perform()
 
#    #pw 버튼 클릭 및 pw 입력
#    password_input = driver.find_element(By.ID, "password")
#    ActionChains(driver).send_keys_to_element(password_input, "비밀번호 작성").perform()
 
#    #login 버튼 클릭
#    login_btn = driver.find_element(By.CLASS_NAME, "login_button")
#    ActionChains(driver).click(login_btn).perform() 
 
#    #만약 정상적으로 진입하였다면 while문에서 빠져나가기
#    #파이썬 셀레니움으로 웹사이트 접근 시 현재 주소를 확인하는 기능: driver.current_url
#    if (driver.current_url == '로그인 후 접속되는 주소'):
#        print(driver.current_url + "로그인 성공")
#        break   
#-------------------------------------------------------------------------------------------------
 
 
#id 버튼 클릭 및 id 입력
id_input = driver.find_element(By.ID, "user")
ActionChains(driver).send_keys_to_element(id_input, "ID 작성").perform()
 
#pw 버튼 클릭 및 pw 입력
password_input = driver.find_element(By.ID, "password")
ActionChains(driver).send_keys_to_element(password_input, "비밀번호 작성").perform()
 
#login 버튼 클릭
login_btn = driver.find_element(By.CLASS_NAME, "login_button")
ActionChains(driver).click(login_btn).perform()  
 
 
 
 
#로그인 이후 라이선스 Cleaning 작업 진행
#System Admin 탭 -> Maintenance mode 진입
driver.find_element(By.CSS_SELECTOR, "copy - selector").click()
 
#Normal모드 -> Maintenance모드로 변경: 라이선스 끊기 위해, Maintenance모드는 유지보수 모드로, cb.manager만 접근 가능하고 나머지 사용자들은 로그아웃됨
driver.find_element(By.CSS_SELECTOR, "copy - selector").click()
 
#저장
driver.find_element(By.CSS_SELECTOR, "copy - selector").click()
 
 
#팝업창 확인: Are you sure you want to change the system mode settings?
check = Alert(driver)
check.accept()
 
#time.sleep 걸어두기
time.sleep(1)
 
#System Admin 탭 -> Maintenance mode 진입
driver.find_element(By.CSS_SELECTOR, "copy - selector").click()
 
#다시 Normal 모드로 변경
driver.find_element(By.CSS_SELECTOR, "copy - selector").click()
 
#저장
driver.find_element(By.CSS_SELECTOR, "copy - selector").click()
 
#팝업창 확인: Are you sure you want to change the system mode settings?
check = Alert(driver)
check.accept()
 
#이유는 모르지만 크롬창 유지가 안됨, time.sleep 이용하여 유지시켜주자
time.sleep(2)
 
#창 종료
driver.quit()