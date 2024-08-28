from selene import by, be, browser


def test_github():
    browser.open("/")

    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("Another test issue")).should(be.visible)


