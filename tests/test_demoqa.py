from selene import browser, have, be
from demoga_tests.model import resource
from demoga_tests.model.pages.registration_page import RegistrationPage


def test_forms_filling_and_submit(open_page_demoqa):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('Фамилия')
    registration_page.fill_last_name('Имя')
    registration_page.fill_email('address@mail.ru')
    registration_page.set_radio_gender('Female')
    registration_page.fill_mobile('81234567890')
    registration_page.set_date_of_birth('1991', 'September', '15')
    registration_page.set_subjects('Commerce')
    registration_page.set_checkbox_hobbies('Music')
    registration_page.upload_picture(resource.path('img.jpg'))
    registration_page.fill_current_address('г. Москва, ул. Шарикоподшипниковская, 13c33')
    registration_page.set_state('Haryana')
    registration_page.set_city('Panipat')

    registration_page.submit()

    registration_page.should_have_registered.should(
        have.exact_texts(
            'Student Name', 'Фамилия Имя',
            'Student Email', 'address@mail.ru',
            'Gender', 'Female',
            'Mobile', '8123456789',
            'Date of Birth', '15 September,1991',
            'Subjects', 'Commerce',
            'Hobbies', 'Music',
            'Picture', 'img.jpg',
            'Address', 'г. Москва, ул. Шарикоподшипниковская, 13c33',
            'State and City', 'Haryana Panipat'
        )
    )
