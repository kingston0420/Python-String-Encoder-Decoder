message='vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.'
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
for i in range(1,26):
    print(decoder(message, i))

#the shift is 7 that we found