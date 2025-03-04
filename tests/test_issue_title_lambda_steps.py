from selene import have, by
from selene.support.shared import browser
import allure

def test_issue_title_with_lambda_steps():
    with allure.step("Развернуть окно браузера на весь экран"):
        browser.driver.maximize_window()
    
    # Arrange
    with allure.step("Открыть главную страницу GitHub"):
        browser.open("https://github.com")

    # Act
    with allure.step("Открыть поле поиска"):
        browser.element(".search-input-container").click()
        
    with allure.step("Ввести 'eroshenkoam/allure-example' и выполнить поиск"):
        browser.element("#query-builder-test").type("eroshenkoam/allure-example").press_enter()
        
    with allure.step("Перейти в репозиторий 'eroshenkoam/allure-example' из результатов"):
        browser.element("[href='/eroshenkoam/allure-example']").click()
        
    with allure.step("Открыть вкладку Issues"):
        browser.element("#issues-tab").click()
        
    with allure.step("Открыть задачу (issue) 'Тестируем тест'"):
        browser.element(by.text("Тестируем тест")).click()

    # Assert
    with allure.step("Проверить, что заголовок задачи равен 'Тестируем тест'"):
        browser.element("[data-testid='issue-title']").should(have.text("Тестируем тест"))
