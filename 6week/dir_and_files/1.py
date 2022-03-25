import os
path=input("Input path here: ")
#/Applications/docs/
os.chdir('path')
print(os.listdir())
"""for dirpath, dirnames, filenames in os.walk('/Applications/docs/'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()
    """