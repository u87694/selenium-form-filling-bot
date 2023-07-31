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
URL = 'https://clienthub.getjobber.com/client_hubs/b8f303c0-cc98-4f0e-b8c9-354ff52dd6e8/public/work_request/new?source=social_media'

# This method is for chrome driver initialization. You can customize if you want.
def setDriver():
    print('Setting up driver')
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

    print('Options configured')

    # driver = webdriver.Chrome(executable_path="chromedriver", options = options, seleniumwire_options=seleniumwire_options)
    driver = webdriver.Chrome(options = options, seleniumwire_options=seleniumwire_options)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options, seleniumwire_options=seleniumwire_options)

    return driver


selectors = {
"first_name":       '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/div[1]/label/div[1]/placeholder-field/input',
"last_name":        '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/div[1]/label/div[2]/placeholder-field/input',
"company":          '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/div[1]/div[2]/div/placeholder-field/input',
"email":            '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/div[2]/div/div/placeholder-field/input',
"phone_number":     '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/div[3]/div[1]/div/placeholder-field/input',
"address_1":        '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/label/div[1]/div/placeholder-field/input',
"address_2":        '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/label/div[2]/div/placeholder-field/input',
"city":             '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/label/div[3]/div[1]/placeholder-field/input',
"state":            '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/label/div[3]/div[2]/placeholder-field/input',
"zip_code":         '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/label/div[3]/div[3]/placeholder-field/input',
"service_detail":   '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[1]/sgx-fc-submission-section/ul/li/sgx-fc-submission-text-area/placeholder-field/textarea',
"date_1":           '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[1]/sgx-fc-submission-date-picker/div/div/div/placeholder-field/input',
"date_2":           '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[2]/sgx-fc-submission-date-picker/div/div/div/placeholder-field/input',
"check_1":          '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[3]/sgx-fc-submission-checkbox-group/div/div[1]/input',
"check_2":          '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[3]/sgx-fc-submission-checkbox-group/div/div[2]/input',
"check_3":          '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[3]/sgx-fc-submission-checkbox-group/div/div[3]/input',
"check_4":          '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[3]/sgx-fc-submission-checkbox-group/div/div[4]/input',
"submit":           '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[2]/div/input'
}


def fill_form(user_info):

    print('################','Set Driver','################')
    driver = setDriver()
    driver.get(URL)

    print('################','Filling Contact Details','################')
    first_name = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['first_name'])))
    first_name.clear()
    first_name.send_keys(user_info['first_name'])

    last_name = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['lat_name'])))
    last_name.clear()
    last_name.send_keys(user_info['last_name'])

    company_name = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['company_name'])))
    company_name.clear()
    company_name.send_keys(user_info['company_name'])

    email = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['email'])))
    email.clear()
    email.send_keys(user_info['email'])

    phone_number = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['phone_number'])))
    phone_number.clear()
    phone_number.send_keys(user_info['phone_number'])

    print('################','Filling Address','################')

    address_1 = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['address_1'])))
    address_1.clear()
    address_1.send_keys(user_info['address_1'])

    address_2 = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['address_2'])))
    address_2.clear()
    address_2.send_keys(user_info['address_2'])

    city = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['city'])))
    city.clear()
    city.send_keys(user_info['city'])

    state = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['state'])))
    state.clear()
    state.send_keys(user_info['state'])

    zip_code = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['zip_code'])))
    zip_code.clear()
    zip_code.send_keys(user_info['zip_code'])

    service_detail = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['service_detail'])))
    service_detail.clear()
    service_detail.send_keys(user_info['service_detail'])

    print('################','Filling Dates','################')

    if user_info['date_1']:
        date_1 = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['date_1'])))
        date_1.clear()
        date_1.send_keys(user_info['date_1'])

    if user_info['date_2']:
        date_2 = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['date_2'])))
        date_2.clear()
        date_2.send_keys(user_info['date_2'])

    print('################','Checkboxes','################')

    if user_info['check_1']:
        check_1 = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['check_1'])))
        check_1.clear()
        check_1.send_keys(user_info['check_1'])

    if user_info['check_2']:
        check_2 = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['check_2'])))
        check_2.clear()
        check_2.send_keys(user_info['check_2'])

    if user_info['check_3']:
        check_3 = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['check_3'])))
        check_3.clear()
        check_3.send_keys(user_info['check_3'])

    if user_info['check_4']:
        check_4 = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['check_4'])))
        check_4.clear()
        check_4.send_keys(user_info['check_4'])

    print('################','Submit Form','################')

    WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selectors['submit']))).click()

    print('################','Close Browser','################')
    # time.sleep(WAIT)
    time.sleep(10)
    driver.close()

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

app.config["DEBUG"] = True
@app.route('/run', methods=['GET'])
def automate():
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
        user_info['first_name'] = args.get('first_name') or ""
        user_info['last_name'] = args.get('last_name') or ""
        user_info['company_name'] = args.get('company_name') or ""
        user_info['email'] = args.get('email') or ""
        user_info['phone_number'] = args.get('phone_number') or ""
        user_info['address_1'] = args.get('address_1') or ""
        user_info['address_2'] = args.get('address_2') or ""
        user_info['city'] = args.get('city') or ""
        user_info['state'] = args.get('state') or ""
        user_info['zip_code'] = args.get('zip_code') or ""
        user_info['service_detail'] = args.get('service_detail') or ""
        user_info['date_1'] = args.get('date_1') or False
        user_info['date_2'] = args.get('date_2') or False
        user_info['check_1'] = args.get('check_1') or False
        user_info['check_2'] = args.get('check_2') or False
        user_info['check_3'] = args.get('check_3') or False
        user_info['check_4'] = args.get('check_4') or False
        print('Received Details')
        fill_form(user_info)
        return "Success"
    except Exception as E:
        print(repr(E))
        return "Fail"

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)
