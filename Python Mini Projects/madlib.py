# open file and read it 

with open("story.txt", "r") as f: # opened a file and read using r, with open ensures file is safe
    story = f.read()


# create some before stuff

# we want to slice just one section continuously and put it into a set 

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

# slicing it down 

for idx, char in enumerate(story): # enumerate gives the index of the char and the char itself in the given file
    if char == target_start: # if the start of the words has the <, then we set that as the index to slice later
        start_of_word = idx

    if char == target_end and start_of_word != -1: # if the char is equal to what we know as the end >, then we know that the idx is the end index
        word = story[start_of_word: idx + 1] # so we slice this, in story, we find the index of the start from earlier and then the idx right now + 1 to include
        # then assign it the variable word because it is - <word>
        words.add(word) # we add the word to the set from earlier called words - which will only unique ones 
        start_of_word = -1 # we then reset the program by putting the start of the word as -1 to restart the progress

answers = {} # so now we want to basically assign each word to its corresponding user input answer and store it in this dictionary

# ask user for word

for word in words: # so for each word in the whole set of words
    answer = input("Enter word for " + word + " : ") # we ask for the answer from user and assign it to var answer
    answers[word] = answer # we then go into the dict - answer, set the key as the word that is looping and set the value as the answer that we just got from user

# replace each given word with prexisting word

for word in words: # so for the word in words - words being the set with all the <word>
    story = story.replace(word, answers[word]) # using the loop, we then replace each of the word with the answer - which is answers[word]

print(story)