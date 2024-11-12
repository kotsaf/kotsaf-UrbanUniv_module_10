import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)


if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start1 = datetime.now()

    for i in filenames:
        read_info(i)

    end1 = datetime.now()
    line_time = end1 - start1
    print(line_time, '- линейный метод')

    start2 = datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end2 = datetime.now()
    process_time = end2 - start2
    print(process_time, '- многопроцессный метод')

'''Вывод'''
# 0:00:04.793544 - линейный метод
# 0:00:02.191502 - многопроцессный метод
