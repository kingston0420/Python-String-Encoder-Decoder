alphabet = 'abcdefghijklmnopqrstuvwxyz'
def coder(sentence, offset):
    encode = ''
    for word in sentence:
        index = alphabet.find(word)
        if index==-1:
            encode = encode + word
        else: 
            encode = encode + alphabet[(index+26-offset)%26]
    return encode
message = 'hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!'
answer = coder(message, 10) 
print(answer)