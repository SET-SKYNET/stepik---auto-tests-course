import time

# webdriver це і є набір команд для керування браузером
from selenium import webdriver

# ініціюємо драйвер браузера. Після цієї команди ви повинні побачити нове відкрите вікно браузера
driver = webdriver.Chrome()

# команда time.sleep встановлює паузу у 5 секунд, щоб ми встигли побачити, що відбувається в браузері
time.sleep(5)

# Метод get повідомляє браузеру, що потрібно відкрити сайт за вказаним посиланням
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Метод find_element_by_css_selector дозволяє знайти потрібний елемент на сайті, вказавши шлях до нього.
# Способи пошуку елементів ми обсудимо пізніше
# Шукаємо поле для вводу тексту
textarea = driver.find_element_by_css_selector(".textarea")

# Пишемо текст відповіді у знайдене поле
textarea.send_keys("get()")
time.sleep(5)

# Знайдемо кнопку, котра відправляє введене рішення
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Скажемо драйверу, що потрібно натиснути на кнопку.
# Після цієї команди ми повинні побачити повідомлення про правильну відповідь
submit_button.click()
time.sleep(5)

# Після вивиконання усіх дій ми повинні закрити вікно браузера
driver.quit()
