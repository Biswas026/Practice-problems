def vowels(string):
    new_string = ""
    vowel="AEIOUaeiou"
    for a in string:
        if a not in vowel:
            new_string += a
    print(new_string)

string=input("Enter your character")
vowels(string)
