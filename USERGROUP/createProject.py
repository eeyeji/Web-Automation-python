#user group에서 Create Project 권한이 있는 그룹 확인

# Selenium 설치: pip install selenium
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Pandas 설치: pip install pandas
import pandas as pd

# BeautifulSoup을 설치: pip3 install bs4
from bs4 import BeautifulSoup

# request 모듈 설치: pip install requests
import requests

#팝업창 관련
from selenium.webdriver.common.alert import Alert

#time.sleep
import time

#정해진 시간마다 작업해주기 위해서 cron job 설정 -> 리눅스에서
#분 시 일 월 요일 /파이썬의 위치 /실행파일의 위치
#분 시 일 월 요일 /파이썬의_절대경로/python3 /크롤링_파이썬_스크립트의_절대경로/script.py
#30 15 * * * /usr/local/bin/python3 /your/path/to/script.py
#0 16 * * 1-5 /C:\Users\bnosoft_이예지\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12 /C:\Users\bnosoft_이예지\Desktop\웹자동화/214.py


# 크롤링 옵션 생성
#options = webdriver.ChromeOptions()

# 백그라운드 실행 옵션 추가
#options.add_argument("headless")

#사이트 접속(SystemAdmin 탭으로 바로 진입)
driver = webdriver.Chrome()
#driver = webdriver.Chrome(options=options)
#url = '주소 작성'


url = '주소 작성 '
driver.get(url)

#크롬창 최대화
driver.maximize_window()
time.sleep(1)

# 214서버 로그인 구현

#id 버튼 클릭 및 id 입력
id_input = driver.find_element(By.ID, "user")
ActionChains(driver).send_keys_to_element(id_input, "id 입력란").perform()
time.sleep(1)

#pw 버튼 클릭 및 pw 입력
password_input = driver.find_element(By.ID, "password")
ActionChains(driver).send_keys_to_element(password_input, "비밀번호 입력란").perform()

#login 버튼 클릭
login_btn = driver.find_element(By.CLASS_NAME, "login_button")
ActionChains(driver).click(login_btn).perform()  


#System Admin 탭 -> Groups 진입
driver.find_element(By.CSS_SELECTOR, "copy - selector").click()

#------------------------------------------------------------------------------------------------------------------------------------
#그룹 명 print
# x = driver.find_element(By.XPATH, '//*[@id="group"]/tbody/tr[1]/td[1]').text
# print("그룹명은 " + x + "입니다.")
#------------------------------------------------------------------------------------------------------------------------------------

#n번째 프로젝트    
i = 0

#해당 서버 group 수
#f {} : 포맷팅
while(True):
    
    try:
        i += 1 
        groupName = driver.find_element(By.XPATH, f'copy - XPATH').text
        #print(str(i) + "번째 그룹의 이름은 " + groupName + "입니다.")
        

        
    except:
        i -= 1
        print("Group 개수는 " + str(i) + "개 입니다.") 
        break

time.sleep(1)



# time.sleep(1)
#------------------------------------------------------------------------------------------------------------------------------------

# #System Admin 탭 -> Groups 진입 -> 각 group의 edit 진입
# driver.find_element(By.CSS_SELECTOR, "copy - selector").click()
# driver.find_element(By.CSS_SELECTOR, "copy - selector").click()

# #System Admin 탭 -> Groups 진입 -> 각 group의 edit 진입 -> Create Project 권한 여부 파악
# Check box에 설정이 적용되어 있는지 확인 하는 메소드: .is_selected()

# check = driver.find_element(By.CSS_SELECTOR, "copy - selector").is_selected()
# if check == False:
#     print("create Project 설정이 적용되어 있지 않습니다.")
#     print(check)
# else:
#     print("설정되어있습니다.")
#     print(check)

# #뒤로가기
# driver.find_element(By.CSS_SELECTOR, "copy - selector").click()
    
#------------------------------------------------------------------------------------------------------------------------------------

GroupName_list = []
CreateProject_list = []

