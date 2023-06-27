from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/Users/Olga/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qahacking.guru/")
driver.set_window_size(1600,900)
time.sleep(5)


driver.get("https://qahacking.guru/")
driver.find_element(By.CSS_SELECTOR, ".uk-navbar-nav > li:nth-child(6) > a").click()
driver.find_element(By.ID, "question2_2").click()
time.sleep(5)
driver.find_element(By.ID, "question14_2").click()
time.sleep(5)
driver.find_element(By.ID, "question16_2").click()
time.sleep(5)
driver.find_element(By.ID, "question21_2").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Далее").click()
time.sleep(5)
driver.find_element(By.ID, "question23_2").click()
time.sleep(5)
driver.find_element(By.ID, "question24_2").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Далее").click()
time.sleep(5)
driver.find_element(By.ID, "question7_2").click()
driver.find_element(By.ID, "question8_1").click()
driver.find_element(By.ID, "question9_1").click()
driver.find_element(By.ID, "question10_2").click()
driver.find_element(By.ID, "question11_1").click()
driver.find_element(By.ID, "question12_1").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Далее").click()
time.sleep(5)
driver.find_element(By.ID, "question17_2").click()
driver.find_element(By.ID, "question18_2").click()
driver.find_element(By.ID, "question19_1").click()
driver.find_element(By.ID, "question20_1").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Далее").click()
time.sleep(5)
driver.find_element(By.ID, "question22_2").click()
driver.find_element(By.ID, "question25_2").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".qsm-submit-btn").click()
time.sleep(5)
driver.close()



  
