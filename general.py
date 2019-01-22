import os


# Each Website You Crawl Is Separate Project (Directory)
def create_project_dir(directory):
	if not os.path.exists(directory):
		print("Creating Project " + directory)
		os.makedirs(directory)


# Create Queue And Crawled Files (If Not Exists)
def create_data_files(project_name, base_url):
	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'
	if not os.path.isfile(queue):
		write_file(queue, base_url)
	
	if not os.path.isfile(crawled):
		write_file(crawled, '')


# Create New File
def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()


# Append Data To Existing File
def append_to_file(path, data):
	with open(path, 'a') as file:
		file.write(data + '\n')


# Delete The Content Of The File
def delete_file_content(path):
	with open(path, 'w'):
		# Do Nothing
		pass


# Read A File And Convert Each Line To List
def file_to_set(file_name):
	results = set()
	with open(file_name, 'rt') as f:
		for line in f:
			results.add(line.replace('\n', ''))
	return results


# Iterate To A Set, Each item Will be A New Line In The File
def set_to_file(links, file):
	delete_file_content(file)
	for link in sorted(links):
		append_to_file(file, link)
