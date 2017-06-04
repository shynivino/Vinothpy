import pip

def install(package):
	for pack in package:
		pip.main(['install', pack])

	print("installed successfully")
# Example
if __name__ == '__main__':
    install(['xlrd','openpyxl'])
	