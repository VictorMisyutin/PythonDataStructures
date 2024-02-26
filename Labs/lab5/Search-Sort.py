import datetime

# menu selector
menuSelect = 0
listSelect = 0

list1 = [22, 25, 5, 1, 7, 2, 8, 9, 14, 15, 4, 15, 29, 20, 33, 31]
list2 = ['b', 't', 'a', 'n', 'd', 'p', 'h', 'c', 'o', 'r', 'i', 'k']
list3 = ["dog", "cat", "horse", "cow", "ant", "squirrel", "mouse", "chicken", "rooster", "bird"]
myList = []
def DisplayMenu() :
    print ("enter your choice")
    print ("1 for a Linear Search")
    print ("2 for a Binary Search")
    print ("3 for a Bubble Sort")
    print ("4 for a Selection Sort")
    print ("5 for a Insertion Sort")

def ListSelection():
    print ("Please select a list: ")
    print ("1 for [22, 25, 5, 1, 7, 2, 8, 9, 14, 15, 4, 15, 29, 20, 33, 31]")
    print ("2 for [b, t, a, n, d, p, h, c, o, r, i, k]")
    print ("3 for [dog, cat, horse, cow, ant, squirrel, mouse, chicken, rooster, bird]")
    global listSelect
    listSelect = int(input())
    global myList
    if(listSelect == 1):
        myList = list1
    elif(listSelect == 2):
        myList = list2
    elif(listSelect == 3):
        myList = list3
    else:
        print("invalid selection")
        exit()

def SearchSelection():
    global searchItem
    print("What element would you like to search for?")
    if(listSelect == 1):
        try:
            searchItem = int(input())
        except:
            print("Program terminated, you must enter a number.")
            exit()
    else:
        searchItem = input()



def LinearSearch():
    found = False
    for i in range(len(myList)) :
        if(myList[i] == searchItem) :
            found = True
            print(searchItem, " found at position ", i)
            break
    if (found == False) :
        print(searchItem, " is not in list")


def binarySearch():
    print('First we need to sort the list.\nHere is the sorted list:')
    bubbleSort()
    print(myList)

    n = len(myList)
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if searchItem == myList[mid]:
            print(searchItem, " found at position ", mid)
            return
        elif searchItem < myList[mid]:
            end = mid - 1
        else:
            start = mid + 1

    print(searchItem, " is not in list")

def bubbleSort() :
    n = len(myList)
    for i in range(n - 1) :
        for j in range(0, n - i - 1) :
            if myList[j] > myList[j + 1] :
              myList[j], myList[j + 1] = myList[j + 1], myList[j]

def SelectionSort():
    for i in range(len(myList)) :
        min_= i
        for j in range(i + 1, len(myList)) :
            if (myList[min_] > myList[j]) :
                min_ = j
        myList[i], myList[min_] = myList[min_], myList[i]

def InsertionSort():
    for i in range(1, len(myList)):
        key = myList[i]
        j = i - 1
        while j >= 0 and key < myList[j]:
            myList[j + 1] = myList[j]
            j -= 1
        myList[j + 1] = key

def SelectRoutine() :
    global menuSelect
    DisplayMenu()
    menuSelect = int(input())
    if (menuSelect == 1) :
        ListSelection()
        SearchSelection()
        print ("Call the Linear Search Routine")
        tStamp1 = datetime.datetime.now()
        LinearSearch()
        tStamp2 = datetime.datetime.now()
        delta = tStamp2 - tStamp1
        interval = float(delta.total_seconds() * 1000)
        print ("Routine took " + str(interval) + " miliseconds")
    elif (menuSelect == 2) :
        ListSelection()
        SearchSelection()
        print ("Call the Binary Search Routine")
        tStamp1 = datetime.datetime.now()
        binarySearch()
        tStamp2 = datetime.datetime.now()
        delta = tStamp2 - tStamp1
        interval = int(delta.total_seconds() * 1000)
        print ("Routine took " + str(interval) + " miliseconds")
    elif (menuSelect == 3) :
        ListSelection()
        print ("Call the Bubble Sort Routine")
        tStamp1 = datetime.datetime.now()
        bubbleSort()
        print ("the sorted array is:\n[ ", end='')
        for i in range(len(myList)) :
            print (myList[i], end=' ')
        print(']')
        tStamp2 = datetime.datetime.now()
        delta = tStamp2 - tStamp1
        interval = int(delta.total_seconds() * 1000)
        print ("Routine took " + str(interval) + " miliseconds")
    elif (menuSelect == 4) :
        ListSelection()
        print ("Call the Selection Sort Routine")
        tStamp1 = datetime.datetime.now()
        SelectionSort()
        print ("the sorted array is:\n[ ", end='')
        for i in range(len(myList)) :
            print (myList[i], end=' ')
        print(']')
        tStamp2 = datetime.datetime.now()
        delta = tStamp2 - tStamp1
        interval = int(delta.total_seconds() * 1000)
        print ("Routine took " + str(interval) + " miliseconds")
    elif (menuSelect == 5) :
        ListSelection()
        print ("Call the Insertion Sort Routine")
        tStamp1 = datetime.datetime.now()
        InsertionSort()
        print ("the sorted array is:\n[ ", end='')
        for i in range(len(myList)) :
            print (myList[i], end=' ')
        print(']')
        tStamp2 = datetime.datetime.now()
        delta = tStamp2 - tStamp1
        interval = int(delta.total_seconds() * 1000)
        print ("Routine took " + str(interval) + " miliseconds")
    else :
        print("invalid selection")

SelectRoutine()
