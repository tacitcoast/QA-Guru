from selene.support.shared import browser
from selene import be, have


def test_google_search(browser_size, browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_invalid_google_search(browser_size, browser_open):
    browser.element('[name="q"]').should(be.blank).type('3546*ЕАлппдольдэ;%:').press_enter()
    browser.element('[id="center_col"]').should(have.text('ничего не найдено'))
