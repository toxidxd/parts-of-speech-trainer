import random
import csv


def get_words():
    words_list = []
    with open('words.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for line in reader:
            words_list.append(line)

    return words_list


def gen_tasks_list(count):
    words_list = get_words()
    indexes = list(range(len(words_list)))
    random.shuffle(indexes)
    indexes = indexes[:count]

    return [words_list[i_index] for i_index in indexes]


def testing(tasks_count):
    mistakes = 0
    tasks = gen_tasks_list(tasks_count)

    for count, word in enumerate(tasks):
        print(f'{count+1}) {word[0].upper()}')

        while True:
            ans = input('Какая часть речи? (сущ/прил/гл): ')

            if ans == word[1]:
                # print('Верно!')
                break
            else:
                print('Не верно!')
                mistakes += 1

        if word[2] != '-':
            while True:
                ans = input('Какой род? (м/ж/ср): ')
                if ans == word[2]:
                    # print('Верно!')
                    break
                else:
                    print('Не верно!')
                    mistakes += 1

        if word[3] != '-':
            while True:
                ans = input('Какое число? (ед/мн): ')
                if ans == word[3]:
                    # print('Верно!')
                    break
                else:
                    print('Не верно!')
                    mistakes += 1

    print(f'Количество ошибок: {mistakes}')
    return mistakes


def main():
    all_mistakes = 0
    print('Привет!')
    tasks_count = int(input('Введи количество заданий: '))

    all_mistakes += testing(tasks_count)

    if all_mistakes == 0:
        print('Ты молодец!')
    else:
        print(f'Дополнительные задания: {all_mistakes}')
        all_mistakes += testing(all_mistakes)

        print(f'Ты балбес! Количество ошибок: {all_mistakes}.')
        print('Постарайся лучше в следующий раз!')

    print('Пока!')
    input('Нажми Enter, чтобы выйти...')


if __name__ == ('__main__'):
    main()
