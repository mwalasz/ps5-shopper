from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from requests_html import HTMLSession
from apscheduler.schedulers.background import BackgroundScheduler
import time
from time import gmtime, strftime
import os, sys, winsound, random
from src.mediaexpert import MediaExpert
from src.settings import Settings

scheduler = BackgroundScheduler()

def is_available(settings):
    session = HTMLSession()
    product_link = settings.get_link()
    r = session.get(product_link)
    to_cart_button = r.html.find('div.c-offerBox_addToCart a', first=True)
    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    if to_cart_button is not None and to_cart_button.text == 'Do koszyka':
        scheduler.remove_job('my_job_id')
        scheduler.shutdown(wait=False)
        ME = MediaExpert(settings)
        if ME.buy():
            winsound.PlaySound("SystemExit", winsound.SND_LOOP)
            return strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' ready to pay for item!'
        else:
            return 'some error occurred...'

    return date + ' product unavailable.';

def start_scheduler(settings):
    sec = settings.get_interval()
    scheduler.add_job(lambda: print(is_available(settings)), 'interval', seconds=int(random.randint(sec-2, sec+3)), id='my_job_id')
    scheduler.start()

settings = Settings('./settings/settings.json')
start_scheduler(settings)