import random


def get_words():
    words_list = []
    with open('words.txt', mode='r', encoding='utf-8') as file:
        for line in file:
            words_list.append(line.strip().split(','))

    # print(*words_list, sep='\n')

    return words_list


def gen_tasks_list(count):
    words_list = get_words()
    indexes = list(range(len(words_list)))
    random.shuffle(indexes)
    indexes = indexes[:count]
    return [words_list[i_index] for i_index in indexes]


def main():
    wrong = 0
    print('hello pes')
    tasks_count = int(input('tasks: '))
    tasks = gen_tasks_list(tasks_count)

    # print(tasks)

    for word in tasks:
        print(word[0].upper())

        while True:
            ans = input('Какая часть речи? (сущ/прил/гл): ')
            if ans == word[1]:
                print('Верно!')
                break
            else:
                print('Не верно!')
                wrong += 1

        if word[2] != '-':
            while True:
                ans = input('Какой род? (м/ж/ср): ')
                if ans == word[2]:
                    print('Верно!')
                    break
                else:
                    print('Не верно!')
                    wrong += 1

        if word[3] != '-':
            while True:
                ans = input('Какое число? (ед/мн): ')
                if ans == word[3]:
                    print('Верно!')
                    break
                else:
                    print('Не верно!')
                    wrong += 1


if __name__ == ('__main__'):
    main()
