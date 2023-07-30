from seleniumwire import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
from flask import Flask, Response


app = Flask(__name__)

@app.route('/', methods=['GET'])
def fill_form():

    # driver = webdriver.Firefox()

    form_url = 'https://clienthub.getjobber.com/client_hubs/b8f303c0-cc98-4f0e-b8c9-354ff52dd6e8/public/work_request/new?source=social_media'

    seleniumwire_options = {}
    seleniumwire_options['exclude_hosts'] = ['google-analytics.com']

    # Set User Agent
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
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
    # options.add_argument("--headless")

    driver = webdriver.Chrome(options = options, seleniumwire_options=seleniumwire_options)


    driver.get(form_url)

    time.sleep(2)

    #selenium.common.exceptions.NoSuchElementException

    # Contact Detail
    try:
        first_name   = driver.find_element(By.ID, 'contact_first_name')
        time.sleep(4)
        first_name.send_keys('First Name')
        last_name    = driver.find_element(By.ID, 'contact_last_name')
        time.sleep(2)
        last_name.send_keys('Last Name')
        company_name = driver.find_element(By.ID, 'company_name')
        time.sleep(4)
        company_name.send_keys('Company Name')
        email        = driver.find_element(By.ID, 'work_request_email')
        time.sleep(2)
        email.send_keys('Email@email.com')
        phone_number = driver.find_element(By.ID, 'work_request_phone')
        time.sleep(4)
        phone_number.send_keys('1234567890')
        
    except Exception as e:
        print('Exception occured while filling "Contact Details"')
        print(f'\n{e}')
        driver.quit()
        # return Response('exception occured while filling "Contact Details"')

    # Address
    try:
        street_1 = driver.find_element(By.ID, 'address_street1')
        time.sleep(4)
        street_1.send_keys('Street 1')
        street_2 = driver.find_element(By.ID, 'address_street2')
        time.sleep(4)
        street_2.send_keys('Street 2')
        city     = driver.find_element(By.ID, 'address_city')
        time.sleep(2)
        city.send_keys('City')
        state    = driver.find_element(By.ID, 'address_province')
        time.sleep(2)
        state.send_keys('State')
        zip_code = driver.find_element(By.ID, 'address_pc')
        time.sleep(2)
        zip_code.send_keys('12345')

    except Exception as e:
        print('Exception occured while filling "Address"')
        print(f'\n{e}')
        driver.quit()
        # return Response('exception occured while filling "Address"')

    # Service Detail
    try:
        service_detail = driver.find_element(By.XPATH, '//*[@id="new_work_request"]/div/sgx-fc-submission/div[1]/sgx-fc-submission-section/ul/li/sgx-fc-submission-text-area/placeholder-field/textarea')
        time.sleep(8)
        service_detail.send_keys('Service Detail')

    except Exception as e:
        print('Exception occured while filling "Service Detail"')
        print(f'\n{e}')
        driver.quit()
        # return Response('Exception occured while filling "Service Details"')

    # Date Field 1
    try:
        date_field1 = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[1]/sgx-fc-submission-date-picker/div/div/div/placeholder-field/input')
        time.sleep(4)
        date_field1.send_keys('2023-07-30')

    except Exception as e:
        print('Exception occured while filling "First Data Field"')
        print(f'\n{e}')
        driver.quit()
        # return Response('Exception occured while filling "First Date Field"')

    # Date Field 2
    try:
        date_field2 = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[2]/sgx-fc-submission-date-picker/div/div/div/placeholder-field/input')
        time.sleep(4)
        date_field2.send_keys('2023-07-30')

    except Exception as e:
        print('Exception occured while filling "Second Data Field"')
        print(f'\n{e}')
        driver.quit()
        # return Response('Exception occured while filling "Second Date Field"')

    # Checkboxes
    try:
        check1 = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[3]/sgx-fc-submission-checkbox-group/div/div[1]/input')
        time.sleep(1)
        driver.execute_script("arguments[0].click();", check1)
        print('Clicked first checkbox')

        check2 = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[3]/sgx-fc-submission-checkbox-group/div/div[2]/input')
        time.sleep(1)
        driver.execute_script("arguments[0].click();", check2)
        print('Clicked second checkbox')

        check3 = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[3]/sgx-fc-submission-checkbox-group/div/div[3]/input')
        time.sleep(1)
        driver.execute_script("arguments[0].click();", check3)
        print('Clicked third checkbox')

        check4 = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[3]/sgx-fc-submission-checkbox-group/div/div[4]/input')
        time.sleep(1)
        driver.execute_script("arguments[0].click();", check4)
        print('Clicked fourth checkbox')
    except Exception as e:
        print('Exception occured while clicking one of the checkboxes')
        print(f'\n{e}')
        driver.quit()
        # return Response('Exception occured while clicking one of the checkboxes')

    print('All details filled successfully')

    # Submit the form
    submit = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[2]/div/input')
    time.sleep(4)
    submit.click()

    time.sleep(30)
    # Close the browser after form submission
    driver.quit()

    # return Response('All details are filled successfully')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
