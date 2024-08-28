import allure
from allure_commons.types import Severity
from selene import by, be, browser


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")
    browser.open("/")

    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("Another test issue")).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "Antonio Banderas")
@allure.feature("Задачи в репозитории")
@allure.story("Проверка наличия нужного названия Issue в списке")
@allure.link("https://github.com", name="Testing")

def test_decorator_labels():
    browser.open("/")

    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("Another test issue")).should(be.visible)