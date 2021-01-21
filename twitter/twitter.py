# coding: utf-8

from selenium import webdriver
import chromedriver_binary
import time
from settings import settings

b = webdriver.Chrome()

# twitterに遷移
b.get("https://twitter.com/home/")
# ログイン画面への遷移を待つ
time.sleep(2)

# 非ログインならログインする
if "ログイン" in b.title:
    idBox = b.find_element_by_css_selector("input[name='session[username_or_email]']")
    idBox.send_keys(settings.TID)
    passBox = b.find_element_by_css_selector("input[name='session[password]']")
    passBox.send_keys(settings.TPS)
    loginBtn = b.find_element_by_css_selector("div[data-testid='LoginForm_Login_Button']")
    loginBtn.click()
    time.sleep(2)

tweet = "テスト"
b.get("https://twitter.com/compose/tweet?text=" + tweet)

time.sleep(3)
tweetBtn = b.find_element_by_css_selector("div[data-testid='tweetButton']")
tweetBtn.click()