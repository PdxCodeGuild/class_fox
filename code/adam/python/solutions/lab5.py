"""
Adam
Date: Mar 20th, 2023
Lab 5: ROT13
"""


# Version 1

# create dictionary of chracters
characters = {"a": "n",
"b": "o",
"c": "p",
"d": "q",
"e": "r",
"f": "s",
"g": "t",
"h": "u",
"i": "v",
"j": "w",
"k": "x",
"l": "y",
"m": "z",
"n": "a",
"o": "b",
"p": "c",
"q": "d",
"r": "e",
"s": "f",
"t": "g",
"u": "h",
"v": "i",
"w": "j",
"x": "k",
"y": "l",
"z": "m"
}
              

# ask for user input for their phrase
phrase = input("Enter phrase to be encrypted: ")

# loop over phrase
output_str = ""
for char in phrase:
    if char in characters:
        output_str = output_str + characters[char]
# user input converted to output string
print(output_str)


