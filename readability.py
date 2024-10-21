import math
# a program that ask the user to type some text, and outputs the grade level for the text
# using Coleman_liau formula
# 0.0588 * L - 0.296 * S - 15.8
# S is the average number of sentences per 100 words in the text
user_input = input("Enter a text: ").lower()
# count 100 words
letter_counter = 0
word_counter = 1
sentence_counter = 0
for i in user_input:
    if i.isalpha():
        letter_counter += 1
    elif i in " ":
        word_counter += 1
    elif i in "." or i in "!" or i in "?":
        sentence_counter += 1
    else:
        continue
    
print(f"total letter is {letter_counter}")
print(f"total word is {word_counter}")
print(f"total sentence is {sentence_counter}")

average_letter = int((letter_counter/word_counter) * 100)
print(f"average_letter is {average_letter}")

average_sentence = int((sentence_counter/word_counter) * 100)
print(f"average_sentence {average_sentence}")

difficulty_index = int(0.0588 * average_letter - 0.296 * average_sentence - 15.8)
print(f"difficulty_index is {difficulty_index}") 
if difficulty_index > 16:
    print(f"Grade 16+")
elif difficulty_index == 15:
    print(f"Grade {difficulty_index}")
elif difficulty_index == 14:
    print(f"Grade {difficulty_index}")
elif difficulty_index == 13:
    print(f"Grade {difficulty_index}")
elif difficulty_index == 12:
    print(f"Grade {difficulty_index}")
elif difficulty_index == 11:
    print(f"Grade {difficulty_index}")
elif difficulty_index == 10:
    print(f"Grade {difficulty_index}")
elif difficulty_index == 9:
    print(f"Grade {difficulty_index}")
elif difficulty_index == 8:
    print(f"Grade {difficulty_index}")
elif difficulty_index == 7:
    print(f"Grade {difficulty_index}")
elif difficulty_index == 6:
    print(f"Grade {difficulty_index}")
elif difficulty_index == 5:
    print(f"Grade {difficulty_index}")
elif difficulty_index == 4:
    print(f"Grade {difficulty_index}")
elif difficulty_index == 3:
    print(f"Grade {difficulty_index}")
elif difficulty_index == 2:
    print(f"Grade {difficulty_index}")
elif difficulty_index == 1:
    print(f"Grade {difficulty_index}")
else:
    print(f"Before Grade 1")        