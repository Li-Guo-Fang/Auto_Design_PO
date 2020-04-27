import time
from selenium import webdriver
from Util.ObjectMap import find_element,find_elements
from Util.ParseConfig import *
from Conf.ProjVar import PageElementLocator_file_path

class loginPage():

    def __init__(self,driver):
        self.driver = driver

    '''[126mail_login]
       loginPage.loginlink=xpath>//a[contains(text(),'密码登录')]
    '''
    def get_login_link(self):
        link = read_ini_file_option(
            PageElementLocator_file_path,"126mail_login","loginPage.loginlink")
        element = find_element(self.driver,link.split(">")[0],link.split(">")[1])
        return element

    def click_login_link(self):
        self.get_login_link().click()
        time.sleep(2)

    """loginPage.frame=xpath>//iframe[contains(@id,'x-URS-iframe')]"""
    def get_iframe(self):
        link = read_ini_file_option(
            PageElementLocator_file_path,"126mail_login","loginPage.frame")
        element = find_element(self.driver,link.split(">")[0],link.split(">")[1])
        return element

    def switch_to_iframe(self):
        iframe = self.get_iframe()
        self.driver.switch_to.frame(iframe)
        time.sleep(1)

    """loginPage.username=xpath>//input[@name='email']"""
    def get_username(self):
        link = read_ini_file_option(
            PageElementLocator_file_path,"126mail_login","loginPage.username")
        element = find_element(self.driver,link.split(">")[0],link.split(">")[1])
        return element

    def input_username(self,username):
        self.get_username().send_keys(username)

    def get_password(self):
        link = read_ini_file_option(
            PageElementLocator_file_path,"126mail_login","loginPage.password")
        element = find_element(self.driver,link.split(">")[0],link.split(">")[1])
        return element

    def input_password(self,password):
        self.get_password().send_keys(password)

    def get_login_button(self):
        link = read_ini_file_option(
            PageElementLocator_file_path, "126mail_login", "loginPage.loginbutton")
        element = find_element(self.driver, link.split(">")[0], link.split(">")[1])
        return element

    def click_login_button(self):
        button = self.get_login_button()
        button.click()
        self.driver.switch_to.default_content()    #注意这一句要切出一下，如果这一句放sleep后面会找不到通讯录定位，先切换，再等待页面元素加载
        time.sleep(10)


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="d:\\chromedriver")
    driver.get("https://www.126.com")
    login_page = loginPage(driver)
    login_page.click_login_link()
    login_page.switch_to_iframe()
    login_page.input_username("lgf18301991450")
    login_page.input_password("411527lgf")
    login_page.click_login_button()