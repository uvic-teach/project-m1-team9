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


def main():
  print(openfile)



if __name__ == "__main__":
    main()
