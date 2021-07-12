#Finished on 7/7/2021
#Replaces letters in a password to stronger charactors
def listToString(s):
    str1 = ""
    for ele in s: 
        str1 += ele  
    return str1

holder = 0

Replace = ['@', '!', '3', '1', '^', '$', '*', '¥',  '₩', '0']

Normal = ['a', 'i', 'e', 'l', 'v', 's', 'x', 'y', 'w', 'o']

Weak = input("Please enter your password ")

Weak_sep = list(Weak)

while holder < len(Weak_sep):
     if Weak_sep[holder] in Normal:
            replace_char = Weak_sep[holder]
            replace_index = Normal.index(replace_char)
            Weak_sep[holder] = Replace[replace_index]
     holder = holder + 1

Strong_sep = Weak_sep

listToString(Strong_sep)

print(Strong_sep)