def get_element_type(element_name, type, driver):
    element = None
    if type == 'id':
        element = driver.find_element_by_id(element_name)
    elif type == 'name':
        element = driver.find_element_by_name(element_name)
    elif type == 'xpath':
        element = driver.find_element_by_xpath(element_name)
    return element

def inputTextField(text, element_name, type, driver):
    element = get_element_type(element_name, type, driver)
    element.send_keys(text)

def clickButton(element_name, type, driver):
    element = get_element_type(element_name, type, driver)
    element.click()

def get_random_index_from_select_options(element_name, type, driver):
    element = get_element_type(element_name, type, driver)
    select = Select(element)
    max_ops_length = len(select.options)-1
    return random.randint(1, max_ops_length)

def inputSelectField(value, element_name, type, driver, select_by='text'):
    element = get_element_type(element_name, type, driver)
    select = Select(element)

    if select_by == 'index':
        select.select_by_index(value)
    elif select_by == 'text':
        select.select_by_visible_text(value)
    elif select_by == 'value':
        select.select_by_value(value)
    else:
        print("Defaulting to Visible Text")
        select.select_by_visible_text(value)
