# Gregory Pereverzev 25.11.2019
# Создаем первые функции.

def search4vowels(phrase: str) -> set:
    """Возвращает гласные, найденные в указанной фразе."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase.lower()))


def search4letters(phrase: str, letters=str('aeiou')) -> set:
    # Аргументу letters присвоено значение по умолчанию.
    """Возвращает множество букв из letters, найденных в указанной фразе."""
    return set(letters.lower()).intersection(set(phrase.lower()))



