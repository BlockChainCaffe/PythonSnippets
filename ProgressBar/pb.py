import time

from tqdm import tqdm                   # Example 1
from alive_progress import alive_bar    # Example 2 / https://github.com/rsalmei/alive-progress

mylist = [1,2,3,4,5,6,7,8]

print("Example 1: ")
# Example 1
for i in tqdm(mylist):
    time.sleep(1)

print("Example 2: ")
# Example 2
with alive_bar(len(mylist)) as bar:
    for i in mylist:
        bar("example2 ")
        time.sleep(1)
