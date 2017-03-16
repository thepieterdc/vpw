import queue

pq = queue.PriorityQueue()

pq.put((1, "Test"))
pq.put((6, "Test2"))
pq.put((2, "A"))

while not pq.empty():
    print(pq.get())
