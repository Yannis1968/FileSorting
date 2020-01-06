# FileSorting 
---
FileSorting contains three .py programs. The first two (CleanUp.py and YannCleanUp.py) work once and the third one 
works constantly in the background until you shut it down.
What they do is, move files of certain extension from the origin file to a destination file and sort them by year
and month of creation (CleanUp.py) and by year, month and day of creation the other two (YannCleanUp.py and yansWatcher.py).
All you have to do to make them work for you is to determine the **origin_path** and **destination_path** variables and
create in the destination_path folder all the subfolders that are stated in the **file_type_dict** dictionary as values.
---
## My Intention
Later on I will try to make a simple UI to let the user determine the origin_path and destination_path from there, so that 
it will be easy to turn this as an .exe and distribute it, even to non-Python-users.
We'll see about that.
