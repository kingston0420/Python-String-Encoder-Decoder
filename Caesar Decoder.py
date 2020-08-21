alphabet = 'abcdefghijklmnopqrstuvwxyz'
def decoder(sentence, offset):
    decode = ''
    for word in sentence:
        index = alphabet.find(word)
        if index==-1:
            decode = decode + word
        else: 
            decode = decode + alphabet[(index+offset)%26]
    return decode
message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
answer = decoder(message, 10) 
print(answer)