import config_files.data_generator as dg

base_url = 'https://stellarburgers.nomoreparties.site'
url_registration = f'{base_url}/register'
url_authorization = f'{base_url}/login'
url_password_recovery = f'{base_url}/forgot-password'

username = 'Павел'
sign_in_email = 'lopukhovpavel16999@gmail.com'
sign_in_password = '123456'
sign_up_email = dg.email
sign_up_password = dg.new_password
incorrect_password = '111'
