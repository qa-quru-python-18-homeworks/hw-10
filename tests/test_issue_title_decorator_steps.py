import allure

from selene import have, by
from selene.support.shared import browser
from allure_commons.types import Severity


@allure.tag("Web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Waldemar")
@allure.feature("Задачи в репозитории")
@allure.story("Неавторизованный пользователь может посмотреть задачу в репозитории")
@allure.link("https://github.com", name="GitHub Homepage")
def test_issue_title_with_decorator_steps():
    maximize_browser_window()

    # Arrange
    open_github_home_page()

    # Act
    open_search_field()
    search_for_repository()
    open_repository_from_results()
    open_issues_tab()
    open_specific_issue()

    # Assert
    verify_issue_title()


# Steps


@allure.step("Развернуть окно браузера на весь экран")
def maximize_browser_window():
    browser.driver.maximize_window()


@allure.step("Открыть главную страницу GitHub")
def open_github_home_page():
    browser.open("https://github.com")


@allure.step("Открыть поле поиска")
def open_search_field():
    browser.element(".search-input-container").click()


@allure.step("Ввести 'eroshenkoam/allure-example' и выполнить поиск")
def search_for_repository():
    browser.element("#query-builder-test").type(
        "eroshenkoam/allure-example"
    ).press_enter()


@allure.step("Перейти в репозиторий 'eroshenkoam/allure-example' из результатов")
def open_repository_from_results():
    browser.element("[href='/eroshenkoam/allure-example']").click()


@allure.step("Открыть вкладку Issues")
def open_issues_tab():
    browser.element("#issues-tab").click()


@allure.step("Открыть задачу (issue) 'Тестируем тест'")
def open_specific_issue():
    browser.element(by.text("Тестируем тест")).click()


@allure.step("Проверить, что заголовок задачи равен 'Тестируем тест'")
def verify_issue_title():
    browser.element("[data-testid='issue-title']").should(have.text("Тестируем тест"))
