# This is a mock database with some assumptions
# 1: Queue must run independently (not controlled by anything else)
# 2: Queue must have an interface to interact with that enables:
#   Interface to add to queue (M3: load (mockDB(seperatefile) + mockNoise(hardcoded))) (possible shuffle), key is name (M3: assumption no two patients have the same name),
#   print list of users (debug purposes super simple m3) 
#   TO BE TREATED LIST (TBTL) -> implements kick (M4: Kick cond. 1: Timeout 2: Confirm treated)
#   TBTL.kick(patient) -> remove patient from TBTL, then dequeue item on queue and put into TBTL
#   for now M3; have kick place patient at end of queue (infinite loop)

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
      self.list.remove(key)

  def size(self):
    return len(self.list)
  
  def print(self):
    print(self.list)
   

class Queue(ED_List):
  def __init__(self):
    super.__init__()
  
  def enqueue(self, patient):
    self.list.append(patient)
  
  def dequeue(self):
    if not self.is_empty():
      return self.list.pop(0)
    else:
      return None

class TBTL:
  def __init__(self):
    super.__init__()
    self.capacity = 3
  


def main():
  print(openfile)



if __name__ == "__main__":
    main()
