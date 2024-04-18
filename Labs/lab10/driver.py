# from Queue import *
from Priority_Queue import *

pq = PriorityQueue()

pq.enqueue(1, "GrubHub 1")
pq.enqueue(2, "Customer 1")
pq.enqueue(2, "Customer 2")
pq.enqueue(1, "GrubHub 2")
pq.enqueue(1, "GrubHub 3")
pq.enqueue(2, "Customer 3")
pq.enqueue(1, "GrubHub 4")
pq.enqueue(4, "Senior Executive")
pq.enqueue(1, "GrubHub 5")
pq.enqueue(3, "High Value Customer")

print("Here is the current queue. Each element is (priority, customer)")
pq.display()
print()

print("next person being served is: " + pq.peek())

print("\nI will now dequeue customers until the priorty queue is empty:")
while(not pq.isEmpty()):
    pq.dequeue()

print("\npriority queue is empty")