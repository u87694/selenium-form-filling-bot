import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from flask import Flask, Response, request

form_url = 'https://clienthub.getjobber.com/client_hubs/b8f303c0-cc98-4f0e-b8c9-354ff52dd6e8/public/work_request/new?source=social_media'

FIRST_NAME      = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/div[1]/label/div[1]/placeholder-field/input'
LAST_NAME       = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/div[1]/label/div[2]/placeholder-field/input'
COMPANY_NAME    = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/div[1]/div[2]/div/placeholder-field/input'
EMAIL           = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/div[2]/div/div/placeholder-field/input'
PHONE_NUMBER    = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/div[3]/div[1]/div/placeholder-field/input'
STREET_1        = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/label/div[1]/div/placeholder-field/input'
STREET_2        = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/label/div[2]/div/placeholder-field/input'
CITY            = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/label/div[3]/div[1]/placeholder-field/input'
STATE           = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/label/div[3]/div[2]/placeholder-field/input'
ZIP_CODE        = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[1]/div[3]/label/div[3]/div[3]/placeholder-field/input'
SERVICE_DETAIL  = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[1]/sgx-fc-submission-section/ul/li/sgx-fc-submission-text-area/placeholder-field/textarea'
DATE_FIELD_1    = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[1]/sgx-fc-submission-date-picker/div/div/div/placeholder-field/input'
DATE_FIELD_2    = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[2]/sgx-fc-submission-date-picker/div/div/div/placeholder-field/input'
CHECK_1         = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[3]/sgx-fc-submission-checkbox-group/div/div[1]/input'
CHECK_2         = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[3]/sgx-fc-submission-checkbox-group/div/div[2]/input'
CHECK_3         = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[3]/sgx-fc-submission-checkbox-group/div/div[3]/input'
CHECK_4         = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/sgx-fc-submission/div[2]/sgx-fc-submission-section/ul/li[3]/sgx-fc-submission-checkbox-group/div/div[4]/input'
SUBMIT          = '/html/body/div[3]/div[2]/div[1]/div/div/div/div/form/div/div[2]/div/input'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def scrape():
    # get arguments from request
    args = request.args
    first_name_keys = args.get('first_name') or ""
    last_name_keys = args.get('last_name') or ""
    company_name_keys = args.get('company_name') or ""
    email_keys = args.get('email') or ""
    phone_number_keys = args.get('phone_number') or ""
    address_1_keys = args.get('address_1') or ""
    address_2_keys = args.get('address_2') or ""
    city_keys = args.get('city') or ""
    state_keys = args.get('state') or ""
    zip_code_keys = args.get('zip_code') or ""
    service_detail_keys = args.get('service_text') or ""
    date_1_keys = args.get('date_1') or None
    date_2_keys = args.get('date_2') or None
    check_1_keys = args.get('check_1') or None
    check_2_keys = args.get('check_2') or None
    check_3_keys = args.get('check_3') or None
    check_4_keys = args.get('check_4') or None

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"

    options = uc.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--incognito")
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--start-maximized")

    print('Starting Browser')
    driver = uc.Chrome(options=options)

    driver.get(form_url)
    time.sleep(2)

    # Contact Detail
    try:
        first_name = driver.find_element(By.XPATH, FIRST_NAME)
        time.sleep(2)
        first_name.send_keys(first_name_keys)

        last_name = driver.find_element(By.XPATH, LAST_NAME)
        time.sleep(2)
        last_name.send_keys(last_name_keys)

        company_name = driver.find_element(By.XPATH, COMPANY_NAME)
        time.sleep(2)
        company_name.send_keys(company_name_keys)

        email = driver.find_element(By.XPATH, EMAIL)
        time.sleep(2)
        email.send_keys(email_keys)

        phone_number = driver.find_element(By.XPATH, PHONE_NUMBER)
        time.sleep(2)
        phone_number.send_keys(phone_number_keys)

    except Exception as e:
        print('Exception occured while filling "Contact Details"')
        print(f'\n{e}')
        driver.quit()
        return Response('exception occured while filling "Contact Details"')

    print('Filled Contact Details')

    # Address
    try:
        street_1 = driver.find_element(By.XPATH, STREET_1)
        time.sleep(2)
        street_1.send_keys(address_1_keys)

        street_2 = driver.find_element(By.XPATH, STREET_2)
        time.sleep(2)
        street_2.send_keys(address_2_keys)

        city = driver.find_element(By.XPATH, CITY)
        time.sleep(2)
        city.send_keys(city_keys)

        state = driver.find_element(By.XPATH, STATE)
        time.sleep(2)
        state.send_keys(state_keys)

        zip_code = driver.find_element(By.XPATH, ZIP_CODE)
        time.sleep(2)
        zip_code.send_keys(zip_code_keys)

    except Exception as e:
        print('Exception occured while filling "Address"')
        print(f'\n{e}')
        driver.quit()
        return Response('exception occured while filling "Address"')

    print('Filled Address')

    # Service Detail
    try:
        service_detail = driver.find_element(By.XPATH, SERVICE_DETAIL)
        time.sleep(2)
        service_detail.send_keys(service_detail_keys)

    except Exception as e:
        print('Exception occured while filling "Service Detail"')
        print(f'\n{e}')
        driver.quit()
        return Response('Exception occured while filling "Service Details"')

    print('Filled Service Detail')

    # Date Field 1
    try:
        if date_1_keys:
            date_field1 = driver.find_element(By.XPATH, DATE_FIELD_1)
            time.sleep(2)
            date_field1.send_keys(date_1_keys)
            print('Filled Date Field 1')

    except Exception as e:
        print('Exception occured while filling "First Data Field"')
        print(f'\n{e}')
        driver.quit()
        return Response('Exception occured while filling "First Date Field"')

    # Date Field 2
    try:
        if date_2_keys:
            date_field2 = driver.find_element(By.XPATH, DATE_FIELD_2)
            time.sleep(2)
            date_field2.send_keys(date_2_keys)
            print('Filled Date Field 2')

    except Exception as e:
        print('Exception occured while filling "Second Data Field"')
        print(f'\n{e}')
        driver.quit()
        return Response('Exception occured while filling "Second Date Field"')

    # Checkboxes
    try:
        if check_1_keys:
            check1 = driver.find_element(By.XPATH, CHECK_1)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", check1)
            print('Clicked first checkbox')

        if check_2_keys:
            check2 = driver.find_element(By.XPATH, CHECK_2)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", check2)
            print('Clicked second checkbox')

        if check_3_keys:
            check3 = driver.find_element(By.XPATH, CHECK_3)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", check3)
            print('Clicked third checkbox')

        if check_4_keys:
            check4 = driver.find_element(By.XPATH, CHECK_4)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", check4)
            print('Clicked fourth checkbox')
    except Exception as e:
        print('Exception occured while clicking one of the checkboxes')
        print(f'\n{e}')
        driver.quit()
        return Response('Exception occured while clicking one of the checkboxes')

    print('All details filled successfully')


    submit = driver.find_element(By.XPATH, SUBMIT)
    submit.click()
    print('Submitted')

    time.sleep(10)
    # Close the browser after form submission
    driver.quit()

    return Response('Form submitted with provided details')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
