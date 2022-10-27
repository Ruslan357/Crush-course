def send_massages(list_of_text):
    '''shows messages from the list. Creates and returns new list'''
    sent_massages = []
    while list_of_text:
        temp = list_of_text.pop()
        sent_massages.append(temp)
    return sent_massages


text1 = 'this is the text №1'
text2 = 'this is the text №2'
text3 = 'this is the text №3'
texts = [text1, text2, text3]
texts_2=send_massages(texts[:])
for text in texts:
    print(text)

print()

for text in texts_2:
    print(text)

