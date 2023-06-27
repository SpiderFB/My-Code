from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
import time
import cv2
import pytesseract

Addhar_number = int(input("Enter: "))
URL = 'https://resident.uidai.gov.in/verify'


def check(Addhar_number):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(URL)
    driver.find_element_by_id("uidno").send_keys(Addhar_number)
    time.sleep(2)
    if(driver.find_element_by_class_name("form-group.has-success")):
        print("Captcha")
    # elif(driver.find_element_by_class_name("form-group.has-error")):
    else:
        driver.quit()
        print("Please enter valid Addhar number.")
        Addhar_number = int(input("Enter: "))
        check(Addhar_number)


check(Addhar_number)
# driver.find_element_by_img_id

#Phone_number = input("Enter phn nmber : ")
