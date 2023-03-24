"""
Adam
Date: Mar 23rd, 2023
Lab 6: ARI
""" 

import string

file_name = "momentum.txt"
file = open(file_name)
contents = file.read()
file.close()

# calculate how many words are in text
words = contents.split(" ")
print(f"There are {len(words)} words in {file_name}")

# calculate how many characters are in text
characters = len(contents)
print(f"There are {characters} characters in {file_name}")

# calculate how many sentences are in the text
contents = contents.replace("?", ".").replace("!", ".").replace(":", ".").replace(";", ".")
sentences = contents.split(".")
print(f"There are {len(sentences)} sentences in {file_name}")

# ari dictionary that let's user see what grade level a certain age reads at
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}




# ari formula to compute U.S. grade level
ari = 4.71 * (characters/len(words)) + 0.5 * (len(words)/len(sentences)) - 21.43
print(ari)

# if statement when ari score is larger than 14
if ari > 14:
    ari = 14

print(f"The ARI for {file_name} is {ari}")
print(f"This corresponds to a {ari_scale[14]['grade_level']} level of difficulty")
print(f"That is suitable for {ari_scale[14]['ages']} years old")


