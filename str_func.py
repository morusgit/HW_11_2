def upper_case(string):
    """
    функция, которая принимает на вход строку и возвращает ее со всеми заглавными буквами
    """
    return string.upper()

def upper_first_letters(string):
    """
    принимает строку на вход
    заменяет первые буквы каждого слова в строке на заглавные
    """
    words = string.split()
    upper_words = []
    for word in words:
        upper_word = word[1:] + word[0].upper()
        upper_words.append(upper_word)
    return ' '.join(upper_words)
  