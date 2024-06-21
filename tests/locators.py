# В файл с локаторами добавил урлы для удобства
# локаторы для тестов страницы регистрации
signup_url = 'https://stellarburgers.nomoreparties.site/register' # URL страницы регистрации
signup_name_xpath = "//label[text()='Имя']/parent::div/input[@name='name']" # поле для имени
signup_email_xpath = "//label[text()='Email']/parent::div/input[@name='name']" # поле для почты
signup_pass_xpath = "//input[@type='password']" # поле для пароля
signup_signup_button_class = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']" # кнопка регистрации
signup_user_exist_error_class = "input__error text_type_main-default" # текст ошибки если пользователь уже существует
signup_pass_error_xpath = "//p[@class='input__error text_type_main-default']" # ошибка на невалидный пароль

# локаторы для тестов страницы логина
login_url = "https://stellarburgers.nomoreparties.site/login" # URL страницы логнина
login_forgot_pass_xpath = "//a[text()='Восстановить пароль']" # гиперссылка на восстановление пароля
login_email_xpath = "//input[@name='name']" # Поле для почты
login_pass_xpath = "//input[@name='Пароль']" # Поле для пароля
login_login_button_xpath = "//button[text()='Войти']" # Кнопка для входа
main_page_url = "https://stellarburgers.nomoreparties.site/" # URL главной страницы
main_page_login_xpath = "//button[text()='Войти в аккаунт']" # Кнопка входа на главной странице
main_page_account_login_xpath = "//p[text()='Личный Кабинет']" # Кнопка перехода в личный кабинет
main_page_checkout_xpath = "//button[text()='Оформить заказ']" # Кнопка оформления заказа
forgot_pass_url = "https://stellarburgers.nomoreparties.site/forgot-password" # URL страницы восстановления пароля
forgot_pass_login_link_xpath = "//a[text()='Войти']" # текст со ссылкой на страницу входа
signup_login_xpath = "//a[text()='Войти']" # текст со ссылкой на страницу входа

# локаторы для тестов аккаунта
profile_page_url = "https://stellarburgers.nomoreparties.site/account/profile" # URL Страницы профиля
profile_save_button_xpath = "//button[text()='Сохранить']" # кнопка сохранить в профиле
profile_logo_xpath = "//div[@class='AppHeader_header__logo__2D0X2']" # логотип вверху страницы
profile_main_page_button_xpath = "//p[text()='Конструктор']" # кнопка перехода на главную страницу
profile_logout_button_xpath = "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']" # кнопка выхода из профиля

# локаторы для тестов разделов конструктора
main_scroll_buns_xpath = "//span[text()='Булки']" # кнопка для перехода в раздел с булками
main_scroll_sauces_xpath = "//span[text()='Соусы']" # кнопка для перехода в раздел с соусами
main_scroll_fillings_xpath = "//span[text()='Начинки']" # кнопка для перехода в раздел с начинками