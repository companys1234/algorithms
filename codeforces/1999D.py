t = int(input())
for _ in range(t):
    s1 = str(input())
    s2 = str(input())
    min_raz = 10 ** 9
    n = len(s2)
    p = 0
    z = 0
    d = True

    # Преобразуем s1 в список для изменения символов
    s1_list = list(s1)

    # Жадно ищем символы s2 в s1 по порядку (подпоследовательность)
    ptr = 0
    for i in range(len(s1_list)):
        if ptr < n:
            if s1_list[i] == '?' or s1_list[i] == s2[ptr]:
                if s1_list[i] == '?':
                    s1_list[i] = s2[ptr]
                    p += 1
                ptr += 1

    # Заменяем оставшиеся '?' на 'a'
    for i in range(len(s1_list)):
        if s1_list[i] == '?':
            s1_list[i] = 'a'
            z += 1

    # Проверяем, нашли ли всю строку s2
    if ptr == n:
        print('YES')
        print(''.join(s1_list))
    else:
        print('NO')