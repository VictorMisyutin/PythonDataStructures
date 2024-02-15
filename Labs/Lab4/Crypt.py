# cryptography ( shuffle elements in a list )
import random
# for random shuffle
strMsg = "The Courier is En Route with the Documents"
# the plaintext secret message
print("plaintext message:")
print (strMsg, "\n")
# convert the plaintext to lower case
strMsg = strMsg.lower()
print("lower case:")
print (strMsg, "\n")
# replace any spaces in the message with an "x"
print("replace spaces with \'x\':")
strMsg = strMsg.replace(" ", "x")
plainTxtList = []
# declare a one - dimensional list
# populate the list with the characters comprising the message
for char in strMsg :
    # append the characters
    plainTxtList.append(char)
    # print() 
print("populate the list:")
print (plainTxtList, "\n")
# declare the cipher list
scrambledList = []
# use list() to cast the plaintext list into the ciphertext list
# randomly scramble the list of characters
print("perform a random shuffle:")
scrambledList = plainTxtList
random.shuffle(scrambledList)
print (scrambledList, "\n")
print ("length of the scrambled list, \n")
# determine the length of the list
print("length of list: ", len(scrambledList))
# print in blocks of seven letters per row
for index in range(len(scrambledList)) :
    if (index) % 7 == 0: 
        print()
    print (scrambledList[index], end='')
print()
# # decrypt
# decrypted = False 
# count = 0
# while not decrypted:
#     equal = True
#     for index in range(len(scrambledList)):
#         if scrambledList[index] != plainTxtList[index]:
#             equal = False
#             break
#     if equal:
#         decrypted = True
#     else:
#         random.shuffle(scrambledList)
#         count = count + 1
# print(f"Done, took {count} iterations.")