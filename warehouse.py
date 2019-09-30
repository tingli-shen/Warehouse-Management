
class Item:
    def __init__(self, size):
        self.size = size
        self.contained_by=None # the parent container containing this container

class Warehouse: #super class
    def __init__(self):
        self.data=[] # a list stores all the things ever appended by this container's method add()
        self.position={} # a dictionary maps things to the index in self.data. key: thing, value: index
        

    def __len__(self):
        return len(self.data)
    
    def count(self):
        cnt=[0] # count total number of objects within the Container
        for container in self.data:
            cnt[0]+=1
            self._recursion_count(container,cnt)
        return cnt[0]

    def add(self,thing):
        # implement bonus 2 with contained_by (parent container)
        if thing.contained_by:
            previous_container=thing.contained_by
            previous_container.remove(thing)
        # assign thing's parent container to this container
        thing.contained_by=self
        # push thing to self.data 
        self.data.append(thing)
        # record thing's index in self.data
        self.position[thing]=len(self.data)-1
        
        return True

    def contains(self,thing):
        # check if the thing is within the current Container.
        if thing in self.position:
            return True
        # check if the thing is within a Container within the current Container by recursion.
        for container in self.data:
            if self._recursion_contains(container,thing):
                return True
        return False
    
    def remove(self,*thing):
        '''
        The dictionary allows method remove take O(1) time. 
        It takes O(n) to remove the thing if removing the thing by it's index in self.data
        '''
        # The container contains nothing
        if not self.data:
            return None
        # if no input or thing is None, remove and return the last object added to the Container
        if not thing or not thing[0]:
            last_container=self.data[-1]
            self.data.pop()
            del self.position[last_container]
            return last_container
        thing=thing[0]
        # not found
        if thing not in self.position:
            return None
        # remove the thing within the container
        thing_idx,last_container=self.position[thing],self.data[-1]
        # change the ｐｏｓｉｔｉｏｎ of the last object to the ｐｏｓｉｔｉｏｎ of the object we remove in self.ｄａｔａ
        self.data[thing_idx]=last_container
        #　change the index of the last object to the index of the object we remove in self.position
        self.position[last_container]=thing_idx
        # remove the last object in self.data and remove the object we want to remove in self.position.
        self.data.pop()
        del self.position[thing]
        return thing
    
    def pack(self,thing): # the same as method add because Warehouse has infinite capacity
        self.add(thing)
        
    def extract(self,thing):
        # check if the container contains the thing
        if not self.contains(thing):
            return None
        # check if the Container contains the thing but not within a Container within the Container
        if thing in self.position:
            self.remove(thing)
            return thing
        # remove the thing within the current container
        for container in self.data:
            self._recursion_extract(container,thing)
        return thing
    
    '''
        Helper Functions
    '''
    def _recursion_count(self,container,cnt):
        if type(container).__name__=='Item': # cannot go deeper because Item is the most basic type
            return 
        # go deeper to count
        for item in container.data:
            cnt[0]+=1
            container._recursion_count(item,cnt)
    
    def _recursion_contains(self,container,thing):
        if type(container).__name__=='Item': # cannot go deeper because Item is the most basic type
            return False
        # check if the Container contains the thing but not within a Container within the Container
        if thing in container.position:
            return True
        # go deeper to check
        for item in container.data:
            if container._recursion_contains(item,thing):
                return True
            
    def _recursion_extract(self,container,thing):
        # check if the Container contains the thing but not within a Container within the Container. If yes, remove the thing
        if thing in container.position:
            container.remove(thing)
            return
        # go deeper to find the thing and remove it
        for item in container.data:
            if type(item).__name__=='Item':
                continue
            container._recursion_extract(item,thing)
        

class Bin(Warehouse):
    def __init__(self):
        super().__init__()
        self.total_size=0 # total units that the container contains
        self.capacity = 10
        self.contained_by=None
        
    def add(self,thing): # override because we need to check if the new thing can be added
        # use capacity as size if the thing is not Item type. If the thing is Item type, use it's size
        size=thing.size if type(thing).__name__=='Item' else thing.capacity
        # check if the container can hold the thing
        if size+self.total_size>self.capacity or type(thing).__name__==type(self).__name__:
            return False
        self.total_size+=size
        return super().add(thing)
        
    def pack(self,thing):
        # use capacity as size if the thing is not Item type. If the thing is Item type, use it's size
        size=thing.size if type(thing).__name__=='Item' else thing.capacity
        # check if the current container can hold the thing
        if size+self.total_size<=self.capacity:
            self.add(thing)
        # attempt to find room for the object inside any of the Containers within it with recursion
        for container in self.data:
            if self._recursion_pack(container,thing):
                return True
        return False
    '''
        Helper Functions
    '''
    def _recursion_pack(self,container,thing):
        # use capacity as size if the thing is not Item type. If the thing is Item type, use it's size
        size=thing.size if type(thing).__name__=='Item' else thing.capacity
        if type(container).__name__=='Item': # cannot go deeper because Item is the most basic type
            return False
        # check if the current container can hold the thing
        if size+container.total_size<=container.capacity:
            container.add(thing)
            return True
        # attempt to find room for the object inside any of the Containers within it with recursion
        for item in container.data:
            if container._recursion_pack(item,thing):
                return True
            
class Shelf(Bin):
    def __init__(self):
        super().__init__()
        self.capacity = 100
    #Implement bonus 1
    def add(self,thing):
        if type(thing).__name__=='Item' and thing.size<8:
            return False
        return super().add(thing)
    
class Box(Bin):
    def __init__(self):
        super().__init__()
        self.capacity = 5 


class Bag(Bin):
    def __init__(self):
        super().__init__()
        self.capacity = 2

    
    