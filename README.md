# FileManagerCLI

FileManagerCLI is a simple command-line interface (CLI) tool for managing files and directories. It provides basic functionalities like listing files, changing directories, creating files, and reading file contents. The tool is built using Python's `cmd` module.

## Features

- **List Files and Directories**: View the contents of the current working directory.
- **Change Directory**: Navigate to different directories within the filesystem.
- **Create File**: Create a new text file in the current directory.
- **Read File**: Display the contents of a text file.
- **Quit**: Exit the CLI.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd FileManagerCLI
   ```

3. Run the script:
   ```bash
   python file_manager_cli.py
   ```

## Usage

When you run the script, you will be greeted with the prompt `fileMngr>>`. Use the following commands to interact with the CLI:

### Commands

- **list**

  - Description: Lists all files and directories in the current directory.
  - Usage:
    ```
    list
    ```

- **change_dir <directory_name>**

  - Description: Changes the current working directory to the specified directory.
  - Usage:
    ```
    change_dir <directory_name>
    ```

- **create_file <filename>**

  - Description: Creates a new text file in the current directory.
  - Usage:
    ```
    create_file <filename>
    ```

- **read_file <filename>**

  - Description: Reads and displays the contents of the specified text file.
  - Usage:
    ```
    read_file <filename>
    ```

- **quit**
  - Description: Exits the CLI.
  - Usage:
    ```
    quit
    ```

## Example Usage

1. List all files and directories:

   ```
   fileMngr>> list
   file1.txt
   dir1
   file2.txt
   ```

2. Change to a subdirectory:

   ```
   fileMngr>> change_dir dir1
   Directory changed to /path/to/dir1.
   ```

3. Create a new file:

   ```
   fileMngr>> create_file newfile.txt
   File newfile.txt created in /path/to/dir1.
   ```

4. Read a file:

   ```
   fileMngr>> read_file newfile.txt
   (contents of newfile.txt)
   ```

5. Quit the CLI:
   ```
   fileMngr>> quit
   ```

## Contributing

Contributions are welcome! If you find any bugs or have feature requests, please open an issue or submit a pull request.

---

Enjoy using FileManagerCLI!
