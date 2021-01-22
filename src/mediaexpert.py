from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class MediaExpert:
    def __init__(self, settings):
        if settings is not None:
            self.data = settings
            self.driver_path = settings.get_driver_path()
            self.product_link = settings.get_link()
            self.is_for_company = settings.is_for_company()
            self.wait_time = settings.get_wait_for_element()
        else:
            raise ValueError('there is no settings specified!')

    def open_browser(self):
        try:
            print('opening browser...')
            self.driver = webdriver.Firefox(executable_path=r'D:\portable_programs\geckodriver\geckodriver.exe')
            # item_to_open = sys.argv[1]
            print('opened browser: ' + self.product_link)
            self.driver.get(self.product_link)
        except Exception as e:
            print('error while opening browser!', e)

    def add_to_cart(self):
        try:
            print('looking for buying option...')
            button = self.driver.find_elements_by_css_selector('div.c-offerBox_addToCart a')[1]    
            WebDriverWait(self.driver, self.wait_time).until_not(EC.visibility_of_element_located((By.CLASS_NAME, 'c-modal_container ps is-modalContVisible')))
            button.click()
            print('going to cart...')
            time.sleep(2)
            self.driver.get('https://www.mediaexpert.pl/koszyk/lista')
            print('cart opened!')
        except Exception as e:
            print('error while adding to cart!', e)

    def select_delivery(self):
        try:
            print('selecting delivery...')
            time.sleep(1)
            #zaznaczenie dostawy
            delivery = self.driver.find_elements_by_css_selector('div.c-cart_transportWrapper input#cart_flow_list_step_transportMethod_3')[0]
            self.driver.execute_script("arguments[0].click();", delivery)
            print('delivery selected!')
        except Exception as e:
            print('error while selecting delivery!', e)

    def select_payment(self):
        try:
            #zaznaczenie platnosci
            print('payment selecting...')
            # payment = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.c-cart_paymentWrapper input#cart_flow_list_step_paymentGroup_35')))
            print('payment selected!')
        except Exception as e:
            print('error while selecting payment!')

    def login(self):
        try:
            go_further = WebDriverWait(self.driver, self.wait_time).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.c-btn.is-primary.is-big.is-submitBtn')))
            self.driver.execute_script("arguments[0].click()", go_further)

            # logowanie
            print('selecting login method...')
            without_login = WebDriverWait(self.driver, self.wait_time).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.c-group_row.is-guestBtn a')))
            without_login.click()
            print('login skipped - as guest')
        except Exception as e:
            print('error while login!', e)

    def fill_form(self, data):
        try:
            if self.is_for_company == True:
                print('filling company form...')
                self.driver.find_elements_by_css_selector('div.a-form_row.is-orderAs label')[1].click()
                company_name = self.driver.find_elements_by_id('cart_flow_address_step_accountAddress_company')[0]
                company_name.send_keys(data.get_company_name())
                nip = self.driver.find_elements_by_id('cart_flow_address_step_accountAddress_nip')[0]
                nip.send_keys(data.get_nip())
            else:
                print('filling form...')
                firstName = self.driver.find_elements_by_id('cart_flow_address_step_accountAddress_firstName')[0]
                firstName.send_keys(data.get_first_name())
                surname = self.driver.find_elements_by_id('cart_flow_address_step_accountAddress_lastName')[0]
                surname.send_keys(data.get_last_name())

            mail = self.driver.find_elements_by_id('cart_flow_address_step_accountAddress_email')[0]
            mail.send_keys(data.get_mail())    
            street = self.driver.find_elements_by_id('cart_flow_address_step_accountAddress_street')[0]
            street.send_keys(data.get_street())
            house = self.driver.find_elements_by_id('cart_flow_address_step_accountAddress_houseNumber')[0]
            house.send_keys(data.get_house_number())
            apartment = self.driver.find_elements_by_id('cart_flow_address_step_accountAddress_apartmentNumber')[0]
            apartment.send_keys(data.get_apartment_number())
            postcode = self.driver.find_elements_by_id('cart_flow_address_step_accountAddress_postcode')[0]
            postcode.send_keys(data.get_postcode())
            city = self.driver.find_elements_by_id('cart_flow_address_step_accountAddress_city')[0] ## error
            city.send_keys('')
            phone = self.driver.find_elements_by_id('cart_flow_address_step_accountAddress_phone')[0]
            phone.send_keys(data.get_phone_number())
            check = self.driver.find_elements_by_id('cart_flow_address_step_consentForm_consent_332')[0]
            self.driver.execute_script("arguments[0].click();", check)
            print('form filled!')

            # time.sleep(1) #retrying selecting city
            # city = driver.find_elements_by_id('cart_flow_address_step_accountAddress_city')[0] ## error
            # city.send_keys('Katowice')
            time.sleep(1)
        except Exception as e:
            print('error while filling form!', e)

    def go_to_summary(self):
        try:
            #przejscie dalej do kalendarza
            # driver.find_elements_by_css_selector('div.c-calendar_contentRow a')[0]
            go_further_calendar = WebDriverWait(self.driver, self.wait_time).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.c-btn.is-primary.is-big')))
            self.driver.execute_script("arguments[0].click()", go_further_calendar)
            print('date chosen!')

            #przejscie dalej do podsumowania
            go_further = WebDriverWait(self.driver, self.wait_time).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.c-btn.is-primary.is-big')))
            self.driver.execute_script("arguments[0].click()", go_further)
        except Exception as e:
            print('error while going to summary!', e)

    def buy(self):
        try:
            print("started procedure!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            self.open_browser()
            self.add_to_cart()
            self.select_delivery()
            self.login()
            self.fill_form(self.data)
            self.go_to_summary()
            print('done!')
            return True
        except:
            return False
        finally:
            print('ended procedure...')
            # driver.quit()