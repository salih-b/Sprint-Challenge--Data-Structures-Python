class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.size = 0

    def append(self, item):
        if self.capacity == 0:
            return
# when capacity id mmet move oldest(first) item to the back of the list
        elif self.size < self.capacity:
            self.storage.append(item)
            self.size += 1
# when equal to capacity switch oldest item to the back then remove last item and add new item 
        # elif self.size == self.capacity:
        #     self.storage.pop(0)
        #     self.storage.append(item)
        #     self.storage.append(self.storage[0])
        #     self.storage.pop(0)
        else:
            self.storage.pop(0)
            # self.storage.pop()
            self.storage.append(item)
            # self.storage.append(self.storage[0])
            # self.storage.pop(0)


    def get(self):
        return self.storage

if True == True:
    test = RingBuffer(4)
    test.append(2)
    test.append(45)
    an1= test.get()
    test.append(10)
    an2= test.get()
    test.append(87)
    test.append(6)
    an3= test.get()
    print(f"TESTING: \n answer one: {an1} \n answer two: {an2} \n removing test returning two: {an3}")