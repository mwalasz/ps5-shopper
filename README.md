## ps5-shopper

Bot for checking media-expert page for PS5 availability and eventually performing full purchase process :wink:

### Configuration

To properly use it, first you have to configure `settings.json` file.
```json
{
    "product_link": "https://www.mediaexpert.pl/gaming/playstation-5/konsole-ps5/konsola-sony-ps5",
    "is_company_purchase": false,
    "company_data": {
        "company_name": "",
        "nip": "",
        "mail": "",
        "street": "",
        "house_number": "",
        "apartment_number": "",
        "postcode": "",
        "city": "",
        "phone_number": ""
    },
    "personal_data": {
        "first_name": "",
        "last_name": "",
        "mail": "",
        "street": "",
        "house_number": "",
        "apartment_number": "",
        "postcode": "",
        "city": "",
        "phone_number": ""
    },
    "check_time_interval": 60,
    "wait_time": 600,
    "geckodriver_path": ""
}

```


You can either perform company or personal purchase. To specify on which method you have decided on, fill `is_company_purchase` properly. Then, you can focus on data which is supposed to be filled in the form on the shop page - fill:
- `company_data` if `is_company_purchase = true`
- `personal_data` if `is_company_purchase = false`.

`product_link` variable stands for the product that you are aiming for. By default, it's link for the hero mentioned in repo's tite :innocent: However, you can buy insert here link for any product that you want to possess.

By specyfing `check_time_interval` you can choose the time intervals between consecutive product availability checks.

Also you have to specify absolute path to `geckodriver.exe` driver, which allows script to open proper browser and run operation. 
You can find it [here](https://github.com/mozilla/geckodriver/releases).

## Usage

Simply run the `bot.py` script.

## Requirements

You need to have installed python 3.x+ and following packages:
- selenium - performing operations in browser
- APScheduler - scheduling task for checking for the product availability
- requests-html - checking for the product availability without opening browser
