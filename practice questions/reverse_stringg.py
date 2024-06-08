def reverse(string):
    org_string = string
    new_string = ""
    for i in range(-1,-len(string)-1,-1):
        new_string += string[i]

    print("Your old string was",org_string)
    print("your reversed string will be",new_string)


reverse("Biswas")
        
