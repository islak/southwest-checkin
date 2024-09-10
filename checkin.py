from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def open_southwest_page(confirmation_number, first_name, last_name):
    chrome_driver_path = '/Users/hershkalsi/Documents/chromedriver-mac-arm64/chromedriver'

    chrome_options = Options()
    # chrome_options.add_argument('--headless') 

    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
    driver.get('https://www.southwest.com/air/check-in/index.html')
    time.sleep(2)  
    print(driver.title)  

    try:
        driver.find_element(By.ID, 'confirmationNumber').send_keys(confirmation_number)
        driver.find_element(By.ID, 'passengerFirstName').send_keys(first_name)
        driver.find_element(By.ID, 'passengerLastName').send_keys(last_name)

        driver.find_element(By.ID, 'form-mixin--submit-button').click()
        print('Form submitted!')
    except Exception as e:
        print(f"Error occurred: {e}")

    time.sleep(3)  
    driver.quit()
