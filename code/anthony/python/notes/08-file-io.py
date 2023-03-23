
"""
file = open('example.txt')  # default is "r"
content = file.read()
file.close()


content = content.replace("f", "l")


file = open('example.txt', "w")
file.write(content)
file.close()
"""

"""
students = open("students.csv")
content = students.read()
students.close()

content = content.split(",")
print(f"Here are your current students: {content}")
new_student = input("What is your new students name? ")
content.append(new_student)
content = ",".join(content)


students = open("students.csv", "w")
students.write(content)
students.close()
"""


# Read in treasureisland.txt
import string
file_name = "treasureisland.txt"
file = open(file_name)
contents = file.read()
file.close()

# Figure out how many words
words = contents.split(" ")
print(f"There are {len(words)} words in {file_name}")

# Figure out how many sentences
contents = contents.replace("?", ".").replace("!", ".").replace(":", ".")
sentences = contents.split(".")
print(f"There are {len(sentences)} sentences in {file_name}")

# What is the longest word
for char in string.punctuation + "”“\n":
    contents = contents.replace(char, " ")

contents = contents.replace(".", " ")
words = contents.split(" ")

longest_word = ""
for i in range(len(words)):
    if len(words[i]) > len(longest_word):
        longest_word = words[i]

print(f"The longest word in {file_name} is {longest_word}")


"""
contents = contents.replace("?", ".").replace("!", ".").replace(":", ".").replace(
    ",", " ").replace("“", " ").replace("”", " ").replace("-", " ").replace(";", " ").replace("\n", " ")
sentences = contents.split(".")

for char in string.punctuation + "”“\n":
    contents = contents.replace(char, " ")
"""
