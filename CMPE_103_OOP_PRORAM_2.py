''' PROBLEM 2 - DECRYPTION
Write a program that will accept a string as encypted text and then the program will decrypt it using the following character substitute:
'a'= *, 'e'= &, 'i'= #, 'o'= +, 'u'= ! '''

# Program takes in user's input (message)
message = input("Enter an encrypted message \n(ex. th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g ) : ")
changed_char = ""

# loop the message to check each character
for i in range(len(message)):
    # replace characters
    # replace * with a
    if message[i] == "*":
        # set a control :
        changed_char += "a"
    # replace & with e
    elif message[i] == "&":
        changed_char += "e"
    # replace # with i
    elif message[i] == "#":
        changed_char += "i"
    # replace + with 0
    elif message[i] == "+":
        # set a control
        changed_char += "o"
    # replace ! with u
    elif message[i] == "!":
        # set a control
        changed_char += "u"
    else:
        changed_char += message[i]
        
     #display the decrypted message
print(changed_char)   
