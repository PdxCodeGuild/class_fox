'''
Lab 6: ARI 
22 Mar 23
'''
import string
file_name = "The Raven"
file = open("the_raven.txt")
contents = file.read()
file.close

# number or words
words = contents.split(" ")
print(f"There are {len(words)} words in {file_name}.")
''' There are 3281 words in The Raven. '''

# number of sentences
sentences = contents.split(".")
print(f"There are {len(sentences)} sentences in {file_name}. ")

# number of characters
characters = contents
for char in string.punctuation + " ”“\n":
    characters = characters.replace(char, " ")
characters = " ".join(characters)
print(f"There are {len(characters)} characters in {file_name}.")

ARI = float(4.71*(len(characters)/len(words)) + 0.5*(len(words)/len(sentences) - 21.43))
print(ARI)

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
if ARI > 14:
    ARI = 14
if ARI in ari_scale:
    difficulty = ari_scale[ARI]['grade_level']
    suitable = ari_scale[ARI]['ages']
print(f"The ARI for {file_name} is {ARI}.")
print(f"This corresponds to a {difficulty} level of difficulty.") 
print(f"That is suitable for an average person {suitable} years old.")