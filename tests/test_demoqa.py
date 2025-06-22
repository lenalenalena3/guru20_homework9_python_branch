from demoga_tests.data import users
from demoga_tests.model.application import app

def test_forms_filling_and_submit(open_page_demoqa):
    student = users.student
    app.registration_page.open()
    app.registration_page.register(student)
    app.registration_page.should_have_registered(student)
