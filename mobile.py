# -*- coding: utf-8 -*-
import requests

def Login(username, password):#登陆
    try:
        response = requests.get('http://api.jmyzm.com/http.do?action=loginIn&uid=' +username+ '&pwd=' +password).content
        if "|" in response:
            return response.split("|")[1]
    except:
        return ""
    return ""

def GetMobile(username, token):#获取手机号码
    try:
        response = requests.get('http://api.jmyzm.com/http.do?action=getMobilenum&pid=13750&uid=' + username + '&token=' + token + '&mobile=&size=1').text
        if "|" in response:
            return response.split('|')[0]
    except:
        return ''
    return response

def GetCaptcha(username, token, mobile):#获取手机验证码
    try:
        response = requests.get('http://api.jmyzm.com/http.do?action=getVcodeAndReleaseMobile&uid='+ username + '&token='+ token +'&mobile=' + mobile).text
        if "|" in response:
            return response.split('|')[1]
    except:
        return ''
    return ''

def AddBlackList(username, token, mobile):#手机号码拉黑
    try:
        response = requests.get('http://api.jmyzm.com/http.do?action=addIgnoreList&uid='+ username +'&token='+ token +'&mobiles='+ mobile +'&pid=13750').text
        if '1' in response:
            return 'succ'
    except:
        return 'fail'
    return 'fail'