#List implementation

# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.pop()
#print("Top = ",stack[-1])
# print(stack)


#Module implementation
#1. By using double ended queues

# import collections
# stack = collections.deque()
# stack.append(10)
# stack.append(20)
# stack.append(30)
#
# print(stack)
# stack.pop()
#
# print(stack)


#2. By using Lifoqueue

import queue

stack = queue.LifoQueue()
stack.put_nowait(10)
stack.put(20)
stack.put(30)

stack.get()

while not stack.empty():
    print(stack.get_nowait())


