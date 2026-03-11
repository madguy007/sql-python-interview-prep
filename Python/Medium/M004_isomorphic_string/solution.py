s = input()
t = input()

def word_dict(word):
    dic = dict()

    for letter in word:
        if letter not in dic:
            dic[letter] = 0
        dic[letter] += 1

    return list(dic.values())


if word_dict(s) == word_dict(t):
    print(True)
else:
    print(False)