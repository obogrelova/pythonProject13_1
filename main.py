# Принимаем на вход строку и сохраняем ее в отдельную переменную.
# Передаем эту строку в качестве аргумента в рекурсивную функцию.
# Убеждаемся, что строка непустая.
# Приводим все символы строки к нижнему регистру с помощью метода lower().
# Удаляем пробелы и специальные символы.
# Сравниваем исходную строку с её зеркальным отражением.
# Делаем вывод и возвращаем результат.


def is_palindrome(s):
    if not s:
        return 'Это пустая строка.'
    
    s = s.lower()

    s = ''.join(c.lower() for c in s if c.isalnum())

    s_lower = s == s[::-1]

    if s_lower:
        return 'Это палиндром'
    else:
        return 'Это не палиндром'


print(is_palindrome(''))
print(is_palindrome('level'))