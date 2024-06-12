#Queue implementation

#1.Using List

# queue = []
# queue.append(10)
# queue.append(20)
# queue.append(30)
#
# print(not queue) #is empty
# print(queue)
#
# queue.pop(0)
#
# print(queue)


#2.Using module

#1.collections module

# import collections
# queue = collections.deque()
#
# queue.appendleft(10)
# queue.appendleft(20)
# queue.appendleft(30)
# queue.appendleft(40)
#
# print(queue)
#
# queue.pop()
# queue.pop()
#
# print(queue)

#2.Queue module

import queue
Queue = queue.Queue(maxsize=5)

Queue.put_nowait(10)
Queue.put_nowait(20)
Queue.put_nowait(102)
Queue.put_nowait(1023)
Queue.put_nowait(123)

while not Queue.empty():
    print(Queue.get_nowait())

