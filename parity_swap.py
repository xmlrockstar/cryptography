import random
import string

message = "Hello, World!"

bin_1 = ''
bin_2 = ''

# def get_alphabet():

def encode(msg: str, quiet) -> list[str]:
    part1 = ''
    part2 = ''
    add_null_byte = False

    for i in range(0, len(msg)-1, 2):
        part1 += msg[i]
        part2 += msg[i+1]

    if len(msg) % 2 == 0:
        part2 += msg[-1]
    else:
        add_null_byte = True
        part1 += msg[-1]

    lower = string.ascii_letters
    spoof_msg = ''
    for i in range(len(msg)):
        rand = random.randint(0, 51)
        spoof_msg += lower[rand]

    binary_msg = ''.join(format(ord(i), '08b') for i in part1)
    binary_msg_2 = ''.join(format(ord(i), '08b') for i in part2)

    if add_null_byte:
        binary_msg_2 += '00111101'


    # xor both binaries

    final_binary = ''

    for i in range(len(binary_msg)):
        if binary_msg[i] == '1' and binary_msg_2[i] == '0':
            final_binary += '1'
        elif binary_msg[i] == '0' and binary_msg_2[i] == '1':
            final_binary += '1'
        else:
            final_binary += '0'

    bin_1 = binary_msg
    bin_2 = final_binary

    if quiet:
        print("msg p1: ", bin_1)
        print("msg p2: ", binary_msg_2)
        print("parity: ", final_binary)

    return [bin_1, bin_2]


def decode(binary_1: str, binary_2: str, quiet) -> str:
    un_xor_binary = ''

    for i in range(len(binary_1)):
        if binary_1[i] == '1' and binary_2[i] == '0':
            un_xor_binary += '1'
        elif binary_1[i] == '0' and binary_2[i] == '1':
            un_xor_binary += '1'
        else:
            un_xor_binary += '0'

    if quiet:
        print('arg1 (msg p1)         ', binary_1) 
        print('reconstructed (msg p2)', un_xor_binary)
        print('arg2 (xor)            ', binary_2)

    part1 = ''.join(chr(int(binary_1[i:i+8], +2)) for i in range(0, len(binary_1), 8))
    part2 = ''.join(chr(int(un_xor_binary[i:i+8], +2)) for i in range(0, len(un_xor_binary), 8))

    if quiet:
        print(part1)
        print(part2)
    
    final_msg = ''
    for i in range(0, len(part1)):
        final_msg+=part1[i]
        final_msg+=part2[i]

    if final_msg[-1] == '=':
        final_msg=final_msg[:-1]
        
    return(final_msg)

# encode(message)
# print('---')
# decode('01001000011011000110111100100000011011110110110000100001', '00101101000000000100001101110111000111010000100000011100')

def main(q=False):
    q = True if q else None
    
    inp1 = input("Enter message to be encoded: ")
    print(f'Encoding: {inp1}')
    bin_enc = encode(inp1, q)
    decoded = decode(bin_enc[0], bin_enc[1], q)
    print('Part: 2', bin_enc[1])
    print('Part: 1', bin_enc[0])
    print(f'Decoded: {decoded}')
    
