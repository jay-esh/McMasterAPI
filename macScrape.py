# from cgitb import html
# from dis import dis
# from faulthandler import disable
# from html.parser import HTMLParser
# from warnings import catch_warnings
# from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(
    'https://academiccalendars.romcmaster.ca/content.php?catoid=41&navoid=8647')
driver.implicitly_wait(5)

for i in range(0, 32):
    courseRows = driver.find_elements(by=By.XPATH,
                                      value='//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr')
    for j in range(3, len(courseRows)-1):
        course = driver.find_element(by=By.XPATH,
                                     value=f'//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[{j}]/td[2]/a')
        print(course.text)
        course.click()

        discription = driver.find_element(by=By.XPATH,
                                          value=f'//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[{j}]/td[2]/table/tbody/tr/td/div[2]')
        print(discription.text)
        # print(programs)
    nextpage = driver.find_element(by=By.XPATH,
                                   value='//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[104]/td/a[1]')
    nextpage.click()
