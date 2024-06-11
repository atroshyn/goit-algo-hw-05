class HashTable:
    """
    Реалізація хеш-таблиці in Python.

    Атрибути:
        size: Розмір хеш-таблиці.
        table: Список, що представляє хеш-таблицю. Кожен елемент списку - це список пар (ключ, значення) для певного індексу хешування.
    """

    def __init__(self, size):
        """
        Ініціалізація хеш-таблиці.

        Args:
            size: Розмір хеш-таблиці.
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        """
        Функція хешування для ключів.

        Args:
            key: Ключ для хешування.

        Returns:
            Індекс у хеш-таблиці, отриманий за допомогою вбудованої функції hash(key) та операції mod розміром хеш-таблиці.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Вставка пари (ключ, значення) в хеш-таблицю.

        Args:
            key: Ключ для пари.
            value: Значення для пари.

        Returns:
            True - якщо пара успішно вставлена, False - якщо ключ вже існує.
        """
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if not self.table[key_hash]:
            self.table[key_hash] = [key_value]
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value  # Оновити значення, якщо ключ вже існує
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        """
        Отримання значення за ключем.

        Args:
            key: Ключ для пошуку.

        Returns:
            Значення пари (ключ, значення), якщо ключ знайдено, None - якщо ключ не знайдено.
        """
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        """
        Видалення пари (ключ, значення) з хеш-таблиці.

        Args:
            key: Ключ для видалення.

        Returns:
            True - якщо пару успішно видалено, False - якщо ключ не знайдено.
        """
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for i in range(len(self.table[key_hash])):
                if self.table[key_hash][i][0] == key:
                    del self.table[key_hash][i]
                    return True
        return False

# Тест хеш-таблиці

H = HashTable(5)
H.insert("книга", 100)
H.insert("телефон", 500)
H.insert("комп'ютер", 1500)

print(H.get("книга"))  # Виводить: 100
print(H.get("телефон"))  # Виводить: 500
print(H.get("комп'ютер"))  # Виводить: 1500

H.delete("комп'ютер")
print(H.get("комп'ютер"))  # Виводить: None

H.insert("стіл", 200)
print(H.get("стіл"))  # Виводить: 200
