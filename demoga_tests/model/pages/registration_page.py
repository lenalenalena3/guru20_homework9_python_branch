from selene import browser, have


class RegistrationPage:
    def __init__(self):
        self.should_have_registered = browser.element('//table').all('td')
        self._first_name = browser.element('#firstName')
        self._last_name = browser.element('#lastName')
        self._email = browser.element('#userEmail')
        self._gender = browser.element('#genterWrapper').all('label')
        self._mobile = browser.element('#userNumber')
        self._date_of_birth = browser.element('#dateOfBirthInput')
        self._date_of_birth_year = self._date_of_birth.element('//select[@class="react-datepicker__year-select"]')
        self._date_of_birth_month = self._date_of_birth.element('//select[@class="react-datepicker__month-select"]')
        self._date_of_birth_day = browser.all(
            '//div[contains(@class,"datepicker__day--") and not(contains(@class,"outside-month"))]')
        self._subjects = browser.element('#subjectsInput')
        self._hobbies = browser.element('#hobbiesWrapper').all('//input/following-sibling::label')
        self._picture = browser.element('//input[@type="file"]')
        self._current_address = browser.element('#currentAddress')
        self._state = browser.element('#state')
        self._state_elements = self._state.all('//div[contains(@id, "option")]')
        self._city = browser.element('#city')
        self._city_elements = self._city.all('//div[contains(@id, "option")]')
        self._submit_button = browser.element('[id="submit"]')

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        self._first_name.type(value)

    def fill_last_name(self, value):
        self._last_name.type(value)

    def fill_email(self, value):
        self._email.type(value)

    def set_radio_gender(self, value):
        self._gender.element_by(have.text(value)).click()

    def fill_mobile(self, value):
        self._mobile.type(value)

    def set_date_of_birth(self, year, month, day):
        self._date_of_birth.click()
        self._date_of_birth_year.click()
        self._date_of_birth_year.all('option').element_by(have.text(year)).click()
        self._date_of_birth_month.click()
        self._date_of_birth_month.all('option').element_by(have.text(month)).click()
        self._date_of_birth_day.element_by(have.text(day)).click()

    def set_subjects(self, value):
        self._subjects.type(value).press_enter()

    def set_checkbox_hobbies(self, value):
        self._hobbies.element_by(have.text(value)).click()

    def upload_picture(self, value):
        self._picture.send_keys(value)

    def fill_current_address(self, value):
        self._current_address.type(value)

    def set_state(self, value):
        browser.driver.execute_script("arguments[0].scrollIntoView(true);", self._state.locate())
        self._state.click()
        self._state_elements.element_by(have.text(value)).click()

    def set_city(self, value):
        self._city.click()
        self._city_elements.element_by(have.text(value)).click()

    def submit(self):
        self._submit_button.click()
