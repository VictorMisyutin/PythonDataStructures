class PriorityQueue():
    # construct the list to implement the queue
    def __init__(self):
        self.queue = []

    # enqueue an element
    def enqueue(self, priority, item):
        self.queue.append((priority, self.size(), item))  # Include counter for insertion order
        # lambda function
        # -x[0] because we want higher priority to be first
        # then x[1] because the second factor should be insertion order
        self.queue.sort(key=lambda x: (-x[0], x[1])) 

    # remove an element from the queue
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        priority, ignore, item = self.queue.pop(0) 
        print(f"{item} is now being served.")
        return item

    # display the current queue
    def display(self):
        print(self.queue)

    # return the size of the queue
    def size(self):
        return len(self.queue)

    # return true if queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # return next element without dequeing
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0][2]
        else:
            return None
