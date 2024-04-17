from Queue import *

# instantiate a class object
q = Queue()

# object uses methods of the class
q.enqueue("Customer 1")
q.enqueue("Doordash Customer 2")
q.enqueue("GrubHub Customer 3")
q.enqueue("Customer 4")
q.dequeue()
q.display()
q.dequeue()
q.display()
