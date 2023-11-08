# This is a mock database with some assumptions
# 1: Queue must run independently (not controlled by anything else)
# 2: Queue must have an interface to interact with that enables:
#   Interface to add to queue (M3: load (mockDB(seperatefile) + mockNoise(hardcoded))) (possible shuffle), key is name (M3: assumption no two patients have the same name),
#   (COMPLETE) print list of users (debug purposes super simple m3) 
#   (COMPLETE) TO BE TREATED LIST (TBTL) -> implements kick 
#   (M4: Kick cond. 1: Timeout 2: Confirm treated)
#   (COMPLETE) TBTL.kick(patient) -> remove patient from TBTL, then dequeue item on queue and put into TBTL
#   (COMPLETE) for now M3; have kick place patient at end of queue (infinite loop)

import json

file_path = "mockDB.json"

with open(file_path, 'r') as openfile:
  data = json.load(openfile)


class ED_List:
  def __init__(self):
    self.list = []

  def is_empty(self):
    return len(self.list) == 0
  
  def add(self, item):
    self.add.append(item)
  
  def remove(self, key):
    for key in self.list:
      item = self.list.remove(key)
      return item

  def size(self):
    return len(self.list)
  
  def print(self):
    print(self.list)
   

class Queue(ED_List):
  def __init__(self):
    super.__init__()
    
  # enqueue function is not meant to be a duplicate of the add() function of ED_lists
  # future implementation would implement a smarter insertion of elements into the queue
  # future implementation goal is to use smarter insertion to implement a priority queue
  def enqueue(self, patient):
    self.list.append(patient)
  
  def dequeue(self):
    if not self.is_empty():
      return self.list.pop(0)
    else:
      return None

class TBTL(ED_list):
  def __init__(self, capacity):
    super.__init__()
    self.capacity = capacity
    self.queue = Queue()
  
  def add(self, item):
    if len(self.list) >= capacity:
      print("TBTL is full");
    else:
      self.list.append(item)
  
  def kick(self, key):
    # if infinite loop of patients isn't required, remove the patient variable
    patient = self.remove(key)
    # temporary infinite loop of rotating patients for development/demonstration purposes
    self.queue.enqueue(patient)
    
    patient = self.queue.dequeue()
    if patient != None:
      self.add(patient)


def main():
  print(openfile)



if __name__ == "__main__":
    main()
