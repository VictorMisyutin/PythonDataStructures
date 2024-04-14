class Node :
    # singly linked node
    def __init__(self, data = None) :
        self.data = data
        self.next = None
class singly_linked_list :
    def __init__(self) :
        # create an empty list
        self.head = None
        self.tail = None
        self.count = 0

    def length(self):
        return self.count
    
    def iterate_item(self) :
        # iterate through the list
        current_item = self.head
        while current_item :
            yield current_item
            current_item = current_item.next

    def append_item(self, data) :
        # append items on the list
        node = Node(data)
        if self.tail :
            self.tail.next = node
            self.tail = node
        else :
            self.head = node
            self.tail = node
        self.count += 1

    def delete_by_value(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        previous = self.head
        current = self.head.next
        while(current and current != data):
            if(current.data == data):
                previous.next = current.next
                self.count -= 1
                return
            previous = current
            current = current.next

    def delete_by_index(self, index):
        if(index >= self.count):
            return print(index, " is out of bounds")
        if index == 0:
            self.head = self.head.next
        count = 1
        previous = self.head
        current = previous.next
        while(count != index):
            count += 1
            previous = current
            current = current.next
        previous.next = current.next
        self.count -= 1

    def contains(self, data):
        for node in self.iterate_item() :
            if node.data == data:
                return True
        return False
    def index_of(self, data):
        index = 0
        for val in self.iterate_item() :
            if val.data == data:
                return index
            index += 1
        return -1
    
    def update_by_index(self, index, new_val):
        if(index >= self.count):
            return print(index, " is out of bounds")
        count = 0
        current = self.head
        while(count != index):
            count += 1
            current = current.next
        current.data = new_val

    def update_by_value(self, origin_val, new_val):
        if(not self.contains(origin_val)):
            return print(origin_val, " not found")
        for node in self.iterate_item() :
            if node.data == origin_val:
                node.data = new_val
                return
            
    def sort_ascending(self):
        if self.length() < 2: return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    temp = current.next.data
                    current.next.data = current.data
                    current.data = temp
                    swapped = True
                current = current.next

    def sort_descending(self):
        if self.length() < 2: return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data < current.next.data:
                    temp = current.next.data
                    current.next.data = current.data
                    current.data = temp
                    swapped = True
                current = current.next

    def print(self):
        # iterate through the list
        current_item = self.head
        while current_item :
            val = current_item.data
            current_item = current_item.next
            print(val)
            
    # adds linked_list to the end of self
    def merge(self, linked_list):
        if linked_list.length() == 0:
            return
        elif linked_list.length() == 1:
            self.tail.next = linked_list.head
            self.tail = linked_list.head
            return
        current = linked_list.head
        while current.next:
            self.tail.next = current
            self.tail = current
            current = current.next

print("items 1 linked list")
items1 = singly_linked_list()
items1.append_item("item 1")
items1.append_item("item 4")
items1.append_item("item 2")
items1.append_item("item 5")
items1.append_item("item 3")
items1.print()
print("\nitems 1 sorted in ascending order")
items1.sort_ascending()
items1.print()

print("\nitems 2 linked list")
items2 = singly_linked_list()
items2.append_item("item 6")
items2.append_item("item 8")
items2.append_item("item 7")
items2.append_item("item 9")
items2.print()
print("\nitems 2 sorted in descending order")
items2.sort_descending()
items2.print()

print("\nitems 2 contains 'item 9': ", items2.contains("item 9"))
print("merge items 2 into items 1:")
items1.merge(items2)
items1.print()

print("\nindex of 'item 6': ", items1.index_of("item 6"))
print("\nsort new list")
items1.sort_ascending()
items1.print()
print("\ndelete 'item 3'")
items1.delete_by_value("item 3")
items1.print()
