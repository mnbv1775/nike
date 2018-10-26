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
import mobile
import NikeBrowser
import setting

if __name__ == '__main__':
    mobileToken = mobile.Login(setting.PHONE_USER, setting.PHONE_PASS)
    if mobileToken!='':
        print('MobileLoginSucc Token:', mobileToken)
    else:
        print('MobileLoginFail')

    for i in range(1,setting.REG_ACCOUNT_NUM):
        print('Register Nike account:<'+str(i)+'>')
        f = open('regUser.txt', 'a+')
        Nike = NikeBrowser.NikeBrowser()

        mobileNumber = mobile.GetMobile(setting.PHONE_USER, mobileToken)
        print('GetMobileNumberSucc Mobile:', mobileNumber)

        Nike.NikeSendMobileCap(mobileNumber)
        for i in range(1, 10):
            mobileCap = mobile.GetCaptcha(setting.PHONE_USER, mobileToken, mobileNumber)
            time.sleep(5)
            print('MessageGetNoCap:', i, mobileCap)
            if mobileCap != '' and mobileCap != 'to_fast_try_again':
                break
        if mobileCap != '':
            mobileCap = mobileCap.replace(u'【NIKE中国】您的 NIKE 手机验证码是 ', '')
            Nike.NikeCheckMobileCap(mobileCap)
            time.sleep(3)
            Nike.NikeReg(setting.REG_ACCOUNT_PASSWORD, 'Yang', 'Yuchen', '256839713@qq.com')
            time.sleep(10)
            if u'注册成功' in Nike.NikeGetRegStatus():
                print('RegSucc.')
                f.writelines('+86' + mobileNumber + ','+setting.REG_ACCOUNT_PASSWORD+'\n')
            Nike.exitBrowser()
        else:
            print('mobileCap is not right arriver.')
            Nike.exitBrowser()