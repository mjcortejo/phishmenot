# https://foundation.jblfmu.edu.ph/bacolod_hr2/bdo/47ab27ed/sso/login.php?josso_back_to=https://online.bdo.com.ph/sso/josso_security_check
import random
import string

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.generators import *
from utils.selenium import *

import pandas as pd

from utils.names import *

from faker import Faker

phl_cities_df = pd.read_csv('phl_cities.csv')

driver = webdriver.Chrome()
filipino_first_names = get_male_names()
filipino_first_names.extend(get_female_names())
filipino_last_names = get_names_family()
filipino_last_names.extend(get_names_middle())

while True:
    driver.get("https://nuevaeconomia.com.bo/bdo.php")

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.title_contains('Banco De Oro'))
    # Login
    fake = Faker()

    fake_profile = fake.profile(fields=['mail'])
    # "{'username': 'xlewis', 'name': 'Kelly Jackson', 'mail': 'sharon82@gmail.com'}"
    # print(fake_profile)

    # fake_first_name = fake.first_name()
    # fake_last_name = fake.last_name()
    # fake_full_name = fake_profile['name'].split(' ')
    fake_full_name = "{} {}".format(filipino_first_names[random.randint(0, len(filipino_first_names)-1)], filipino_last_names[random.randint(0, len(filipino_last_names)-1)])
    fake_full_name = fake_full_name.split(' ')
    fake_first_name = fake_full_name[0]
    fake_last_name = fake_full_name[1]
    favorite_number = randomInt(random.randint(2,3))
    fake_email = generate_email(fake_first_name, fake_last_name, fake_profile['mail'], favorite_number)

    fake_middle_name = filipino_last_names[random.randint(0, len(filipino_last_names)-1)]
    fake_maiden_name = filipino_last_names[random.randint(0, len(filipino_last_names)-1)]

    row = random.randint(0, len(phl_cities_df)-1)
    fake_city = phl_cities_df['City'][row]
    fake_state = phl_cities_df['Province'][row]
    fake_zipcode = fake.zipcode()

    fake_credit_card = fake.credit_card_number()
    fake_security_number = fake.credit_card_security_code()

    fake_full_address = "{} {} {} {}".format(fake.street_address(), fake.building_number(), fake_city, fake_state)

    gen_user_id = generate_user_id(fake_first_name, fake_last_name, favorite_number)
    gen_password = randomString(random.randint(10,14))

    inputTextField(gen_user_id, 'channelUserID', 'name', driver)
    inputTextField(gen_password, 'channelPswdPin', 'name', driver)

    clickButton('loginButton', 'id', driver)

    #Real stuff
    # account_selection = get_random_index_from_select_options('account', 'name', driver)
    # inputSelectField(account_selection, 'account', 'name', driver, select_by="index")
    # inputTextField(gen_user_id, 'uid', 'id', driver)
    # inputTextField(gen_password, 'ps', 'id', driver)
    # inputTextField(gen_password, 'cps', 'id', driver)
    # inputTextField("{}{}".format(gen_user_id, domains[random.randint(0, len(domains)-1)]), 'email', 'name', driver)
    # inputTextField(gen_password, 'epass', 'name', driver)
    inputTextField(fake_first_name, 'fname', 'id', driver)
    inputTextField(fake_middle_name, 'mname', 'id', driver)
    inputTextField(fake_last_name, 'lname', 'id', driver)
    inputTextField(fake_maiden_name, 'm_mname', 'name', driver)
    inputTextField("{:02d}/{:02d}/{}".format(random.randint(1,12),random.randint(1,31), random.randint(1957, 2000)), 'bday', 'name', driver)
    inputTextField(fake_full_address, 'address', 'name', driver)
    inputTextField(fake_city, 'city', 'name', driver)
    inputTextField(fake_state, 'state', 'name', driver)
    inputTextField(fake_zipcode, 'zip', 'name', driver)
    inputTextField(generate_phone_number(), 'phone', 'name', driver)
    inputTextField(fake_email, 'email', 'name', driver)
    clickButton('ide4', 'id', driver)
    # inputSelectField("{:02d}".format(random.randint(1,31)), 'bdays', 'name', driver)
    # inputTextField("{}".format(random.randint(1957, 2000)), 'birthyear', 'name', driver)
    # inputSelectField("Social Security Number", 'ssntin', 'name', driver)
    # inputTextField(randomInt(12), 'sstino', 'name', driver)
    inputTextField(randomInt(6), 'OTP', 'name', driver)
    # q1_selection = get_random_index_from_select_options('challenge1q', 'name', driver)
    # inputSelectField(q1_selection, 'challenge1q', 'name', driver, select_by="index")
    # q1_answer = fake.word()
    # inputTextField(q1_answer, 'ans1', 'name', driver)
    # inputTextField(q1_answer, 'c_ans1', 'name', driver)
    # q2_selection = get_random_index_from_select_options('challenge2q', 'name', driver)
    # inputSelectField(q2_selection, 'challenge2q', 'name', driver, select_by="index")
    # q2_answer = fake.word()
    # inputTextField(q2_answer, 'ans2', 'name', driver)
    # inputTextField(q2_answer, 'c_ans2', 'name', driver)
    # inputTextField(fake_credit_card, 'cc', 'name', driver)
    # exp_month = get_random_index_from_select_options('expmonth', 'name', driver)
    # inputSelectField(exp_month, 'expmonth', 'name', driver, select_by="index")
    # exp_year = get_random_index_from_select_options('expyear', 'name', driver)
    # inputSelectField(exp_year, 'expyear', 'name', driver, select_by="index")
    # inputTextField(fake_security_number, 'securitycode', 'name', driver)
    # # /html/body/div[2]/div[2]/form/div[6]/div/table/tbody/tr/td[2]/select
    # feedback = get_random_index_from_select_options('/html/body/div[2]/div[2]/form/div[6]/div/table/tbody/tr/td[2]/select', 'xpath', driver)
    # inputSelectField(feedback, '/html/body/div[2]/div[2]/form/div[6]/div/table/tbody/tr/td[2]/select', 'xpath', driver, select_by="index")

    clickButton('/html/body/div[2]/div[2]/font/font[2]/form/div/font/font/button[1]', 'xpath', driver)
