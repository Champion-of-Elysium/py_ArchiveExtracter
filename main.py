import PySimpleGUI as gui
from zip_extractor import extractor_archive

gui.theme("LightBlue2")

lable1 = gui.Text("Select archive: ")
input_archive_path = gui.Input()
choose_archive = gui.FileBrowse("Choose", key="archive")

lable2 = gui.Text("Select dest dir: ")
input_dest_dir = gui.Input()
choose_dest_dir = gui.FolderBrowse("Choose", key="folder")

extract_btn = gui.Button("Extract")
output_label = gui.Text(key="output", text_color="yellow")

col1 = gui.Column([[lable1], [lable2]])
col2 = gui.Column([[input_archive_path], [input_dest_dir]])
col3 = gui.Column([[choose_archive], [choose_dest_dir]])

window = gui.Window("Archive Extractor",
                    layout=[[col1, col2, col3], [extract_btn, output_label]])

while True:
    event, value = window.read()
    match event:
        case "Extract":
            try:
                filepath = value['archive']
                folderpath = value['folder']
                extractor_archive(filepath, folderpath)
                window["output"].update(value="Extraction Completed!")
            except FileNotFoundError:
                gui.popup("Forget to select file?!")
        case gui.WIN_CLOSED:
            break

window.close()
