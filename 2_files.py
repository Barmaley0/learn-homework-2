"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open(file="referat.txt", mode="r", encoding="utf-8") as text:
        my_text = text.read()
        print(f"Количество слов в тексте: {len(my_text.split())}.")
        print(f"Длинна строки: {len(my_text)} символа.")
    with open(file="referat2.txt", mode="w", encoding="utf-8") as text_rec:
        text_rep = my_text.replace(".", "!")
        text_rec.write(text_rep)

if __name__ == "__main__":
    main()
