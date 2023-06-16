from selene import browser, have, be


def test_registration_demoqa():

    browser.open('https://demoqa.com/automation-practice-form/')

    # Fill in Name, Email, Gender, Mobile
    browser.element('#firstName').should(be.blank).type('Anna')
    browser.element('#lastName').should(be.blank).type('Malinovskaia')
    browser.element('#userEmail').should(be.blank).type('test@demoqa.com')
    browser.element('#gender-radio-3').with_(click_by_js=True).click()
    browser.element('#userNumber').should(be.blank).type('1234567890')

    # Choosing the date of birth
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="0"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1989"]').click()
    browser.element('.react-datepicker__day--011').click()

    # Fill Subjects, Hobbies
    browser.element('#subjectsInput').type('ma').press_enter()
    browser.element('#hobbies-checkbox-1').with_(click_by_js=True).click()

    # Uploading a picture
    browser.element('#uploadPicture').send_keys('/Users/annamalinovskaia/Desktop/Projects/Autotest_registrations_demoqa/tests/file/kotik.jpeg')

    # Fill Current Address
    browser.element('#currentAddress').should(be.blank).type('Test test test')

    # Временный костыль чтобы проверить заполнение формы
    browser.element('#userNumber').click().press_enter()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('#closeLargeModal').click()

'''
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.element('#state').type('NCR').press_enter()
    browser.element('#city').type('Delhi').press_enter().press_enter()
'''
