def anagram(string1,string2):
    if sorted(string1) == sorted(string2):
        print("It is anagram")
    else:
        print("Not an anagram")

anagram("silent","listen")
