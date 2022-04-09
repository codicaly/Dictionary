from PyDictionary import PyDictionary
dictionary = PyDictionary()

print('-----Enter 0 to exit-----\nWelcome to Dictionary\n')

while True :
    word = input("Enter the word : ")
    if word == '0':
        break
    print(dictionary.meaning(word))