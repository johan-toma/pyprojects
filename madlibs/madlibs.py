import os
import sys

if __name__ == '__main__':
    location = os.path.dirname(__file__)
    f = open(os.path.join(location, 'story.txt'), 'r')
    story = f.read()
    
    words = []
    start = "<"
    end = ">"
    temp_word = ""
    for char in story:
        #nytt ord då öka dens plats i listan, alla ord läggs i words
        if char == " ":
            words.append(temp_word)
            temp_word = ""
        else:
            temp_word = temp_word + char
    
    mutable_words = set()
    for word in words:
        if start == word[0] and end == word[-1]:
            mutable_words.add(word)
    
    print("MADLIBS GAME!  Make your own story")
    print("Replace the names, adjectives, adverbs, verbs and nouns!!!")
    ordered_list = []
    for mutable_word in mutable_words:
        #print(mutable_word[1:-1])
        user_input = input(f"{mutable_word[1:-1]}: ")
        ordered_list.append(user_input)
    
    replaced_story = ""
    temp_word = ""
    i = 0
    ##print(words)
    for word in words:
        if word[0] == start or word[-1] == end:
            if i < len(ordered_list):
                replaced_story = replaced_story + ordered_list[i] + " "
            i = i + 1
        elif word[0] != start or word[-1] != end:
            replaced_story = replaced_story + word + " "
        
        
        
    print(replaced_story)
        
        
        