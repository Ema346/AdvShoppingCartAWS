import datetime

from faker import Faker

fake = Faker(locale='en_CA')
home_page_title = ' Advantage Shopping'
adv_shop_cart_url = 'https://advantageonlineshopping.com/#/'
my_account_url = 'https://advantageonlineshopping.com/#/myAccount'
old_username = fake.user_name()
new_username = old_username[0:14]
new_password = fake.password()
username = fake.user_name()[0:15]
password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
city = fake.city()
country = fake.country()
address = fake.street_address()
phone = fake.phone_number()
province = fake.province_abbr()
postal_code = fake.postcode()
DEMO = 'DEMO'

product_list = ['SPEAKERS', 'TABLETS', 'LAPTOPS', 'HEADPHONES', 'MICE']
Subject = fake.sentence(100)