import sys

def is_hidden(str1, str2):
    done = []
    for letter in str1:
        if letter in str2: #if the letter is in str2
            done.append(letter)
            #replace first occurence of letter in str2 and continue
            str2 = str2.replace(letter, "", 1)
            #if done list has the same length as str1 it means str1 is in str2
            if len(done) == len(str1):
                return True
        else:
            return False
            

try:
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    if is_hidden(str1, str2):
        print("1")
    else:
        print("0")
except:
    print("\n")



