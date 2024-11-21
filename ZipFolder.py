import os
import zipfile

folder_path = input("Enter the path to the folder you want to zip: ").strip()

if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
    print("Error: The folder does not exist or the path is not a valid directory.")
else:
    # Determine the name of the zip file
    folder_name = os.path.basename(folder_path)
    zip_file_path = os.path.join(os.path.dirname(folder_path), f"{folder_name}.zip")

    # Create the ZIP file
    try:
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Traverse the folder and add files to the zip
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname)
                    print(f"Added {file} to the ZIP archive.")

        print("Folder successfully zipped as:",zip_file_path)
    except PermissionError:
        print("Error: Permission denied while creating the ZIP file.")
    except Exception as e:
        print("An unexpected error occurred:",e)
