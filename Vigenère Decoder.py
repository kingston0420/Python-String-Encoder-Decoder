alphabet = 'abcdefghijklmnopqrstuvwxyz'
message = 'dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!'
def vigenere_decoder(message, keyword):
    final_keyword = ''
    keyword_index = 0
    for i in range(len(message)):
        index = alphabet.find(message[i])
        if index==-1:
            final_keyword += message[i]
        else: 
            final_keyword += keyword[keyword_index%len(keyword)]
            keyword_index += 1
    decode_message = ''
    shift = 0
    for i in range(len(message)):
        index = alphabet.find(message[i])
        if index==-1:
            decode_message += message[i]
        else:
            shift = alphabet.find(final_keyword[i])
            decode_message += alphabet[(index+26-shift)%26]
    return decode_message

final_message = vigenere_decoder(message, 'friends')
print(final_message)