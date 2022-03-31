import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select  # <--- add this import for drop down lists
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)


def setUp():
    print(f'------------------------------------')
    print(f'Test start at: {datetime.datetime.now()}')

    # make browser full screen
    driver.maximize_window()
    # give the browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # navigate to Advantage Shopping website
    driver.get(locators.adv_shop_cart_url)
    print(driver.title)
    # check that Advantage Shopping URL and the home page title are displayed
    if driver.current_url == locators.adv_shop_cart_url and driver.title == locators.home_page_title:
        print('Congratulations! Advantage Shopping website launched successfully')
        print(f'Advantage Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(10)
    else:
        print(f'Oops! Advantage Shopping did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        sleep(10)


def teardown():
    if driver is not None:
        print(f'------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


def sign_up():
    print(f'***************************************************************************')
    if driver.current_url == locators.adv_shop_cart_url:  # check we are on home page
        driver.find_element(By.ID, 'menuUserSVGPath').click()
        sleep(0.25)
        assert driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').is_displayed()
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(0.25)
        driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)
        sleep(0.25)
        driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
        sleep(0.25)
        driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
        sleep(0.25)
        driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
        sleep(0.25)
        driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
        sleep(0.25)
        driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
        sleep(0.25)
        driver.find_element(By.NAME, 'countryListboxRegisterPage').send_keys(locators.country)
        sleep(0.25)
        driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
        sleep(0.25)
        driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
        sleep(0.25)
        driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
        sleep(0.25)
        driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
        sleep(0.25)
        driver.find_element(By.NAME, 'i_agree').click()
        sleep(0.25)
        driver.find_element(By.ID, 'register_btnundefined').click()
        sleep(5)
        print(f' New user account is created')
        ################################################################################


def check_full_name():
    print(f'*******************************************************************************')
    if driver.current_url == locators.adv_shop_cart_url:  # check we are on home page
        assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
        sleep(0.25)
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(0.25)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
        sleep(0.25)
        print(f'************Validating Full name is displayed*********************************')
        if driver.find_element(By.XPATH, f'//label[contains(., "{locators.full_name}")]').is_displayed():
            print(f'You are in your account page: {locators.full_name}.')
        else:
            print(f'Something is not right, account page is not displayed')


def check_orders():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[2]').click()
    sleep(2)
    if driver.find_element(By.XPATH, f'//label[contains(.," - No orders - ")]').is_displayed():
        print(f'------------------------------------')
        print(f'Step passed ~~~No orders~~~ is displayed')
    else:
        print(f'Step failed ~~~No orders~~~ isn\'t displayed')


def log_in():
    if driver.current_url == locators.adv_shop_cart_url:
        print(f'---We are back on the Advantage Shopping website. Checking Registered User account.---')
        sleep(0.5)
        driver.find_element(By.ID, 'menuUser').click()
        sleep(0.5)
        driver.find_element(By.NAME, 'username').send_keys(locators.username)
        sleep(0.5)
        driver.find_element(By.NAME, 'password').send_keys(locators.password)
        sleep(0.5)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(0.5)
        print(f'---Registered User account successfully logged in!---')
    else:
        print('Oops! website missing, check your code or website.')


def log_out():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(5)


def delete_test_account():
    print(f'***************Delete Registered User Account***************************')
    assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
    sleep(0.25)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//button[contains(., "Delete Account")]').click()
    sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'div.deletePopupBtn.deleteRed').click()
    sleep(3)
    print(f'***************Registered User Account deleted ***************************')


def check_re_login():
    print(f'***************Check if User Account Exist***************************')
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.NAME, 'username').send_keys(locators.username)
    sleep(2)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    sleep(2)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(5)
    print(f'***************Incorrect User name or password. User does not exist***************************')


