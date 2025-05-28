"""Takes the input and translates it to integers, changing each letter to its corresponssing index in the cipher
        - cipher is generated with a shuffled alphabet (fisher yates shuffle) and translated to an array of their indexes
    the numbered input is added to the top line of an array preceeded by a placeholder ('X')
    the entire array has dimensions of len(input)+1 by len(input)+1
    the top line of the array (bar placeholder) is multiplied by the secret_key 'sk' which is determined by the user
    the multiplied array is then iterated downwards to the bottom of the array, each line starting with the secret key (it look like a multiplication table)
    
    Example: input of "Hello"  - uses a random cipher i used for development
    ^-- length of message is 5
       ^-- array dimensions are 6 x 6 
    [
                           [X, 33, 6, 48, 48, 9] <-- unmultiplied translation of the user input
        --> secret key (7) [7, 231, 42, 336, 336, 63]
                           [7, 231, 42, 336, 336, 63]
                           [7, 231, 42, 336, 336, 63]
                           [7, 231, 42, 336, 336, 63]
                           [7, 231, 42, 336, 336, 63]
    ]
    the numbers of the array are added diagonally using the indexes, you dont actually use all numbers because the sequence repeats
    [
                           [X, 33, 6, 48, 48, 9]
                           [7, 33 , 42, 336, 336, 63] final index - 63                           | 63
                           [7,  X , 42, 336, 336, 63] final 2 indexes - 336 + 63                 | 399
                           [7,  X,  X , 336, 336, 63] final 3 indexes - 336 + 336 + 63           | 735
                           [7,  X ,  X,  X , 336, 63] final 4 indexes - 336 + 336 + 63 + 42      | 777
                           [7,  X ,  X,  X ,  X , 63] final 5 indexes - 33 + 42 + 336 + 336 + 63 | 1008
                            
                           these sums then go into an array
                           ^-- [63, 399, 735, 777, 1008]
                               ^-- A '§' is added to indentify breaks between words
                                  ^-- This is our final encoded message
                                  |
                                  |-- 63§399§735§777§1008

                            The decoding just reverses all of this
                            
                            The encoding and decoding functions all except 3 arguments
                            ^-- message, secret_key, cipher
                            |-- without these the message is unintelligible
    ]
    """

import string
import random

def get_alphabet() -> list[str]:
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_higher = list(string.ascii_uppercase)

    alphabet = []
    for i in range(26):
        alphabet.append(alphabet_lower[i])
        alphabet.append(alphabet_higher[i])
    
    alphabet.extend(string.punctuation)
    alphabet.append(' ')
    return alphabet

def shuffle_to_cipher(arr: list[str]) -> list[str]: # fisher yates shuffle
    for i in range(len(arr) -1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

alphabet = get_alphabet()
cipher = shuffle_to_cipher(alphabet)

test_msg = "Hello"
test_secret_key = 7

cipher1 = ''

def encode(msg: str, sk: int, cipher: list[str]) -> str:
    #get encoded using index of cipher 
    encoded = []

    split_msg = [char for char in msg]
    for char in split_msg:
        if cipher.__contains__(char):
            encoded.append(cipher.index(char))
            print(encoded)
        else:
            encoded.append("!")
            encoded.append(char)
            encoded.append("!")
            print("This character is not allowed", char)
            print("§ is NEVER allowed")
            print("Please type numbers: e.g. one, twelve")
            exit(1)


    #iterate downwards
    multiplied = [num * sk for num in encoded]
    #--construct array
    grid = []

    for _ in range(len(msg)):
        grid.append(multiplied)

    sums = []

    width = len(grid[0])

    for i in range(width):
        total = 0
        for j in range(i + 1):
            row = width - 1 - j
            col = width - 1 - j
            total += grid[row][col]
        sums.append(total)

    final = ""
    for i in range(len(sums)):
        final += (str(sums[i]))
        if i == len(sums)-1:
            break
        else:
            final += ('§')

    return final

def decode(enc: str, sk: int, cipher: list[str]) -> str:
    enc_split = enc.split("§")

    enc_int = list(map(int, enc_split))
    row = []
    row.append(enc_int[0])
    length = len(enc_int)

    for i in range(len(enc_int)-1):
        row.append(enc_int[i+1] - enc_int[i])

    row.reverse()
    divided = []

    for num in row:
        divided.append(int(num / sk))

    decoded = ""

    for char in divided:
        decoded += (cipher[char])

    return decoded

# decode(encode(test_msg, test_secret_key, test_cipher), test_secret_key)

def keygen() -> list[str]:
    al1 = get_alphabet()
    cipher1 = shuffle_to_cipher(al1)
    return cipher1
    
def default_keygen():
    default_cipher = ['F', '+', 'G', "'", ' ', 'r', '}', '~', 'o', '_', 'E', 'O', '.', 'a', 'g', 'P', 'h', 'U', '^', 'V', 'w', 'x', '*', '=', 'd', 'H', '(', '[', 'y', 'J', '@', 'i', 'n', ';', ']', 'b', 'R', '"', 'N', '{', '%', 't', '#', 'c', 'f', 'p', 'k', '\\', '&', 'z', 'C', '$', ',', 'K', '|', '-', 'I', 'W', 'X', '/', 'j', '<', 'L', 'A', '?', '`', 'm', 'Z', 'S', 'Q', 'u', 'l', 's', '!', ')', 'e', 'q', 'M', 'B', 'T', 'D', 'v', '>', 'Y', ':']
    return default_cipher    
