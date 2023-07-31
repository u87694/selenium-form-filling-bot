# from selenium import webdriver
from flask import Flask, request
from seleniumwire import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
from flask_cors import CORS


# Time to wait for SELECTORS.(second)
WAIT = 4
URL = 'https://book.housecallpro.com/book/Rapid-Clean-Restoration/c9fa32bd46114b4198441aa2d04f395e'

# This method is for chrome driver initialization. You can customize if you want.
def setDriver():
    seleniumwire_options = {}
    seleniumwire_options['exclude_hosts'] = ['google-analytics.com']

    # Set User Agent
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    # user_agent = UserAgent(fallback="Mozilla/5.0 (Macintosh; Intel Mac OS X10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36").random
    # Set Browser Option
    options = ChromeOptions()

    prefs = {"profile.password_manager_enabled": False, "credentials_enable_service": False, "useAutomationExtension": False}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('prefs', {'profile.default_content_setting_values.cookies': 2})

    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument("disable-popup-blocking")
    options.add_argument("disable-notifications")
    options.add_argument("disable-popup-blocking")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument("--incognito")



    options.add_argument('--ignore-certificate-errors')
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")

    driver = webdriver.Chrome(executable_path="chromedriver", options = options, seleniumwire_options=seleniumwire_options)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options, seleniumwire_options=seleniumwire_options)

    return driver


selectors = {
"next_btn":'//button[contains(.,"Next")]',
"fullname":'//input[@id="name_field"]',
"address":'//input[@id="street"]',
"unit":'//input[@id="street_line_2"]',
"city":'//input[@id="city"]',
"state":'//input[@id="state"]',
"zip":'//input[@id="postal_code"]',
"phone":'//input[@id="mobile_number_field"]',
"email":'//input[@id="email"]',
"confirm_btn":'//div[contains(@class,"right-align")]//button[contains(.,"Confirm")]'
}


def scrape(user_info):
    # user_info= {
    # 'product':'Stairs Carpet Cleaning',
    # 'fname':'Alan',
    # 'lname':'Myers',
    # 'address':'Andrusia',
    # 'unit':'',
    # 'city':'Indianapolis',
    # 'state':'IN',
    # 'zip':'46237',
    # 'phone':'3035365033',
    # 'email':'tr.soft.engineer@gmail.com'
    # }

    add_product_btn = f'//span[text()="{user_info["product"]}"]/ancestor::div[contains(@class,"item-text-area")]//div[contains(@class,"quick-add-buttons")]//div[contains(@class,"qty-plus-minus-col")]//button'
    print(user_info['product'])
    # print(type(add_product_btn))
    # Scrape Websites.
    print('################','Set Driver','################')

    driver = setDriver()
    driver.get(URL)

    time.sleep(WAIT)
    print('################','Click Add Button','################')
    add_product = driver.find_element(By.XPATH,add_product_btn)
    driver.execute_script("arguments[0].click();",add_product)

    time.sleep(WAIT)
    print('################','Click Next Button','################')
    WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['next_btn']))).click()

    time.sleep(WAIT)
    print('################','Input Full Name','################')

    full_name_input = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['fullname'])))

    full_name = user_info['fname'] + ' ' + user_info['lname']
    full_name_input.clear()
    full_name_input.send_keys(full_name)

    print('################','Input Address','################')

    street_input = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['address'])))

    street_input.clear()
    street_input.send_keys(user_info['address'])

    print('################','Input Unit','################')

    street_line_2_input = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['unit'])))

    street_line_2_input.clear()
    street_line_2_input.send_keys(user_info['unit'])

    print('################','Input City','################')

    city_input = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['city'])))

    city_input.clear()
    city_input.send_keys(user_info['city'])


    print('################','Input State','################')

    state_input = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['state'])))

    state_input.clear()
    state_input.send_keys(user_info['state'])

    print('################','Input Zip','################')

    zip_input = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['zip'])))

    zip_input.clear()
    zip_input.send_keys(user_info['zip'])

    print('################','Input Phone','################')

    phone_input = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['phone'])))

    phone_input.clear()
    phone_input.send_keys(user_info['phone'])

    print('################','Input Email','################')

    email_input = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['email'])))

    email_input.clear()
    email_input.send_keys(user_info['email'])

    print('################','Click Confirm Button','################')

    WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['confirm_btn']))).click()

    print('################','Close Browser','################')
    time.sleep(WAIT)
    driver.close()

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

app.config["DEBUG"] = True
@app.route('/scrape', methods=['GET'])
def scrape_get():
    try:
        # user_info= {
        # 'product':'Stairs Carpet Cleaning',
        # 'fname':'Alan',
        # 'lname':'Myers',
        # 'address':'Andrusia',
        # 'unit':'',
        # 'city':'Indianapolis',
        # 'state':'IN',
        # 'zip':'46237',
        # 'phone':'3035365033',
        # 'email':'tr.soft.engineer@gmail.com'
        # }
        args = request.args
        user_info = {}
        user_info['product'] = args.get('product') or ""
        user_info['fname'] = args.get('fname') or ""
        user_info['lname'] = args.get('lname') or ""
        user_info['address'] = args.get('address') or ""
        user_info['unit'] = args.get('unit') or ""
        user_info['city'] = args.get('city') or ""
        user_info['state'] = args.get('state') or ""
        user_info['zip'] = args.get('zip') or ""
        user_info['phone'] = args.get('phone') or ""
        user_info['email'] = args.get('email') or ""
        scrape(user_info)
        return "Success"
    except Exception as E:
        print(repr(E))
        return "Fail"

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)
