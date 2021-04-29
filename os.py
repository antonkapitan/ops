import os
import time

# print(os.listdir("."))

# print(os.scandir("/Users/akapit/Documents/ss/ops"))
for i in os.scandir("/Users/akapit/Documents/ss/rrr/"):
    print(i)

    # print(i)
    # print(os.stat(i).st_mtime)
    # print(os.stat(i).st_ctime)
    # print(os.stat(i).st_atime)

old = time.time() - (5 * 24 * 60 * 60)
# print(old)
# print(os.path.dirname(i))


# full_name = path.basename(r'C:\python3\file.tar.gz ')
# name = path.splitext(full_name)[0]
# print(name)
