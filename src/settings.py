import json
from types import SimpleNamespace

class Settings:
    def __init__(self, file_name):
        print('opening settings file: ' + file_name + '...')
        self.load(file_name)
        x = 'company' if self.is_for_company() else 'person'
        print('settings loaded for: ' + x)
        print('refresh rate: ' + str(self.get_interval()) + 's')
        print('looking for: ' + self.get_name() + '...')

    def load(self, file_name):
        try:
            with open(file_name) as f:
                text = f.read()
                self.data = json.loads(text, object_hook=lambda d: SimpleNamespace(**d))
        except Exception as e:
            print('error while opening settings: ', e)

    def get_link(self):
        return self.data.product_link
    
    def get_name(self):
        return self.data.product_link.split('/')[-1]
    
    def get_interval(self):
        return self.data.check_time_interval
    
    def get_wait_for_element(self):
        return self.data.wait_time
    
    def get_driver_path(self):
        return self.data.geckodriver_path
    
    def is_for_company(self):
        return self.data.is_company_purchase

    def get_nip(self):
        return self.data.company_data.nip

    def get_company_name(self):
        return self.data.company_data.company_name

    def get_first_name(self):
        return self.data.personal_data.first_name

    def get_last_name(self):
        return self.data.personal_data.last_name

    def get_mail(self):
        if self.is_for_company() == True:
            return self.data.company_data.mail
        else:
            return self.data.personal_data.mail
    
    def get_street(self):
        if self.is_for_company() == True:
            return self.data.company_data.street
        else:
            return self.data.personal_data.street
    
    def get_house_number(self):
        if self.is_for_company() == True:
            return self.data.company_data.house_number
        else:
            return self.data.personal_data.house_number
    
    def get_apartment_number(self):
        if self.is_for_company() == True:
            return self.data.company_data.apartment_number
        else:
            return self.data.personal_data.apartment_number
    
    def get_postcode(self):
        if self.is_for_company() == True:
            return self.data.company_data.postcode
        else:
            return self.data.personal_data.postcode
    
    def get_city(self):
        if self.is_for_company() == True:
            return self.data.company_data.city
        else:
            return self.data.personal_data.city
    
    def get_phone_number(self):
        if self.is_for_company() == True:
            return self.data.company_data.phone_number
        else:
            return self.data.personal_data.phone_number