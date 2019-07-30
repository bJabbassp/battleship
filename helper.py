def letter_to_integer(letter):
    table = str.maketrans('ABCDEFGHIJ', '0123456789')
    return int(letter.translate(table))
