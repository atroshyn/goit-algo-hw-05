# Задамо тексти статтей
text1 = """
ВИКОРИСТАННЯ АЛГОРИТМІВ У БІБЛІОТЕКАХ МОВ ПРОГРАМУВАННЯ
Автори публiкації: Коваленко О.О., Корягіна Д.О. Вінницький національний технічний університет
Анотація: У данній статті було розглянуто використання алгоритмів у бібліотеках мов програмування. Ключові слова: алгоритми, сортування, лінійний пошук, двійковий пошук, пошук стрибками, інтерполяційний пошук, експоненціальний пошук, жадібний алгоритм.
Стаття
За всю історію комп'ютерних наук склалося розуміння, які алгоритми та структури даних (способи їх зберігання) потрібні для вирішення практичних завдань, певний набір, який повинен знати кожен розробник. Наприклад, сортування: товари в магазині сортують за вартістю або терміну придатності, а ресторани – за віддаленістю або рейтингу. Хеш-таблиці допомагають перевірити коректність пароля та не зберігати його на сайті у відкритому вигляді, графи – знаходити найкоротший шлях і зберігати зв'язки між користувачами в соцмережах.
Алгоритми – це послідовність точно визначених дій, які призводять до вирішення поставленої задачі чи певного завдання і на сьогодні уже створено величезну кількість алгоритмів для вирішення важких задач, що полегшують написання коду будь-якому програмісту, особливо початківцям [1].
Метою роботи є виявлення найбільш популярних алгоритмів у бібліотеках мов програмування.
Усі алгоритми та структури даних вже давно реалізовані в бібліотеках популярних мов програмування. Більше ніхто не пише вручну алгоритм сортування чисел, а щоб користуватися хеш-таблицями, навіть не потрібно знати, як вони влаштовані.
Але наявність безлічі готових бібліотек не означає, що не потрібно розуміти, як влаштовані алгоритми. Фундаментальні знання допомагають дізнатися, що всередині, як воно працює і чому одне рішення краще, аніж інше у конкретній ситуації. Якщо зрозуміти, як влаштовані класичні алгоритми, то можна створювати власні рішення, комбінувати методи один з одним, щоб вирішувати більш складні завдання.
У програмуванні стандартна бібліотека — це бібліотека, що доступна в усіх реалізаціях даної мови програмування. Зміст такої бібліотеки зазвичай описано у специфікації мови, однак також він може частково або повністю визначатися більш неформальними практиками програмістів, що користуються нею. Більшість стандартних бібліотек включають у себе визначення принаймні таких найчастіше використовуваних інструментів як:
Алгоритми (такі як алгоритми сортування); 
Структури даних (наприклад, списки, дерева, хеш-таблиці); 
Взаємодія з відповідною платформою (введення-виведення, системні виклики та ін.). 
Пошук – поширена дія, яка виконується в бізнес-додатках. Розглянемо деякі реалізації відомих алгоритмів пошуку [2] на Java.
Лінійний або послідовний пошук – найпростіший алгоритм пошуку. Він рідко використовується через свою неефективність. По суті, це метод повного перебору, і він поступається іншим алгоритмам [3]. У лінійного пошуку немає передумов до стану структури даних. Алгоритм шукає елемент у заданій структурі даних, поки не досягне кінця структури. При знаходженні елемента повертається його позиція у структурі даних. Якщо елемент не знайдений, повертаємо -1. Лінійний пошук можна використовувати для малого, несортоване набору даних, який не збільшується в розмірах...
"""

