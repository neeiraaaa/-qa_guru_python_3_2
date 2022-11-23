from selene.support.shared import browser
from selene import be, have


def test_successful_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_negative_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('fjfjfjfjjdlelcfkefldvlsbnd').press_enter()
    browser.element('[id= "rcnt"]').should(have.text('ничего не найдено'))