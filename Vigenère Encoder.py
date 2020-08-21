alphabet = 'abcdefghijklmnopqrstuvwxyz'
message = 'you were able to decode this? nice work! you are becoming quite the expert at crytography!'
def vigenere_encoder(message, keyword):
    final_keyword = ''
    keyword_index = 0
    for i in range(len(message)):
        index = alphabet.find(message[i])
        if index==-1:
            final_keyword += message[i]
        else: 
            final_keyword += keyword[keyword_index%len(keyword)]
            keyword_index += 1
    encode_message = ''
    shift = 0
    for i in range(len(message)):
        index = alphabet.find(message[i])
        if index==-1:
            encode_message += message[i]
        else:
            shift = alphabet.find(final_keyword[i])
            encode_message += alphabet[(index+shift)%26]
    return encode_message

final_message = vigenere_encoder(message, 'friends')
print(final_message)