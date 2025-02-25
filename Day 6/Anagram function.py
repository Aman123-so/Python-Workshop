def anagram(str1, str2):
    str1= str1.lower()
    str2= str2.lower()
    return sorted(str1)==sorted(str2)
string1= input("Enter first string: ")
string2= input("Enter second string: ")
if anagram (string1,string2):
    print("Anagram")
else:
    print("Not Anagram")
