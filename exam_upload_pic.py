# -*- coding: utf-8 -*-
"Exam in QA Varna University of Management"
# Student Number : 1714015
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException


class ExamUploadPic(unittest.TestCase):
    "exam test"
    def setUp(self):
        "set up class"
        self.driver = webdriver.Chrome(
            executable_path='/home/traiana/Desktop/HW_2/QA/testing/chromedriver')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verification_errors = []
        self.accept_next_alert = True

    def test_upload_pic(self):
        "test with uploading a picture"
        driver = self.driver
        driver.get("https://mdn.mozillademos.org/files/3698/image_upload_preview.html")
        self.assertIn(
            "https://mdn.mozillademos.org/files/3698/image_upload_preview.html", driver.current_url)

        pic = driver.find_element_by_id("uploadImage")
        pic.click()
        pic.clear()
        pic.send_keys(
            "/home/traiana/Desktop/HW_2/QA/testing/Screenshot from 2019-01-08 22-54-09.png")
        page_content = driver.page_source

        self.assertIn("data:image/png;base64", page_content)

    def test_excel_document(self):
        "testing with excel document"
        driver = self.driver
        driver.get(
            "https://mdn.mozillademos.org/files/3698/image_upload_preview.html")
        self.assertIn(
            "https://mdn.mozillademos.org/files/3698/image_upload_preview.html", driver.current_url)

        excel = driver.find_element_by_id("uploadImage")
        excel.click()
        excel.clear()
        excel.send_keys("/home/traiana/Desktop/HW_2/QA/testing/winter_semester-11.xlsx-11-2.xls")

        alert = driver.switch_to_alert()
        alert_text = alert.text
        alert.accept()
        print(alert_text)

        self.assertIn("You must select a valid image file!", alert_text)

    def test_no_file(self):
        "testing without file"
        driver = self.driver
        driver.get("https://mdn.mozillademos.org/files/3698/image_upload_preview.html")
        self.assertIn(
            "https://mdn.mozillademos.org/files/3698/image_upload_preview.html", driver.current_url)

        button = driver.find_element_by_id("uploadImage")
        button.click()
        button.clear()

        try:
            self.is_alert_present()
        except NoAlertPresentException:
            # in real case developers should receive raised Exception
            # only printing is done for test exam purposes
            print("No file selected")
            raise

    def is_alert_present(self):
        "ver alert"
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException:
            return False
        return True

    def tearDown(self):
        "tear down class"
        # self.driver.quit()
        self.assertEqual([], self.verification_errors)

if __name__ == "__main__":

    unittest.main(
        # defaultTest = "exam_upload_pic.test_upload_pic"
    )
