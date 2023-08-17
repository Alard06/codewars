def duplicate_encode(word):
    output = ''
    word = word.lower()
    for letter in word:
        if word.count(letter) > 1:
            output += ')'
        else:
            output += '('
    return output

print(duplicate_encode('Success'))