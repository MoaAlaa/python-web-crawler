import os


# Each Website You Crawl Is Separate Project (Directory)
def create_project_dir(directory):
	if not os.path.exists(directory):
		print("Creating Project " + directory)
		os.makedirs(directory)

# Create Queue And Crawled Files (If Not Exists)
def create_data_files(project_name, base_url):
	queue = project_name + 'queue.txt'
	crawled = project_name + 'crawled.txt'
	if not os.path.isfile(queue):
		write_file(queue, base_url)
	
	if not os.path.isfile(crawled):
		write_file(crawled, '')

# Create New File
def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()
