# cryptography

Different methods of encoding and decoding data
Uses:
  - math
  - preexisting encoding formats (binary, base64)
  - string manipulation
  - arrays

Current projects
1. 2d array multiplication table
2. parity swap 


2d array multiplication
  |- Uses ciphers and and secret keys to encode data, 3 pieces of data are needed to decode a message
      1. The message
      2. The secret key
      3. The cipher
  |- This means that you can share a cipher [~70 chars] between multiple people/groups but share a single secret key [1+ chars] with specific people for private messaging
  |- This also means the cipher is not sensitive information and does not NEED to be hidden but can be hidden to increase security

  parity swap
    |- Splits the message into two even strings and encodes them into binary
    |- XOR is operated on each bit of the two strings to produce a third
    |- Half of the original message gets removed so only half the message remains after encoding
    |- The other half can be recovered using the first half and the third new binary string by operating XOR on each bit
    |- From this they can be decoded to ascii and reconfigured into one string