projectCnt = 0
for j in range(1, i+1):
    n = ((j-1)*3)+2
    
    
    if j < 15:
        groupName = driver.find_element(By.XPATH, f'copy - XPATH').text
        print(str(j) + "번째 그룹의 이름은 " + groupName + "입니다.")
        GroupName_list.append(groupName)
        
        #edit 진입
        driver.find_element(By.CSS_SELECTOR, f"copy - selector").click()
        time.sleep(0.5) 
        driver.find_element(By.CSS_SELECTOR, f"copy - selector").click()
        time.sleep(0.5) 
        
        
        #creat Project 권한 여부 판단
        check = driver.find_element(By.CSS_SELECTOR, "copy - selector").is_selected()
        time.sleep(0.5) 
        
        if check == True:
            #creat Project 권한 있으면 cnt += 1
            print(check)
            CreateProject_list.append(check)
            projectCnt += 1
        else:
            CreateProject_list.append(check)
            
        #뒤로가기
        driver.find_element(By.CSS_SELECTOR, "copy - selector").click()
        time.sleep(1)   
        
    else:
        if j < 35:
            #스크롤 내리기 - pagedown
            driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5) 
            
            groupName = driver.find_element(By.XPATH, f'copy - XPATH').text
            print(str(j) + "번째 그룹의 이름은 " + groupName + "입니다.")
            GroupName_list.append(groupName)
            
            #edit 진입
            driver.find_element(By.CSS_SELECTOR, f"copy - selector").click()
            time.sleep(0.5) 
            driver.find_element(By.CSS_SELECTOR, f"copy - selector").click()
            time.sleep(0.5) 
            
            #creat Project 권한 여부 판단
            check = driver.find_element(By.CSS_SELECTOR, "copy - selector").is_selected()
            time.sleep(0.5) 
            
            if check == True:
                #creat Project 권한 있으면 cnt += 1
                print(check)
                CreateProject_list.append(check)
                projectCnt += 1
                
            else:
                CreateProject_list.append(check)
                
        
            #뒤로가기
            driver.find_element(By.CSS_SELECTOR, "copy - selector").click()
            time.sleep(1)        
        else:
            if j < 55:
                #스크롤 내리기 - pagedown
                driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
                time.sleep(1) 
                driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
                time.sleep(1) 
                
                groupName = driver.find_element(By.XPATH, f'copy - XPATH').text
                print(str(j) + "번째 그룹의 이름은 " + groupName + "입니다.")
                GroupName_list.append(groupName)
                
                #edit 진입
                driver.find_element(By.CSS_SELECTOR, f"copy - selector").click()
                time.sleep(0.5) 
                driver.find_element(By.CSS_SELECTOR, f"copy - selector").click()
                time.sleep(0.5) 
                
                #creat Project 권한 여부 판단
                check = driver.find_element(By.CSS_SELECTOR, "copy - selector").is_selected()
                time.sleep(1) 
                
                if check == True:
                    #creat Project 권한 있으면 cnt += 1
                    print(check)
                    CreateProject_list.append(check)
                    projectCnt += 1
                
                else:
                    CreateProject_list.append(check)
            
                #뒤로가기
                driver.find_element(By.CSS_SELECTOR, "copy - selector").click()
                time.sleep(1)

            else:
                if j < 72:
                    #스크롤 내리기 - pagedown
                    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
                    time.sleep(1)
                    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
                    time.sleep(1)
                    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
                    time.sleep(1)
                    
                    groupName = driver.find_element(By.XPATH, f'copy - XPATH').text
                    print(str(j) + "번째 그룹의 이름은 " + groupName + "입니다.")
                    GroupName_list.append(groupName)
                    
                    #edit 진입
                    driver.find_element(By.CSS_SELECTOR, f"copy - selector").click()
                    time.sleep(0.5)
                    driver.find_element(By.CSS_SELECTOR, f"copy - selector").click()
                    time.sleep(0.5)
                    
                    #creat Project 권한 여부 판단
                    check = driver.find_element(By.CSS_SELECTOR, "copy - selector").is_selected()
                    time.sleep(0.5)
                    
                    if check == True:
                        #creat Project 권한 있으면 cnt += 1
                        print(check)
                        CreateProject_list.append(check)
                        projectCnt += 1
                    else:
                        CreateProject_list.append(check)
                
                    #뒤로가기
                    driver.find_element(By.CSS_SELECTOR, "copy - selector").click()
                    time.sleep(1)    
                
                else:
                    #스크롤 내리기 - pagedown
                    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
                    time.sleep(1)
                    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
                    time.sleep(1)
                    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
                    time.sleep(1)
                    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
                    time.sleep(1)
                    
                    groupName = driver.find_element(By.XPATH, f'copy - selector').text
                    print(str(j) + "번째 그룹의 이름은 " + groupName + "입니다.")
                    GroupName_list.append(groupName)
                    
                    #edit 진입
                    driver.find_element(By.CSS_SELECTOR, f"copy - selector").click()
                    time.sleep(0.5)
                    driver.find_element(By.CSS_SELECTOR, f"copy - selector").click()
                    time.sleep(0.5)
                    
                    #creat Project 권한 여부 판단
                    check = driver.find_element(By.CSS_SELECTOR, "copy - selector").is_selected()
                    time.sleep(0.5)
                    
                    if check == True:
                        #creat Project 권한 있으면 cnt += 1
                        print(check)
                        CreateProject_list.append(check)
                        projectCnt += 1
                    else:
                        CreateProject_list.append(check)
                        
                
                    #뒤로가기
                    driver.find_element(By.CSS_SELECTOR, "copy - selector").click()
                    time.sleep(1)       

    
print("Create Porject 권한을 가지고 있는 Group 개수는 " + str(projectCnt) + "개 입니다.")

# print(GroupName_list)
# print(CreateProject_list)

# data = {'GroupName' : GroupName_list, 'Create Project' : CreateProject_list}
# userGroup = pd.DataFrame(data)
# userGroup.set_index('GroupName').to_excel('userGroup.xlsx', encoding='utf-8-sig')


#이유는 모르지만 크롬창 유지가 안됨, time.sleep 이용하여 유지시켜주자
time.sleep(1)

#창 종료
driver.quit()