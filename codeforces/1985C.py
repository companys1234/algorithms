import sys


def solve():
    # Читаем весь вход сразу (это намного быстрее input())
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    iterator = iter(input_data)
    t = int(next(iterator))

    results = []

    for _ in range(t):
        n = int(next(iterator))

        current_sum = 0
        current_max = -float('inf')  # Инициализируем минимальным значением
        count = 0

        # Проходим по элементам массива, не создавая срезов
        for _ in range(n):
            val = int(next(iterator))

            current_sum += val
            if val > current_max:
                current_max = val

            # Проверяем оптимизированное условие
            if 2 * current_max == current_sum:
                count += 1

        results.append(str(count))

    # Выводим все результаты разом
    sys.stdout.write('\n'.join(results) + '\n')


if __name__ == '__main__':
    solve()