import zipfile


def extract_archive(source_path, dest_dir):
    with zipfile.ZipFile(source_path, "r") as file:
        file.extractall(dest_dir)
