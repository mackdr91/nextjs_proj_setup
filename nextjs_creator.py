import os
import shutil
import subprocess
import time
from file_content_writer import ( write_layout_content, write_page_content,
                                 write_about_content,
                                 write_services_content, write_contact_content,
                                  write_styles_content, write_taiwind_content,
                                   write_not_found_content )

def get_project_directory():
    project_dir = input("Please enter the path to your Next.js project directory: ")
    if os.path.exists(project_dir) and os.path.isdir(project_dir):
        return project_dir
    else:
        print("The provided path is not valid. Please try again.")
        return get_project_directory()

def create_next_app(project_dir):
    try:
        subprocess.run(["npx", "create-next-app@latest", project_dir], check=True)
        print(f"Successfully created Next.js app in {project_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create Next.js app: {e}")
    time.sleep(5)  # Wait for 5 seconds after creating the app

def remove_directories(project_dir, dirs):
    for dir_name in dirs:
        dir_path = os.path.join(project_dir, dir_name)
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
            print(f"Removed directory: {dir_path}")
        else:
            print(f"Directory not found: {dir_path}")
    time.sleep(3)  # Wait for 3 seconds after removing directories

def create_custom_folders(project_dir, folders):
    for folder_name, content in folders.items():
        folder_path = os.path.join(project_dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path, exist_ok=True)
            print(f"Created folder: {folder_path}")
        else:
            print(f"Folder already exists: {folder_path}")

        if isinstance(content, dict):
            # Handle nested structure
            create_custom_folders(folder_path, content)
        elif isinstance(content, list):
            for item in content:
                if isinstance(item, dict):
                    create_custom_folders(folder_path, item)
                else:
                    # Create files
                    file_path = os.path.join(folder_path, item)
                    if "." in item:  # Assuming it's a file if it contains a dot
                        with open(file_path, "w") as f:
                            f.write("// Your custom content here")
                        print(f"Created file: {file_path}")
                    else:
                        nested_folder_path = os.path.join(folder_path, item)
                        if not os.path.exists(nested_folder_path):
                            os.makedirs(nested_folder_path, exist_ok=True)
                            print(f"Created nested folder: {nested_folder_path}")
                        else:
                            print(f"Nested folder already exists: {nested_folder_path}")
    time.sleep(3)  # Wait for 3 seconds after creating custom folders

def create_env_file(project_dir):
    env_file_path = os.path.join(project_dir, ".env")

    # Check if there's a directory with the same name and remove it
    if os.path.exists(env_file_path) and os.path.isdir(env_file_path):
        shutil.rmtree(env_file_path)
        print(f"Removed existing directory named .env: {env_file_path}")

    # Create the .env file
    with open(env_file_path, "w") as f:
        f.write("# Your custom content here")
    print(f"Created file: {env_file_path}")
    time.sleep(2)  # Wait for 2 seconds after creating the .env file

def install_node_packages(project_dir, packages):
    os.chdir(project_dir)  # Change to the project directory

    # Install packages using npm
    command = ["npm", "install"] + packages
    subprocess.run(command, check=True)
    print(f"Installed packages: {', '.join(packages)} in {project_dir}")



def main():
    project_dir = get_project_directory()

    create_next_app(project_dir)

    BOILERPLATE_DIRS = [
        "app",
        "public",
    ]

    CUSTOM_FOLDERS = {
        "components": [
            "Hero.jsx",
            "Footer.jsx",
            "Navbar.jsx",
            "Card.jsx",
            "CardGrid.jsx",
        ],
        "assets": {
            "images": [],
            "styles": ["globals.css"]
        },
        "config": ["database.js"],
        "models": [],
        "public": [],
        "app": [
            "layout.jsx",
            "page.jsx",
            "not-found.jsx",
            {
                "about": [
                    "page.jsx",
                ],
                "contact": [
                    "page.jsx",
                ],
                "services": [
                    "page.jsx",
                ],

            }


        ],
        "tailwind.config.js": [],
    }

    remove_directories(project_dir, BOILERPLATE_DIRS)
    create_custom_folders(project_dir, CUSTOM_FOLDERS)
    create_env_file(project_dir)

    # Add content to layout.jsx and page.jsx
    write_layout_content(project_dir)
    write_page_content(project_dir)

    # Add content to about and contact pages and services page
    write_about_content(project_dir)
    write_contact_content(project_dir)
    write_services_content(project_dir)
    write_styles_content(project_dir)
    write_taiwind_content(project_dir)
    write_not_found_content(project_dir)

    node_packages = ["react", "react-dom", "tailwindcss", "react-icons", "react-spinners", "react-toastify", "mongodb", "mongoose"]

    install_node_packages(project_dir, node_packages)


    print("Next.js app created successfully!")

    time.sleep(5)

    subprocess.run(["npm", "run", "dev"], cwd=project_dir)

    print("Next.js app started successfully!")

    time.sleep(5)



if __name__ == "__main__":
    main()