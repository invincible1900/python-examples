import os
import glob

for file in glob.glob('*'):
    print(os.path.splitext(file)[0], os.path.splitext(file)[1])