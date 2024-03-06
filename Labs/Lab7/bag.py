class Bag(object) :
    def __init__(self, maxsize = 10) :
        self.maxsize = maxsize
        self._items = list()
    
    def add(self, item) :
        if (len(self) >= self.maxsize) :
            raise Exception('Full')
        self._items.append(item)

    def remove(self, item) :
        if(self.contains(item)):
            self._items.remove(item)
        else:
            print(f'Bag does not contain {item}')
    def __len__(self) :
        return len(self._items)
    
    def __iter__(self) :
        for item in self._items:
            yield item

    def isEmpty(self):
        return len(self) == 0
    
    def size(self):
        return len(self)
    
    def contains(self, item):
        for i in self._items:
            if i == item: return True
        return False
    
    def isFull(self):
        return len(self) == self.maxsize 

    def print(self):
        print(f"Current Bag (size {len(self)}):")
        for item in self._items:
            print(item, end=' ')
        print()

def driver():
    size = int(input("Enter the size of the bag you would like to create: "))
    bag = Bag(size)
    items_string = input(f"Enter {size} or less items that you would like to enter into the bag (seperated by spaces): ")
    for item in items_string.split():
        bag.add(item)
    bag.print()
    print(f"Bag is full: {bag.isFull()}")
    user_input = input("Enter an item you would like to remove: ")
    bag.remove(user_input)
    bag.print()
    user_input = input("Enter an item you would like to check is in the bag: ")
    print(f"{user_input} is in bag: {bag.contains(user_input)}")



if __name__ == "__main__":
    driver()