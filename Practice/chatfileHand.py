from pathlib import Path
import os
import shutil
import csv
import json


# ---------------- Utility Functions ---------------- #

def show_all():
    """Show all files & folders in current directory"""
    p = Path('.')
    items = list(p.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")


def list_folder_contents(folder: Path):
    """List files/folders inside a given folder"""
    if folder.exists() and folder.is_dir():
        print(f"\nContents of {folder}:")
        for f in folder.iterdir():
            print("  ", f.name, "(dir)" if f.is_dir() else "(file)")
    else:
        print("Folder not found.")


# ---------------- Main Operations ---------------- #

def create_folder():
    show_all()
    name = input("Enter Folder Name : ")
    p = Path(name)

    if not p.exists():
        p.mkdir()
        print("✅ Folder Created")
    else:
        print("⚠️ Folder Already Exists")


def read_folder():
    show_all()
    name = input("Enter Folder Name : ")
    list_folder_contents(Path(name))


def update_folder():
    show_all()
    name = input("Enter Folder Name to update: ")
    p = Path(name)

    if not p.exists() or not p.is_dir():
        print("❌ Folder Not Found")
        return

    print("\nUpdate Options:")
    print("1. Rename Folder")
    print("2. List Contents")
    print("3. Move File")
    print("4. Copy File")
    print("5. Add New File")
    print("6. Delete File")

    try:
        res = int(input("Choose an option: "))

        if res == 1:
            new_name = input("Enter New Folder Name: ")
            p.rename(Path(new_name))
            print("✅ Folder Renamed")

        elif res == 2:
            list_folder_contents(p)

        elif res == 3:
            file_to_move = input("Enter file path to move: ")
            dest_folder = input("Enter destination folder path: ")
            shutil.move(file_to_move, dest_folder)
            print("✅ File Moved")

        elif res == 4:
            file_to_copy = input("Enter file path to copy: ")
            dest_folder = input("Enter destination folder path: ")
            shutil.copy(file_to_copy, dest_folder)
            print("✅ File Copied")

        elif res == 5:
            new_file = input("Enter new file name (with extension): ")
            file_path = p / new_file
            with open(file_path, 'w', newline='') as f:
                if file_path.suffix.lower() == ".csv":
                    writer = csv.writer(f)
                    data = [["Name", "Course", "Fee"],
                            ["Yunsu", "DS", "20000"],
                            ["Neha", "DA", "15000"]]
                    writer.writerows(data)
                    print("✅ CSV File Created")
                else:
                    data1 = {"Name": "Yunsu", "Age": 23, "is_adult": True}
                    json.dump(data1, f)
                    print("✅ JSON File Created")

        elif res == 6:
            file_name = input("Enter file name to delete: ")
            file_path = p / file_name
            if file_path.exists():
                file_path.unlink()
                print("✅ File Deleted")
            else:
                print("❌ File does not exist")

        else:
            print("⚠️ Invalid choice.")

    except Exception as e:
        print("⚠️ Error:", e)


def delete_folder():
    show_all()
    name = input("Enter Folder Name to delete: ")
    p = Path(name)

    if p.exists() and p.is_dir():
        shutil.rmtree(p)
        print("✅ Folder Deleted")
    else:
        print("❌ Folder Not Found")


# ---------------- Menu ---------------- #

while True:
    print("\n========= MENU =========")
    print("1. Create Folder")
    print("2. List Folder")
    print("3. Update Folder")
    print("4. Delete Folder")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_folder()
        elif choice == 2:
            read_folder()
        elif choice == 3:
            update_folder()
        elif choice == 4:
            delete_folder()
        elif choice == 5:
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid Option. Try Again.")

    except ValueError:
        print("⚠️ Please enter a valid number.")
