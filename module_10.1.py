import time  # Импорты необходимых модулей и функций
from threading import Thread
import time


def write_words(word_count: int, file_name: str):  # Объявление функции write_words
    count = 0
    file = open(file_name, 'a', encoding='utf-8')

    for line in range(word_count):
        count += 1
        file.write(f'Какое-то слово № {count}\n')
        time.sleep(0.1)

    file.close()
    print(f"Завершилась запись в файл {file_name}")


time1 = time.time()  # Взятие текущего времени

write_words(10, 'example1.txt') # Запуск функций с аргументами из задачи
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time2 = time.time()  # Взятие текущего времени
func_work_time = time2 - time1  # Вывод разницы начала и конца работы функций
print(f'Время работы функций {func_work_time}')

time3 = time.time()  # Взятие текущего времени

thr_first = Thread(target=write_words, args=(10, 'example5.txt'))  # Создание и запуск потоков с аргументами из задачи
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()  # старт потока
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()  # ожидание ответа
thr_second.join()
thr_third.join()
thr_fourth.join()

time4 = time.time()  # Взятие текущего времени
stream_work_time = time4 - time3  # Вывод разницы начала и конца работы потоков
print(f'Время работы потоков {stream_work_time}')



print(f'Использование Потоков быстрее функций на {stream_work_time - func_work_time} секунд')