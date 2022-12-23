import PySimpleGUI as sg
from zip_creator import make_archive

label_select_source = sg.Text("Select files to compress: ")
input_select_source_files = sg.Input()
select_source_files_button = sg.FilesBrowse("Choose", key="source_files")

label_select_dest = sg.Text("Select destination folder: ")
input_select_dest_folder = sg.Input()
select_dest_folder_button = sg.FolderBrowse("Choose", key="dest_folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("File Compressor",
                   layout=[[label_select_source, input_select_source_files, select_source_files_button],
                           [label_select_dest, input_select_dest_folder, select_dest_folder_button],
                           [compress_button, output_label]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Compress":
            filepaths = values["source_files"].split(";")
            dest_folder = values["dest_folder"]
            make_archive(filepaths, dest_folder)
            window["output"].update(value="Compression completed")
        case sg.WIN_CLOSED:
            break

window.close()