text2 = """
Методи та структури даних для реалізації бази даних рекомендаційної системи соціальної мережі
Автори публiкації: Міхав В.В., Мелешко Є.В., Шимко С.В. Центральноукраїнський національний технічний університет,
Анотація
Метою даної роботи є дослідження та програмна реалізація методів і структур даних для побудови бази даних рекомендаційної системи, щоб порівняти ефективність їх використання за затратами часу та пам’яті. Наявність великої кількості різних методів реалізації баз даних викликає необхідність порівняльного аналізу та вибору оптимального методу і структури даних для зберігання інформації у рекомендаційних системах.
Було проведено дослідження різних структур даних, які можна використати для створення бази даних рекомендаційної системи, зокрема, досліджені зв’язний список, розгорнутий зв’язний список, хеш-таблиця, B-дерево, B+-дерево та бінарна діаграма рішень. Також було проведено серію експериментів на програмній імітаційній моделі рекомендаційної системи з різною кількістю агентів, предметів та сесій.
Відповідно до результатів проведених експериментів, розгорнутий список показав найкращі показники швидкодії та використання пам’яті. Структура B+-дерево показала результати, близькі до хеш-таблиці. Час доступу до окремого елементу в обох випадках сталий, але B+- дерево має певні переваги – елементи зберігаються відсортованими, а при зміні розміру немає необхідності розширювати область пам’яті. Найгірші результати показала структура даних бінарна діаграма рішень як за затратами часу, так і за затратами пам’яті. Профілювання показало, що 75% часу роботи тесту варіанту з розгорнутим списком зайняло генерування випадкових даних для програмного імітаційного моделювання агентів та предметів рекомендаційної системи, тож, саме сховище даних має високі показники ефективності.
Профілювання варіанту із інвертованим списком показало, що доступ до випадкових блоків займає більше часу через неможливість закешувати їх, тож, за умов реального навантаження час вставки нових даних буде більшим, а відносна ефективність застосування інвертованого списку зросте. Для найбільш ефективного використання пам’яті розмір блоку зв’язного списку має бути адаптований таким чином, щоб блоки були максимально заповнені. Блоки малого розміру зменшують втрати пам’яті, але збільшують час обходу всіх елементів списку та збільшують накладні витрати пам’яті.
Ключові слова: рекомендаційні системи, бази даних, структури даних, програмна імітаційна модель.
Стаття
Постановка проблеми. Рекомендаційні системи є важливою складовою соціальних мереж та значним чином впливають на те, яким користувачі сприймають інформаційний простір [1, 2]. Вибір методу представлення даних, якими оперує рекомендаційна система, має важливе значення, оскільки фективний спосіб побудови бази даних для роботи такої системи може зменшити кількість потрібних ресурсів та збільшити кількість доступних алгоритмів для формування списків рекомендацій. Отже, вибір методів реалізації СУБД для зберігання даних рекомендаційної системи є важливою науково-практичною задачею...

"""

import timeit

# Реалізація алгоритму Боєра-Мура
def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0
    char_table = make_char_table(pattern)
    offset_table = make_offset_table(pattern)
    i = m - 1
    while i < n:
        j = m - 1
        while pattern[j] == text[i]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += max(offset_table[m - 1 - j], char_table.get(text[i], m))
    return -1

def make_char_table(pattern):
    table = {}
    for i in range(len(pattern) - 1):
        table[pattern[i]] = len(pattern) - 1 - i
    return table

def make_offset_table(pattern):
    table = []
    last_prefix_position = len(pattern)
    for i in range(len(pattern) - 1, -1, -1):
        if is_prefix(pattern, i + 1):
            last_prefix_position = i + 1
        table.append(last_prefix_position - i + len(pattern) - 1)
    for i in range(len(pattern) - 1):
        slen = suffix_length(pattern, i)
        table[slen] = len(pattern) - 1 - i + slen
    return table

def is_prefix(pattern, p):
    j = 0
    for i in range(p, len(pattern)):
        if pattern[i] != pattern[j]:
            return False
        j += 1
    return True

def suffix_length(pattern, p):
    length = 0
    j = len(pattern) - 1
    i = p
    while i >= 0 and pattern[i] == pattern[j]:
        length += 1
        i -= 1
        j -= 1
    return length

# Реалізація алгоритму Кнута-Морріса-Пратта
def knuth_morris_pratt(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Реалізація алгоритму Рабіна-Карпа
def rabin_karp(text, pattern, d=256, q=101):
    M = len(pattern)
    N = len(text)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for text
    h = 1

    for i in range(M-1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(N - M + 1):
        if p == t:
            for j in range(M):
                if text[i + j] != pattern[j]:
                    break
            else:
                return i
        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t = t + q
    return -1


# Вибір підрядків для пошуку
existing_substring = "алгоритм"
fake_substring = "мирне небо"

# Функція для вимірювання часу виконання
def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=10)

# Вимірюємо час для кожного алгоритму
results = {}
for text, label in [(text1, "Text1"), (text2, "Text2")]:
    results[label] = {}
    for algorithm, func in [("Boyer-Moore", boyer_moore_search),
                            ("Knuth-Morris-Pratt", knuth_morris_pratt),
                            ("Rabin-Karp", rabin_karp)]:
        results[label][algorithm] = {
            "existing": measure_time(func, text, existing_substring),
            "fake": measure_time(func, text, fake_substring)
        }
# Виводимо результати
results
