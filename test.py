def solve_insertion_sort():
    # Чтение данных из файла input.txt
    try:
        with open('rosalind_ins.txt', 'r') as f:
            n = int(f.readline().strip())
            # Читаем все числа, на случай если они на нескольких строках
            a = []
            for line in f:
                a.extend(map(int, line.split()))
    except FileNotFoundError:
        print("Файл input.txt не найден")
        return

    swaps = 0
    # Реализация алгоритма согласно псевдокоду
    # В Python индексы начинаются с 0, поэтому идем от 1 до n-1
    for i in range(1, n):
        k = i
        # Пока текущий элемент меньше предыдущего — меняем их местами
        while k > 0 and a[k] < a[k - 1]:
            a[k], a[k - 1] = a[k - 1], a[k]
            swaps += 1
            k -= 1
            
    print(swaps)

if __name__ == "__main__":
    solve_insertion_sort()