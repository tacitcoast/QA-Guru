from selene import browser, have, be
import os


def test_registration_demoqa():
    browser.open('https://demoqa.com/automation-practice-form/')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')

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
    browser.element('#subjectsInput').type('ma')
    browser.all("#subjectsWrapper div").element_by(have.exact_text("Maths")).click()

    # Uploading a picture
    browser.element('#uploadPicture').send_keys(os.path.abspath('file/kotik.jpeg'))

    # Fill Current Address
    browser.element('#currentAddress').should(be.blank).type('Test test test')

    # Fill State and City
    browser.element('#state').click()
    browser.all("#state div").element_by(have.exact_text("NCR")).click()
    browser.element('#city').click()
    browser.all("#city div").element_by(have.exact_text("Delhi")).click()

    # Click the register button
    browser.element('#submit').click()

    # Check that the modal window has appeared
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    # We check that our text is filled in
    browser.element('.modal-body').should(have.text('Anna Malinovskaia'))
    browser.element('.modal-body').should(have.text('test@demoqa.com'))
    browser.element('.modal-body').should(have.text('Other'))
    browser.element('.modal-body').should(have.text('1234567890'))
    browser.element('.modal-body').should(have.text('11 January,1989'))
    browser.element('.modal-body').should(have.text('Maths'))
    browser.element('.modal-body').should(have.text('kotik.jpeg'))
    browser.element('.modal-body').should(have.text('Test test test'))
    browser.element('.modal-body').should(have.text('NCR Delhi'))

    # Closing the window
    browser.element('#closeLargeModal').click()

    # We check that the form is empty
    browser.element('#firstName').should(be.blank)
