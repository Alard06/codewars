def alphabet_position(text):
    alf = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    output = ''
    for letter in text:
        index = alf.find(letter) + 1
        if index > 0:
            output += f'{alf.find(letter) + 1} '
    output = output[:-1]
    return output

print(alphabet_position("The sunset sets at twelve o' clock."))
