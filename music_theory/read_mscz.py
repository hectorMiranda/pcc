import zipfile
import xml.etree.ElementTree as ET

def extract_mscz_info(file_path):
    # Open the .mscz file as a zip archive
    with zipfile.ZipFile(file_path, 'r') as z:
        # List the contents of the archive
        print("Contents of the archive:")
        for file_name in z.namelist():
            print(file_name)
        
        # Assuming the XML file is named 'score.xml'
        xml_file_name = 'score.xml'
        if xml_file_name in z.namelist():
            # Extract the XML file
            xml_content = z.read(xml_file_name)
        else:
            print(f"The file '{xml_file_name}' was not found in the archive.")
            return

    # The rest of the function remains the same


    # You can add more fields to extract as needed, such as tempo, time signature, etc.

if __name__ == '__main__':
    file_path = './mscz/Stay.mscz'
    extract_mscz_info(file_path)
