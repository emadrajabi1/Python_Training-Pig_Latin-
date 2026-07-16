def pig_latin(word):
    
    vowels ='aeiou'
    
    if word[0] in vowels :
        return f'{word}way'
    
    return f'{word[1:]}{word[0]}ay'

sentence = input('tell your sentence:')
words = sentence.split()
result = []
for word in words:
    result.append(pig_latin(word))

final = ' '.join(result)
print(final)

if __name__ == '__main__' :
    while True:
        user_input = input("Tell your word: ")
        
        if user_input.lower() in ("exit", "quit","Esc",""):
            print("Bye!")
            break

        print(pig_latin(user_input))