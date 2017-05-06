import zipfile
#zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref = zipfile.ZipFile("code.zip", 'r')
#zip_ref.extractall(directory_to_extract_to)
zip_ref.extractall(r"C:\Users\b.doddahulugappa\Documents\python35\python35\code")
zip_ref.close()
