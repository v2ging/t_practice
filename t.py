
from selenium import webdriver
from selenium.webdriver.common.by import By # 셀레니움 업데이트 후 함수 사용 위해
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options # 브라우저 꺼지지 않게
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service= Service(ChromeDriverManager().install()),options=chrome_options)
url = 'https://ticket.yes24.com/Special/46237'                                                                  
browser.get(url)   

# 0. 로그인
login = browser.find_element(By.CLASS_NAME, "my-ticket")
login.click()

# alert 창 닫기
try:
        WebDriverWait(browser, 3).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        
        # 취소하기(닫기)
        alert.dismiss()
        
        # 확인하기
        alert.accept()
except:
        print("no alert")

# 0-1. id, pw 입력
browser.find_element(By.ID,"SMemberID").send_keys("zlzj01") # 내 아이디
browser.find_element(By.ID,"SMemberPassword").send_keys("rkslrksl0518!") # 내 비밀번호 
browser.find_element(By.ID,"btnLogin").click()

url = 'https://ticket.yes24.com/Special/46237'                                                                  
browser.get(url) 

# 1. 예매하기 누르기
ticket = browser.find_element(By.CLASS_NAME, "rn-bb03")
ticket.click()


# 2. 날짜 선택
# 새로운 창으로 이동 
# option cmd i -> 크롬 개발자도구 열기 
browser.switch_to.window(browser.window_handles[-1])
# 로딩 기다리기
time.sleep(5)

term = browser.find_element(By.ID, "2023-07-22")
term.click()

on = browser.find_element(By.CLASS_NAME, "on")
on.click()

seat = browser.find_element(By.ID, "btnSeatSelect")
seat.click()

