import os

def get_text_file_metadata():
    if os.path.exists("file:///C:/Users/DELL/Documents/jagdambabill.pdf"):
        file_metadata = {
            'File Name': os.path.basename("file:///C:/Users/DELL/Documents/jagdambabill.pdf"),
            'File Size': os.path.getsize("file:///C:/Users/DELL/Documents/jagdambabill.pdf"),
            'Creation Time': os.path.getctime("file:///C:/Users/DELL/Documents/jagdambabill.pdf"),
            'Last Modified Time': os.path.getmtime("file:///C:/Users/DELL/Documents/jagdambabill.pdf"),
        }

        return file_metadata
    else:
        return None
    
text_file_path = 'example.txt'
text_metadata = get_text_file_metadata()
if text_metadata:
    print("Metadata for textfile: ")
    for key, value in text_metadata.items():
        print(f"{key}: {value}")
else:
    print("File not found")