"""
Задача 2.

Дано файл, що містить слова, записані на окремих рядках. Слова можуть повторюватися.
Надрукуйте з файлу список слів на основі першого символу слова в лексикографічному
порядку у вигляді як у вихідних даних.
Вхідні дані:
Файл input.txt з текстом
Вихідні дані:
a: ask
b: be
c: come call
d: do
f: find feel
g: get go give
h: have
k: know
l: look leave
m: make
s: say see seem
t: take think tell
u: use
w: want work

Автор: Новосад Сніжана
"""


#Відкиваємо файл для читання
with open('input.txt', 'r') as file:
    # Читаємо всі рядки з файлу
    lines = file.readlines()

# Ініціалізуємо словник для зберігання слів за першими буквами
word_dict = {}

# Обробляємо кожен рядок з файлу
for line in lines:
    # Розділяємо слова за пробіли
    words = line.split()

    # Додаємо слова до словника за першими буквами
    for word in words:
        first_letter = word[0].lower()  # Використовуємо lower() для ігнорування регістру
        if first_letter in word_dict:
            word_dict[first_letter].append(word)
        else:
            word_dict[first_letter] = [word]

# Сортуємо словник за ключами (першими буквами) в лексикографічному порядку
sorted_word_dict = sorted(word_dict.items())

# Виводимо відсортований список слів у потрібному форматі
for letter, words in sorted_word_dict:
    print(f"{letter}: {' '.join(words)}")

    
