import os

# Each Website You Crawl Is Seperate Project (Directory)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating Project " + directory)
        os.makedirs(directory)

create_project_dir('test')