vowels = {'a','e','i','o','u'}
word = raw_input("""
PIG LATEN TRANSLATOR

ENTER A WORD TO PIG LATINIFY IT

""").lower()


if len(word) > 0 and word.isalpha():
    i = 0
    for char in word:
        for vowel in vowels:
            if char == vowel:
                break           # This breaks the loop when it hits the first up
        else:
            i += 1
            continue
        break

    if word[0:2] == "qu":
        i = 2

    if i == 0:
        new_word = word + "way"
    else:
        first = word[0:i]
        new_word = word[i:len(word)] + first + "ay"

    print """
        %s
        """ % (new_word)
else:
    print "ONLY A SINGLE REAL WORD WORKS"
