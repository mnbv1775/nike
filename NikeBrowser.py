# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
import time
import random

class NikeBrowser:
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.delete_all_cookies()
        self.browser.get('https://www.nike.com/cn/zh_cn/s/register')
        time.sleep(5)

    def NikeSendMobileCap(self, mobileNumber):
        self.browser.find_element_by_class_name('phoneNumber').send_keys(mobileNumber)
        self.browser.find_element_by_class_name('sendCodeButton').click()

    def NikeCheckMobileCap(self, mobileCap):
        self.browser.find_element_by_xpath("//*[@placeholder='输入验证码']").send_keys(mobileCap)
        self.browser.find_element_by_class_name('nike-unite-submit-button').click()
    def NikeReg(self, password, firstName, lastName, Email):
        self.browser.find_element_by_xpath("//*[@placeholder='姓氏']").send_keys(firstName)
        self.browser.find_element_by_xpath("//*[@placeholder='名字']").send_keys(lastName)
        self.browser.find_element_by_xpath("//*[@placeholder='密码']").send_keys(password)
        self.browser.find_element_by_xpath( "//ul[@data-componentname='gender']/li").click()
        self.browser.find_element_by_class_name('checkbox').click()
        self.browser.find_element_by_class_name('nike-unite-submit-button').click()
    def NikeGetRegStatus(self):
        return self.browser.find_element_by_class_name('view-header').text
    def exitBrowser(self):
        self.browser.quit()