""" 58. Length of Last Word Easy 3.4K 179 Companies
Given a string s consisting of words and spaces, return the length of the last word in the string. 
A word is a maximal substring consisting of non-space characters only. """

# help me think throught this problem in code steps
# 1. input a string
# 2. strip the string of any white space
# 3. split the string into a list of words
# 4. return the length of the last word in the list

# Leo soultion: (solve this problem using my coding style)




# co-pilot soultion: (solve this problem using a beginner level's coding style)
def length_of_last_word(s):
    s = s.strip()  # remove leading and trailing white spaces
    words = s.split(' ')  # split the string into words
    if not words:  # if there are no words
        return 0
    else:  # return the length of the last word
        last_word = words[-1]
        return len(last_word)


# co-pilot soultion: (solve this problem using a intermediate level's coding style)
def length_of_last_word(s):
    words = [word for word in s.split() if word]  # list comprehension to generate list of non-empty words
    return len(words[-1]) if words else 0  # return the length of the last word or 0 if there are no words


# co-pilot soultion: (solve this problem using a advanced level's coding style)
def length_of_last_word(s):
    return len(s.strip().split(' ')[-1]) if s.strip() else 0  # chain methods together for a concise solution


"""
# # co-pilot soultion:
i = input("Enter your word: ")
print(i)

def length_of_last_word(i):
    i = i.strip()
    return len(i.split(" ")[-1])

print(length_of_last_word(i))
print("The last word is:", i.split(" ")[-1], "with length of:", len(i.split(" ")[-1]))


"""

"""
# Notes from Leo: using GPT"
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        if len(s) == 0:
            return 0
        if len(s) == 1:
            if s[0] == " ":
                return 0
            else:
                return 1

        if s[-1] == " ":
            return 0

        count = 0
        for i in range(len(s)-1, -1
                          , -1):
                if s[i] == " ":
                 break
                else:
                 count += 1
        return count
    
# Runtime: 28 ms, faster than 81.48% of Python3 online submissions for Length of Last Word.
# Memory Usage: 14.3 MB, less than 49.99% of Python3 online submissions for Length of Last Word.

        #         if len(s) == 0:
        #             return 0
        #         if len(s) == 1:
        #             if s[0] == " ":
        #                 return 0
        #             else:
        #                 return 1

        #         if s[-1] == " ":
        #             return 0

        #         count = 0
        #         for i in range(len(s)-1, -1, -1):
        #             if s[i] == " ":
        #                 break
        #             else:
        #                 count += 1
        #         return count

        #         if len(s) == 0:
        #             return 0
        #         if len(s) == 1:
        #             if s[0] == " ":
        #                 return 0
        #             else:
        #                 return 1

        #         if s[-1] == " ":
        #             return 0

        #         count = 0
        #         for i in range(len(s)-1, -1, -1):
        #             if s[i] == " ":
        #                 break
        #             else:
        #                 count += 1
        #         return count

        #         if len(s) == 0:
        #             return 0
        #         if len(s) == 1:
        #             if s[0] == " ":
        #                 return 0
        #             else:
        #                 return 1

        #         if s[-1] == " ":
        #             return 0

        #         count = 0
        #         for i in range(len(s)-1, -1, -1):
        #             if s[i] == " ":
        #                 break
        #             else:
        #                 count += 1
        #         return count

        """