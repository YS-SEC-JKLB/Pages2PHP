import os
import base64
index=0
def use(c,f):
		global index
		index = index + 1
		
		then = 'if ($_GET["index"] == %d){ echo '%index
		then += 'base64_decode( '
		then += c.strip('=')
		then += ' );}'
		f.write(then)
def r(rf):
	try:
		with open(rf, "rb") as f:
			content = f.read()
			encoded_content = base64.b64encode(content).decode('utf-8')
		return encoded_content
	except Exception as e:
		print(f"Error reading file {rf}: {e}")
		return None

def ls(directory):
	files = []
	for root, dirs, file_names in os.walk(directory, topdown=False):
		for name in file_names:
			files.append((os.path.join(root, name), name))
	return files

def main(file):
	file.write('''<?php''')
	for file_path, file_name in ls(input('GenShellDir:')):
		encoded_content = r(file_path)
		if encoded_content is not None:
			use(encoded_content,file)
	file.write('?>')
if __name__ == '__main__':
	print('''____________________________  ___ _____________ 
\\ \\ ______   \\ \\ _____  \\ \\ ______   \\ \\ /   |   \\ \\ ______   \\ 
 |     ___//  ____/|     ___/    ~    \\      ___/
 |    |   /       \\ |    |   \\     Y    /    |    
 |____|   \\ \\ _______ \\ \\ ____|    \\ \\ ___|_  /|____|    
                  \\ \\ /               \\ \\ /           ''')
	with open(input('output file:'),'w') as f:
		main(f)