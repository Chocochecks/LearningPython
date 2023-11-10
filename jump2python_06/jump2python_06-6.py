import os

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname,filename)
        if os.path.isdir(full_filename):
            search(full_filename)
        else:
            if os.path.splitext(full_filename)[-1] == ".py":
                print(full_filename)

dirname = input("Enter the directory:")
search(dirname)