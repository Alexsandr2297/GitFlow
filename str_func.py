def string():
    """Функция переписывает в заглавные буквы"""
    text = input().upper()
    print(text)


string()


def word_str(string):
    """ функция которая делает заглавные первые буквы каждого слова в строке """
    words = string.split(" ")
    result = ""
    for word in words:
        word = word.capitalize()
        result += " " + word

    return result


string = "hello world"
print(word_str(string))