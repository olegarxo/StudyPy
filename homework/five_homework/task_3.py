def Take_text(name):
    with open(f'{name}'+'.txt','r+') as f:
        text = list(f.readline())
        return text
def RLE_file(text):
    tamp = ''
    coun = 0
    dic = {}
    for i in text:
        if i == tamp:
            coun += 1
            dic[i] = coun
        else:
            tamp = i
            coun = 0
            coun += 1
            dic[i] = coun
    return dic

def Write_file(sum_dict):
    with open('text2.txt', 'w+') as file:
        key = sum_dict.keys()
        for i in key:
            file.write(i * sum_dict.get(i))
name = input('Enter file name: ')
text = Take_text(name)
tamp = (RLE_file(text))
Write_file(tamp)