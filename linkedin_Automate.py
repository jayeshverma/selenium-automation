import re
import scrapy
import  json
import  re
import requests
import selenium
import scrapy, os, logging, hashlib
import requests, json
from scrapy.http import HtmlResponse
from scrapy.cmdline import execute
from selenium import webdriver
from scrapy.utils.response import open_in_browser
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
chrome_options = Options()
# chrome_driver ="E:\\PycharmProjects\\SELENIUM_PROJECT\\driver\\chromedriver.exe"
# from parsel import Selector
# import pandas as pd
# from scrapy.http import HtmlResponse
# from scrapy.cmdline import execute
# # chrome_options.add_argument("--headless")
# from store_locators import db_config as dbc
#
# from scrapy.utils.response import open_in_browser
#
# from selenium.webdriver.firefox.options import Options
# from store_locators.items import StoreLocatorsItem
# from store_locators.spiders.common_functions import Func
import datetime
import time
# import MySQLdb as pymysql
# class Store512Spider(scrapy.Spider):
#     name = 'linkedin'
#     cnt = 0
#     # allowed_domains = []
#     start_urls = ['https://www.example.com']
#     chrome_driver = "E:\\PycharmProjects\\SELENIUM_PROJECT\\driver\\chromedriver.exe"

def login_page(executable_path="E:\\PycharmProjects\\SELENIUM_PROJECT\\driver\\chromedriver.exe"):
    try:
        start_url = url = 'https://www.linkedin.com/home'
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        path = "E:\\PycharmProjects\\SELENIUM_PROJECT\\driver\\msedgedriver.exe"
        # driver = webdriver.edge(options=chrome_options,service=chrome_driver)
        driver = webdriver.Edge()

        # driver = webdriver.Chrome(chrome_options=chrome_options)
        # chrome_options = webdriver.ChromeOptions()
        # options = Options()
        # options.add_argument("--headless")
        # driver = webdriver.Chrome()
        driver.get(start_url)
        time.sleep(2)
        res1 = HtmlResponse(url=driver.current_url, body=driver.page_source.encode('utf8'))
        # print(res1.text,"data")
        try:
            element1 = driver.find_element(by="xpath", value='//label[@class="input-label mb-1"]//..//div[@class="text-input flex"][1]//input[@autocomplete="username"]').send_keys('9670885057')
        except Exception as e:
            print(e,"Email or Phone Number is not click")

        try:
            element1 = driver.find_element(by="xpath", value='//label[@class="input-label mb-1"]//..//div[@class="text-input flex"][1]//input[@autocomplete="current-password"]').send_keys('Chinto@123')
        except Exception as e:
            print(e,"password is not click")

        try:
            login_button = driver.find_element(by="xpath",value='//div[@data-id="sign-in-form__footer"]//button').click()
        except Exception as e:
            login_button=''
            print(e,"Error in login buttin")
        time.sleep(2)

        try:
            post_create = driver.find_element(by="xpath" ,value='//button[@class="artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view share-box-feed-entry__trigger"]').send_keys("HI Everyone")
            print(post_create,"POST CREATE")
        except Exception as e:
            post_create=''
            print(e,"post create exception")

        try:
            send_sms = driver.find_element(by="xpath" ,value='//div[@class="ql-editor ql-blank"]').send_keys("HI Everyone")
            print(send_sms,"SEND S<MS")
        except Exception as e:
            send_sms=''
            print(send_sms,"Send SMS")
        # button disable of psot creation in LinkedIn
        # try:
        #     post_create_button = driver.find_element(by="xpath" , value='//div[@class="share-creation-state__schedule-and-post-container"]//button[@class="share-actions__primary-action artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]').click()
        # except Exception as e:
        #     post_create_button=''
        #     print(e,"error in post create")
        time.sleep(3)


    except Exception as e:
        print(e,"Error in some where")
if __name__ == "__main__":
    login_page()

# # if __name__ == "__main__":
# from scrapy.cmdline import execute
# execute("scrapy crawl linkedin".split())


