# import required module
import os
# assign directory
import re

directory = './inputs_test'

# iterate over files in
# that directory
for filename in os.listdir(directory):
    if "day" in filename:
        n = filename.split('day')[1].split(".txt")[0]
        n = "%02d" % (int(n[:-1])) + n[-1]
        new_name = f"day_{n}.txt"

        fo = os.path.join(directory, filename)
        fn = os.path.join(directory, new_name)
        os.rename(fo, fn)
        # checking if it is a file
        # if os.path.isfile(f):
        #     print(f)