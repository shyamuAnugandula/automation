from selenium import webdriver
import time
import unittest
from htmltestrunner.pom_project.pages.LoginPage import LoginPage
from htmltestrunner.pom_project.pages.HomePage import HomePage
import HtmlTestRunner
url = 'https://consolebeta.vertoz.com//'


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(
            executable_path='C:/Users/DELL/Desktop/Python_program/Pythonprojects/venv/Scripts/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        self.driver.get(url)

        login = LoginPage(driver)
        login.enter_username('ashish.powar@vertoz.com')
        login.enter_password("OglYXO6Fz7OX")
        login.click_login()

        homepage = HomePage(driver)
        time.sleep(10)

        homepage.click_logut()



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/DELL/Desktop/Python_program/Pythonprojects/SampleProject/POM_PROJECT/reports'))
