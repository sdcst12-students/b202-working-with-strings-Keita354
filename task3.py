#!python3
'''
##### Task 3
Split a string into 2 halves and insert a line break in the middle.  If doing so cuts a word in half, add a dash to the first line.  You will need to make use of the

len(str) function
this function returns the length of the string

(2 points)
'''

def split(input_str):
    length = len(input_str)
    middle = length // 2
    first_half = input_str[:middle]
    second_half = input_str[middle:]
    if input_str[middle - 1] != ' ' and input_str[middle] != ' ':
        first_half += '-'
    result = first_half + '\n' + second_half

    return result

if __name__ == "__main__":
    sentence = "There is a big balloon in the blue sky"
    assert split(sentence) == "There is a big ball-\noon in the blue sky"

    sentence = "I am a fat cat"
    assert split(sentence) == "I am a \nfat cat"

    sentence = "I was a fat cat"
    assert split(sentence) == "I was a\n fat cat"