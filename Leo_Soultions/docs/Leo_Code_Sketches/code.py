""" 58. Length of Last Word Easy 3.4K 179 Companies
Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only. """

def length_of_last_word(s: str) -> int:
    # strip the string of any white space
    s = s.strip()
    # split the string into a list of words
    words = s.split()
    # return the length of the last word in the list
    return len(words[-1])

# example usage
s = "Hello World"
print(length_of_last_word(s)) # output: 5


user_input = input("Enter a string: ")
print("You entered:", user_input)
