queue = []
 
queue.append("Jake")
queue.append("Jill")

print("Dequeued customer:", queue.pop(0))

queue.append("Iris")

print("Dequeued customer:", queue.pop(0))

queue.append("David")

print("Size of the queue:", len(queue))

print("Customer at the front of the queue:", queue[0])
