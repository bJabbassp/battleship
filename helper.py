def letter_to_integer(letter):
    table = str.maketrans('ABCDEFGHIJ', '0123456789')
    return int(letter.translate(table))

def parse_coordinates(coordinates):
    try:
        letter_position, x = coordinates.split(',')
        y = letter_to_integer(letter_position)
        x = int(x)
    except:
        return False

    return x, y
