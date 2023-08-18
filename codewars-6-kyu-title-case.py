def title_case(title, minor_words=''):
    title = title.lower().split()
    minor_words = minor_words.lower().split()
    #ans = []
    #for word in title.lower().split(' '):
        #if word == title.lower().split(' ')[0]:
        #or word.lower() not in minor_words.lower().split(' '):
           # print('First!', word)
            #ans.append(word.title())
       # else:
        #    ans.append(word.lower())
        #    print(title.lower().split(' '))
    return ' '.join([word.title() if ((word is title[0]) or (word not in minor_words)) else word for word in title])

#print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('THE WIND IN THE WILLOWS', 'The In'))