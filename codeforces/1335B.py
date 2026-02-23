t = int(input())

for _ in range(t):
    results = []
    n, a, b = map(int, input().split())

    # Строим строку длины n
    # Символ на позиции i определяется как i % b
    # Это обеспечивает циклическое повторение первых b букв
    s = []
    for i in range(n):
        # ord('a') дает код символа 'a'.
        # Прибавляем остаток от деления i на b, чтобы циклически менять буквы.
        char_code = ord('a') + (i % b)
        s.append(chr(char_code))

    results.append("".join(s))

    # Выводим все ответы
    print("\n".join(results))