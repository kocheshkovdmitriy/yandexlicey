'''
Напишите программу для поиска критериев “настоящести”. Найдите символы, которые чаще всего стоят до или после символа R
(real). Если таких несколько, то выведите все в алфавитном порядке без пробелов.

Формат ввода
В файле fake.txt записаны буквы латинского алфавита в верхнем регистре.

Формат вывода
Выведите символ (символы), как описано в условии.
'''

with open('fake.txt', 'r', encoding='utf-8') as f:
    data = f.read().strip()

cnt_let = dict() # key -> let(str), value -> cnt(int)

for index, let in enumerate(data):
    if let == 'R':
        if index > 0:
            cnt_let[data[index - 1]] = cnt_let.get(data[index - 1], 0) + 1
        if index < len(data) - 1:
            cnt_let[data[index + 1]] = cnt_let.get(data[index + 1], 0) + 1

rev_cnt = dict()
for key, value in cnt_let.items():
    rev_cnt[value] = rev_cnt.get(value, []) + [key]

print(''.join(sorted(rev_cnt[max(rev_cnt.keys())])))

max_cnt = max(cnt_let.values())
res = sorted([key for key in cnt_let if cnt_let[key] == max_cnt])
print(''.join(res))