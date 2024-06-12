class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None


    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp = temp.next

    def del_begin(self):
        self.head = self.head.next

    def del__end(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next =  None
    def deL__any(self,x):
        temp = self.head
        while temp.next.data != x:
            temp = temp.next
        if temp.next.next is not None:
            temp.next = temp.next.next
        else:
            temp.next = None

    def add_begin(self,data):
        new = node(data)
        new.next = self.head
        self.head = new

    def add_end(self,data):
        new = node(data)
        if self.head == None:
            self.head = new
        else:
            temp = self.head
            while temp.next is not None:
                temp =  temp.next
            temp.next = new

    def add_any(self,data,x):
        new =  node(data)
        temp = self.head
        while temp is not None:
            if temp.data == x:
                break
            temp = temp.next

        if temp is None:
            print("Wrong element has been given by the user")
        else:
            new.next = temp.next
            temp.next = new





if __name__ == "__main__":
    LL = Linkedlist()
    LL.head =  node(1)
    second =  node(2)
    third =  node(3)
    LL.head.next = second
    second.next = third
    LL.add_begin(4)
    LL.add_end(5)
    LL.add_any(8,2)
    LL.traverse()


    
