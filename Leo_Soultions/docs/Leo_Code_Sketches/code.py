
i = input("Enter your word: ")
print(i)

def length_of_last_word(i):
    i = i.strip()
    return len(i.split(" ")[-1])

print(length_of_last_word(i))
print("The last word is:", i.split(" ")[-1], "with length of:", len(i.split(" ")[-1]))












