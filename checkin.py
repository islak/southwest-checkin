from selenium import webdriver

def open_southwest_page():
    chrome_driver_path = '/Users/hershkalsi/Documents/chromedriver-mac-arm64/chromedriver'
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get('https://www.southwest.com/air/check-in/index.html')
    print('Opened Southwest check-in page.')
    driver.quit()  
