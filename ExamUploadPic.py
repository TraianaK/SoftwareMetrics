# -*- coding: utf-8 -*-
#Exam in QA Varna University of Management
#Student Number : 1714015
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.alert import Alert

class ExamUploadPic(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/home/traiana/Desktop/HW_2/QA/testing/chromedriver')
        print(111)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_upload_pic(self):
        driver = self.driver
        driver.get("https://mdn.mozillademos.org/files/3698/image_upload_preview.html")

        self.assertIn("https://mdn.mozillademos.org/files/3698/image_upload_preview.html", driver.current_url)

        pic = driver.find_element_by_id("uploadImage")
        pic.click()
        pic.clear()
        pic.send_keys("/home/traiana/Desktop/HW_2/QA/testing/Screenshot from 2019-01-08 22-54-09.png")

        screen = driver.save_screenshot("/home/traiana/Desktop/HW_2/QA/testing/screenshot_exam.png")
        page_content = driver.page_source

        self.assertIn("data:image/png;base64",page_content)

    def test_excel_document(self):
        driver = self.driver
        driver.get("https://mdn.mozillademos.org/files/3698/image_upload_preview.html")
        self.assertIn("https://mdn.mozillademos.org/files/3698/image_upload_preview.html", driver.current_url)

        excel = driver.find_element_by_id("uploadImage")
        excel.click()
        excel.clear()
        excel.send_keys("/home/traiana/Desktop/HW_2/QA/testing/winter_semester-11.xlsx-11-2.xls")

        alert = driver.switch_to_alert()
        alert_text = alert.text
        alert.accept()
        print(alert_text)

        self.assertIn("You must select a valid image file!",alert_text)

    def test_no_file(self):
        driver = self.driver
        driver.get("https://mdn.mozillademos.org/files/3698/image_upload_preview.html")
        self.assertIn("https://mdn.mozillademos.org/files/3698/image_upload_preview.html", driver.current_url)

        button = driver.find_element_by_id("uploadImage")
        button.click()
        button.clear()

        try:
            self.is_alert_present()
        except NoAlertPresentException as e:
            #in real case developers should receive raised Exception 
            #only printing is done for test exam purposes
            print("No file selected")

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True


    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main(
        #defaultTest ="ExamUploadPic.test_upload_pic" 
        )