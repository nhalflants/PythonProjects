import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("LightBlue")

archive_label = sg.Text("Select archive: ")
archive_input = sg.Input()
choose_archive_button = sg.FileBrowse("Choose", key="archive_file")

dest_label = sg.Text("Select destination directory: ")
dest_input = sg.Input()
choose_dest_button = sg.FileBrowse("Choose", key="dest_folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor",
                   layout=[[archive_label, archive_input, choose_archive_button],
                           [dest_label, dest_input, choose_dest_button],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    source_path = values["archive_file"]
    dest_dir = values["dest_folder"]
    extract_archive(source_path, dest_dir)
    window["output"].update(value="Archive extracted")

window.close()