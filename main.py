def main():
    book_path = "books/frankenstein.txt"
    book_contents = getBook(book_path)
    word_count = getWordCount(book_contents)
    char_count = getCharCount(book_contents)
    char_list = splitCharsList(char_count)
    char_list.sort(key=sortKey, reverse=True)

    print(f"Report of {book_path}")
    print("--------------------------------------------------")
    print(f"Word count: {word_count}")
    print()
    printCharacters(char_list)


def getBook(path):
    with open(path) as f:
        text = f.read()
        return text

def getWordCount(string):
    list = string.split()
    count = len(list)
    return count

def getCharCount(string):
    string = string.lower()
    dict = {}
    for c in string:
        if c.isalpha():
            if c in dict:
                dict[c] += 1
            else:
                dict[c] =1
    return dict

def splitCharsList(dict):
    list = []
    for k in dict:
        temp_dict = { "letter" : k, "count" : dict[k]}
        list.append(temp_dict)
    return list

def sortKey(dict):
    return dict["count"]

def printCharacters(list):
    for i in list:
        print(f"The '{i["letter"]}' character was found {i["count"]} times")


main()