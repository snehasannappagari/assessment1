string1 = input("Enter a string : ")
unique_letters = set()
for letter in string1:
    if letter not in unique_letters:
        unique_letters.add(letter)
unique_letters = sorted(list(unique_letters))
print("unique_letters:",",".join(unique_letters))