def check_homepage():
    print(f'------------------------------------- Validate Homepage -------------------------------------')
    if driver.current_url == locators.adv_shop_cart_url:  # check we are on home page
        driver.find_element(By.CSS_SELECTOR, '.closeBtn.loginPopUpCloseBtn').click()
        sleep(2)
        print(f'*************Check that SPEAKERS, TABLETS, HEADPHONES, LAPTOPS, MICE texts are displayed.**********')
        for i in range(len(locators.product_list)):
            assert driver.find_element(By.XPATH, f'//span[contains(., "{locators.product_list[i]}")]').is_displayed()
            verifyproducts = driver.find_element(By.XPATH, f'//span[contains(., "{locators.product_list[i]}")]').is_displayed()
            print(f'The product {locators.product_list[i]} text is displayed: {verifyproducts}')
            sleep(0.75)

        if driver.find_element(By.XPATH, '//h3[contains(.,"SPECIAL OFFER")]').is_displayed():
            print(f'------------------ Check that links are clickable ------------------')
            sleep(0.25)
        driver.find_element(By.XPATH, '//a[normalize-space()="POPULAR ITEMS"]').click()
        sleep(0.5)
        if driver.find_element(By.XPATH, '//h3[normalize-space()="POPULAR ITEMS"]').is_displayed():
            sleep(2)
            driver.find_element(By.ID, 'details_21').click()
            sleep(2.50)
            print(f'------------------ HP ROAR PLUS WIRELESS SPEAKER: View Details Button Selected ------------------')
            driver.find_element(By.XPATH, f'//span[contains(., "{locators.DEMO}")]').click()
            sleep(0.25)
            print(f'--------------- Our products page is displayed ------------------')
        else:
            print(f'------------------ Our products page is not displayed ------------------')

        driver.find_element(By.XPATH, '//a[normalize-space()="SPECIAL OFFER"]').click()
        sleep(0.5)
        if driver.find_element(By.XPATH, '//h3[contains(.,"SPECIAL OFFER")]').is_displayed():
            sleep(0.5)
            print(f'--------------- Special offer page is displayed ------------------')
        else:
            print(f'************Special offer page is not displayed****************')

        driver.find_element(By.XPATH, '//a[normalize-space()="POPULAR ITEMS"]').click()
        sleep(0.5)
        if driver.find_element(By.XPATH, '//h3[contains(.,"POPULAR ITEMS")]').is_displayed():
            sleep(0.75)
            print(f'------------------ Popular items page is displayed ------------------')
        else:
            print(f'************Popular items page is not displayed**************')

        driver.find_element(By.XPATH, '//a[normalize-space()="CONTACT US"]').click()
        sleep(0.75)
        if driver.find_element(By.XPATH, '//h1[contains(.,"CONTACT US")]').is_displayed():
            sleep(0.5)
            print(f'------------------ Contact us page is displayed ------------------')
        else:
            print(f'***********Contact us page is not displayed***************')

            print(f'************Check that main page logo is displayed***********************')
        if driver.find_element(By.XPATH, '//span[contains(., "dvantage")]').is_displayed() \
            and driver.find_element(By.XPATH, '//span[contains(., "DEMO")]').is_displayed():
            sleep(0.75)
            print(f'**********dvantage and DEMO from logo are displayed*************')
        else:
            print(f'**********The main logo is not displayed: check your code or website*************')

        driver.find_element(By.XPATH, '//h1[contains(., "CONTACT US")]').is_displayed()
        sleep(0.5)
        Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Laptops')
        sleep(1)
        Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text('HP Pavilion 15z Touch Laptop')
        sleep(0.75)
        driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
        sleep(0.75)
        driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.Subject)
        sleep(0.75)
        driver.find_element(By.ID, 'send_btnundefined').click()
        sleep(0.75)
        if driver.find_element(By.XPATH, '//a[@class="a-button ng-binding"]').is_displayed():
            print(f'Continue Shopping text is displayed')
        else:
            print(f'Continue Shopping text is not displayed ')

        print(f'********Contact us return message*****************')
        if driver.find_element(By.XPATH, f'//p[contains(., "Thank you for contacting Advantage support.")]').is_displayed():
            print(f'Thank you for contacting Advantage support message is displayed')
            sleep(5)
        else:
            print(f'Thank you message is not displayed')
        driver.find_element(By.XPATH, f'//a[contains(., " CONTINUE SHOPPING ")]').click()
        sleep(0.25)
