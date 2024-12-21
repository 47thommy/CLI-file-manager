import cmd
import os


class FileManagerCLI(cmd.Cmd):
    prompt = "fileMngr>>"
    intro = 'welcome to FileManagerCLI, type "help" to see all available commands'

    # initialize our cli file manager with the current working directory
    def __init__(self):
        super().__init__()
        self.current_directory = os.getcwd()

    # define our list command

    def do_list(self, list):
        """list files and directories in the current directory"""
        files_and_dirs = os.listdir(self.current_directory)
        for item in files_and_dirs:
            print(item)

    # define our quit command

    def do_quit(self, line):
        """Exit the CLI"""
        return True

    def do_change_dir(self, directory):
        """change the current directory"""
        new_dir = os.path.join(self.current_directory, directory)

        if os.path.exists(new_dir) and os.path.isdir(new_dir):
            self.current_directory = new_dir
            print(f"Directory changed to {self.current_directory}.")
        else:
            print(f"Directory {directory} does not exist.")

    def postcmd(self, stop, line):
        print()  # add an empty line for better readability
        return stop


if __name__ == "__main__":
    FileManagerCLI().cmdloop()
