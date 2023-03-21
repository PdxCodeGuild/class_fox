"""
Write a program that prompts the user for a string, and encodes it with ROT13.
For each character, find the corresponding character, add it to an output string.
Notice that there are 26 letters in the English language, so encryption is the same as decryption.

Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m


Version 2 (optional)
Allow the user to input the amount of rotation used in the encryption / decryption.
"""
import string
# create list of characters
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# characters = list(string.ascii_lowercase)

# prompt the user for their phrase
phrase = input("Enter phrase to be encrypted: ")

output_string = ""
# loop over user's phrase 'apple' -> 'nccyr'
for char in phrase:
    if char in characters:
        # find the position of each character in our list
        position = characters.index(char)

        # Add 13 to that position
        new_position = position + 13
        new_position = new_position % 26

        # Take the character at the new position and add it to the output
        output_string = output_string + characters[new_position]
    else:
        output_string = output_string + char

# print output
print(output_string)
