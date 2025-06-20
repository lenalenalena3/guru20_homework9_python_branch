from selene import browser, have, be
from pathlib import Path
from selenium.webdriver.common.keys import Keys

def test_forms_filling_and_submit(open_page_demoqa):
    browser.element('#firstName').should(be.visible).type('Фамилия')
    browser.element('#lastName').should(be.visible).type('Имя')
    browser.element('#userEmail').should(be.visible).type('address@mail.ru')
    browser.element('#genterWrapper').all('label').element_by(have.text('Female')).click()
    browser.element('#userNumber').should(be.visible).type('81234567890')
    #значение для даты выбирается в календаре
    browser.element('#dateOfBirthInput').should(be.visible).click()
    browser.element('//select[@class="react-datepicker__year-select"]').should(be.visible).click()
    browser.element('//select[@class="react-datepicker__year-select"]').all('option').element_by(have.text('1991')).click()
    browser.element('//select[@class="react-datepicker__month-select"]').should(be.visible).click()
    browser.element('//select[@class="react-datepicker__month-select"]').all('option').element_by(have.text('September')).click()
    browser.all('//div[contains(@class,"react-datepicker__day")]').element_by(have.text("15")).click()

    browser.element('#subjectsInput').should(be.visible).type('Commerce').press_enter()
    browser.element('#hobbiesWrapper').all('//input/following-sibling::label').element_by(have.text('Music')).click()
    browser.element('//input[@type="file"]').should(be.visible).send_keys(str(Path("./attachment/img.jpg").resolve()))
    browser.element('#currentAddress').should(be.visible).type('г. Москва, ул. Шарикоподшипниковская, 13c33')
    #значения для справочников пишется в строке
    browser.element('#state').element('input').should(be.visible).set_value("Haryana").press_enter()
    browser.element('#city').element('input').should(be.visible).set_value("Panipat").press_enter()

    #отправка формы
    browser.element('[id="submit"]').click()

    #проверка сформированной таблицы
    browser.element('//table').all('td').should(
        have.exact_texts(
            'Student Name','Фамилия Имя',
            'Student Email','address@mail.ru',
            'Gender', 'Female',
            'Mobile','8123456789',
            'Date of Birth','15 September,1991',
            'Subjects','Commerce',
            'Hobbies','Music',
            'Picture','img.jpg',
            'Address','г. Москва, ул. Шарикоподшипниковская, 13c33',
            'State and City','Haryana Panipat'
        )
    )

#другой способ выбора значения для заполнения Даты и Списков "State and City"
def test_forms_filling_and_submit_another(open_page_demoqa):
    browser.element('#firstName').should(be.visible).type('Фамилия')
    browser.element('#lastName').should(be.visible).type('Имя')
    browser.element('#userEmail').should(be.visible).type('address@mail.ru')
    browser.element('#genterWrapper').all('label').element_by(have.text('Female')).click()
    browser.element('#userNumber').should(be.visible).type('81234567890')

    #значение для даты пишется в строке
    browser.element('#dateOfBirthInput').should(be.visible).send_keys(Keys.CONTROL + "A").type("15 Sep 1991").press_enter()

    browser.element('#subjectsInput').should(be.visible).type('Commerce').press_enter()
    browser.element('#hobbiesWrapper').all('//input/following-sibling::label').element_by(have.text('Music')).click()
    browser.element('//input[@type="file"]').should(be.visible).send_keys(str(Path("./attachment/img.jpg").resolve()))
    browser.element('#currentAddress').should(be.visible).type('г. Москва, ул. Шарикоподшипниковская, 13c33')

    # значения для справочников выбирается из списка
    browser.driver.execute_script("arguments[0].scrollIntoView(true);", browser.element('#state').locate())
    browser.element('#state').should(be.visible).click()
    browser.element('#state').all('//div[contains(@id, "option")]').element_by(have.text('Haryana')).click()
    browser.element('#city').should(be.visible).click()
    browser.element('#city').all('//div[contains(@id, "option")]').element_by(have.text('Panipat')).click()

    #отправка формы
    browser.element('[id="submit"]').click()

    #проверка сформированной таблицы
    browser.element('//table').all('td').should(
        have.exact_texts(
            'Student Name','Фамилия Имя',
            'Student Email','address@mail.ru',
            'Gender', 'Female',
            'Mobile','8123456789',
            'Date of Birth','15 September,1991',
            'Subjects','Commerce',
            'Hobbies','Music',
            'Picture','img.jpg',
            'Address','г. Москва, ул. Шарикоподшипниковская, 13c33',
            'State and City','Haryana Panipat'
        )
    )