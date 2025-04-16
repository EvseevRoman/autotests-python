import allure
import pytest
from allure_commons._allure import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.actions.callback.wait import wait_elements


class TestFilterMenu:
    @pytest.mark.parametrize('profession_name,filter_names', [
        ("Программирование", ["Все программы", "Бэкенд-разработка", "Веб-разработка",
                              "Анализ данных", "IT-инфраструктура"]),
        ("Дизайн", ["Все программы", "Цифровой дизайн", "Дизайн среды", "Мода и фотография"]),
        ("Маркетинг", ["Все программы", "Бренд-маркетинг", "Аналитика", "Перформанс-маркетинг", "Электронная коммерция"])
    ])
    @allure.title('Проверка того, что кнопки фильтра соответствуют конкретной профессии')
    def test_filter_block(self, profession_name, filter_names, go_to_url, wait_element, wait_elements, selenium):
        """
        Входные данные:
        [
            ["Программирование", ["Все программы", "Бэкенд-разработка", "Веб-разработка",
                                  "Анализ данных", "IT-инфраструктура"]],
            ["Дизайн", ["Все программы", "Цифровой дизайн", "Дизайн среды", "Мода и фотография"]],
            ["Маркетинг", ["Все программы", "Бренд-маркетинг", "Аналитика", "Перформанс-маркетинг", "Электронная коммерция"]]
        ]
            
        Шаги:
        - Перейти по ссылке:
        - Нажать на кнопку из массива
            
        Ожидаемый результат:
        - Проверить, что в левой части фильтра находятся кнопки-фильтры конкретной профессии из списка
        """

        go_to_url("https://skillbox.ru/courses/?type=profession")
        with step(f'Выбор курса {profession_name}'):
            wait_element(By.XPATH,
                f"//a/descendant::span[contains(@class,'ui-tab__text f') and contains(text(), '{profession_name}')]")\
                .click()
        with step(f'Ожидание появления фильтра курса {profession_name}'):
            filter_blocks = wait_elements(
                By.XPATH, "//*[contains(@class, 'filter-block__direction')]/a/span")

        with step('Проверка кнопок фильтрации'):
            for actual_filter, expected_filter in zip(filter_blocks, filter_names):
                with step(f'Сравнение текущего текста "{actual_filter.text}" с ожидаемым {expected_filter}'):
                    assert actual_filter.text == expected_filter

        assert True
