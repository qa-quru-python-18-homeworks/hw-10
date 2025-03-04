import allure

from selene import have, by
from selene.support.shared import browser
from allure_commons.types import Severity
from constants import *


@allure.tag("Web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Waldemar")
@allure.feature("Задачи в репозитории")
@allure.story("Неавторизованный пользователь может посмотреть задачу в репозитории")
@allure.link("https://github.com", name="GitHub Homepage")
def test_issue_title_selene():
    browser.driver.maximize_window()

    # Arrange
    browser.open("https://github.com")

    # Act
    browser.element(".search-input-container").click()
    browser.element("#query-builder-test").type(f"{REPOSITORY_NAME}").press_enter()
    browser.element(f"[href='/{REPOSITORY_NAME}']").click()
    browser.element("#issues-tab").click()
    browser.element(by.text(f"{ISSUE_NAME}")).click()

    # Assert
    browser.element("[data-testid='issue-title']").should(have.text(f"{ISSUE_NAME}"))
