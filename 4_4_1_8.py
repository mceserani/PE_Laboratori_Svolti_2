""" Find a directory in a tree of directories. """

import os

def find(path, target_dir):
    """ Find a directory in a tree of directories. """
    for root, dirs, files in os.walk(path):
        if target_dir in dirs:
            target_path = os.path.join(root, target_dir)
            print(target_path)

# Example input
path = "../.."
target_dir = "PE_2023_Eventi"

# Call the function to search for the directory and display the results
find(path, target_dir)
