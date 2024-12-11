#Кнопка "Войти в аккаунт" на главной странице
from copyreg import constructor

sign_in_button = './/button[text()="Войти в аккаунт"]'

#Кнопка "Оформить заказ" на главной странице
set_an_order_button = './/section[2]//button'

#Кнопка "Личный Кабинет" на главной странице
account_button = './/header//p[text()="Личный Кабинет"]'

#Заголовок "Соберите бургер" на главной странице
title_on_main_page = './/section[1]//h1'

#Кнопка "Конструктор"
constructor_button = './/header//ul//p[text()="Конструктор"]'

#Вкладка "Булки"
bun_tab_on_main_page = './/main//section[1]//div[1]//div[1]//span[text()="Булки"]'

#Заголовок "Булки" во вкладке "Булки"
bun_header_on_main_page = './/section[1]//div[2]//h2[1]'

#Вкладка "Соусы"
sauce_tab_on_main_page = './/main//section[1]//div[1]//div[2]//span[text()="Соусы"]'

#Заголовок "Соусы" во вкладке "Соусы"
sauce_header_on_main_page = './/section[1]//div[2]//h2[2]'

#Вкладка "Начинки"
fillings_tab_on_main_page = './/main//section[1]//div[1]//div[3]//span[text()="Начинки"]'

#Заголовок "Начинки" во вкладке "Начинки"
fillings_header_on_main_page = './/section[1]//div[2]//h2[3]'