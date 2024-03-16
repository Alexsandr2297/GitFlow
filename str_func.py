def string():
    """Фунция переписывает в заглавные букв"""
    text = input().upper()
    print(text)


string()


def capitalize_words(string):
    """функция которая делает заглавные первые буквы каждого слова в строке"""
    words = string.split(" ")
    result = ""
    for word in words:
        word = word.capitalize()
        result += " " + word
    return result


string = "hello world"
print(capitalize_words(string))
