def char_in_range(ch1, ch2):
    result = []
    for i in range(ord(ch1) + 1, ord(ch2)):
        result.append(chr(i))
    print(" ".join(result))


word1 = input()
word2 = input()

char_in_range(word1, word2)
