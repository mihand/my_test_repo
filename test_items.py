'''
pytest --language=es test_items.py
pytest --language=fr test_items.py
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'

def test_btn_add_to_basket_exist(browser):
    br = browser.get(url)
    #time.sleep(30)
    try:
        button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-lg.btn-primary.btn-add-to-basket'))
        )
        btn_found = True
    except:
        btn_found = False
    assert btn_found, 'button add_to_basket not found'



