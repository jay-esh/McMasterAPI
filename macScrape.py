import requests
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(
    'https://academiccalendars.romcmaster.ca/content.php?catoid=41&navoid=8647')
driver.implicitly_wait(2)

with open('courseData.csv', mode='w') as f:
    csv_writer  = csv.writer(f)
    page = 1
    for i in range(0, 32):
        courseRows = driver.find_elements(by=By.XPATH,
                                        value='//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr')
        for j in range(3, len(courseRows)-1):
            try:
                course = driver.find_element(by=By.XPATH,
                                            value=f'//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[{j}]/td[2]/a')
                courseText  = course.text
                print(courseText)
                course.click()

                discription = driver.find_element(by=By.XPATH,
                                                value=f'//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[{j}]/td[2]/table/tbody/tr/td/div[2]')
                discText = discription.text
                print(discText)
            except:
                pass

            csv_writer.writerow([courseText, discText]) # write to the csv file
        # nextpage = driver.find_element(by=By.XPATH,
        #                             value=f'//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[104]/td/a[{page}]')
        page += 1
        
        # nextpage = driver.find_element_by_css_selector(f'[aria-label = "Page {page}"]')
        nextpage = driver.find_element(by=By.CSS_SELECTOR, value=f'[aria-label = "Page {page}"]')

        nextpage.click()

        
        print(f'\n\n PAGE NUMBER ----> {page} \n\n\n')
        # //*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[105]/td/a[1]
        # //*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[105]/td/a[2]
# //*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[104]/td/a[1]
# //*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[104]/td/a[2]
# //*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[104]/td/a[2]

# //*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[105]/td/a[3]
# //*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[104]/td/a[3]
# //*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[108]/td/a[5]

# //*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[104]/td/a[3]
# //*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[105]/td/a[3]