# alice

# new_list = []

# with open('words_alice.txt', mode='r', encoding='utf-8') as file:
#     for line in file:
#         new_line = line[1:-2].replace(' ', '').strip().split('|')
#         if new_line[2] == 'Множественное':
#             new_line[2] = '-'
#         print(str(new_line))
#         new_list.append(new_line)


# with open('new_alice.txt', mode='w', encoding='utf-8') as file:
#     for item in new_list:
#         file.write(str(item))
#         file.write('\n') 

#gpt

new_list = []

with open('words_gpt.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        new_line = line[1:-2].replace(' ', '').strip().split('|')

        print(str(new_line))
        new_list.append(new_line)


with open('new_gpt.txt', mode='w', encoding='utf-8') as file:
    for item in new_list:
        file.write(str(item))
        file.write('\n') 

#giga

# new_list = []

# with open('words_giga.txt', mode='r', encoding='utf-8') as file:
#     for line in file:
#         new_line = line.strip().split(' ')
#         print(new_line[1:])
#         new_list.append(new_line)

# with open('new_giga.txt', mode='w', encoding='utf-8') as file:
#     for item in new_list:
#         file.write(str(item[1:]))
#         file.write('\n') 