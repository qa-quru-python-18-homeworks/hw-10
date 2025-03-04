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
def test_issue_title_with_lambda_steps():
    with allure.step("Развернуть окно браузера на весь экран"):
        browser.driver.maximize_window()

    # Arrange
    with allure.step("Открыть главную страницу GitHub"):
        browser.open("https://github.com")

    # Act
    with allure.step("Открыть поле поиска"):
        browser.element(".search-input-container").click()

    with allure.step(f"Ввести '{REPOSITORY_NAME}' и выполнить поиск"):
        browser.element("#query-builder-test").type(f"{REPOSITORY_NAME}").press_enter()

    with allure.step(f"Перейти в репозиторий '{REPOSITORY_NAME}' из результатов"):
        browser.element(f"[href='/{REPOSITORY_NAME}']").click()

    with allure.step("Открыть вкладку Issues"):
        browser.element("#issues-tab").click()

    with allure.step(f"Открыть задачу (issue) '{ISSUE_NAME}'"):
        browser.element(by.text(f"{ISSUE_NAME}")).click()

    # Assert
    with allure.step(f"Проверить, что заголовок задачи равен '{ISSUE_NAME}'"):
        browser.element("[data-testid='issue-title']").should(
            have.text(f"{ISSUE_NAME}")
        )
