def send_massages(list_of_text):
    '''shows messages from the list. Creates and returns new list'''
    sent_massages = []
    while list_of_text:
        temp = list_of_text.pop()
        print(temp)
        sent_massages.append(temp)
    print()


text1 = 'this is the text №1'
text2 = 'this is the text №2'
text3 = 'this is the text №3'

texts = [text1, text2, text3]
send_massages(texts[:])

for text in texts:
    print(text)
