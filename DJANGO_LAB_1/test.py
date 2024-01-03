from django.contrib.auth.hashers import check_password

password = "cfiflbvfybrbnf"
hashed_password = "pbkdf2_sha256$600000$8kGMMKWRPL7yZXMrtibRbf$zZodziwhh/CjAxP7hre7ee6YBncKGPYQmYi63WtRyM4="

# Перевірка пароля на співпадіння
result = check_password(password, hashed_password)

if result:
    print("Пароль вірний.")
else:
    print("Пароль невірний.")