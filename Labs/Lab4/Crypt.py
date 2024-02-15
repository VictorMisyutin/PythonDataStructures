# cryptography ( shuffle elements in a list )
import random
import time
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
scrambledList = plainTxtList[:]
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

# decryption
decrypted = False 
count = 0
start_time = time.time()  # Start timing
while scrambledList != plainTxtList:
    random.shuffle(scrambledList)
    count = count + 1
    if (time.time() -  start_time) > 10:
        print("Decryption terminated after 10 seconds")
        break
elapsed_time = time.time() - start_time
print(f"It took {count} iterations and {elapsed_time} seconds.")
# I ran this decryption algorithm for over two minutes without completion 