import zipfile
import xml.etree.ElementTree as ET

def extract_mscz_info(file_path):
    # Open the .mscz file as a zip archive
    with zipfile.ZipFile(file_path, 'r') as z:
        # Assuming the XML file is named 'Stay.mscx'
        xml_file_name = 'Stay.mscx'
        if xml_file_name in z.namelist():
            # Extract the XML file
            xml_content = z.read(xml_file_name)
        else:
            print(f"The file '{xml_file_name}' was not found in the archive.")
            return

    # Parse the XML content
    root = ET.fromstring(xml_content)

    # Extract meaningful information
    info = {}
    info['title'] = root.find('.//work-title').text if root.find('.//work-title') is not None else 'Untitled'
    info['composer'] = root.find('.//creator[@type="composer"]').text if root.find('.//creator[@type="composer"]') is not None else 'Unknown'
    info['key_signature'] = root.find('.//keySig').text if root.find('.//keySig') is not None else 'Unknown'
    info['time_signature'] = root.find('.//timeSig').text if root.find('.//timeSig') is not None else 'Unknown'

    # Extract the first few notes
    notes = root.findall('.//note')
    info['notes'] = [note.find('pitch').text for note in notes[:5]] if notes else []

    # Print the extracted information
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == '__main__':
    file_path = 'mscz/Stay.mscz'
    extract_mscz_info(file_path)

