import os
from lab6_logger import logged

class FileNotFound(Exception):
    pass

class FileCorrupted(Exception):
    pass

class FileHandler:
    @logged(exception=FileNotFound)
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(file_path):
            raise FileNotFound(f"File '{file_path}' not found")

    @logged(exception=FileCorrupted)
    def read(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                return lines
        except Exception as e:
            raise FileCorrupted(f"Cannot read file: {e}")

    @logged(exception=FileCorrupted)
    def write(self, text):
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                f.write(text)
        except Exception as e:
            raise FileCorrupted(f"Cannot write to file: {e}")

    @logged(exception=FileCorrupted)
    def add(self, text):
        try:
            with open(self.file_path, "a", encoding="utf-8") as f:
                f.write("\n" + text)
        except Exception as e:
            raise FileCorrupted(f"Cannot append to file: {e}")

    @logged(exception=FileCorrupted)
    def clear(self):
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                f.write("")
        except Exception as e:
            raise FileCorrupted(f"Cannot clear file: {e}")

    @logged(exception=FileCorrupted)
    def delete_line(self, line_num):
        try:
            lines = self.read()
            if 1 <= line_num <= len(lines):
                del lines[line_num - 1]
                self.write("".join(lines))
            else:
                raise IndexError("Line number out of range")
        except Exception as e:
            raise FileCorrupted(f"Cannot delete line: {e}")

    @logged(exception=FileCorrupted)
    def edit_line(self, line_num, new_text):
        try:
            lines = self.read()
            if 1 <= line_num <= len(lines):
                lines[line_num - 1] = new_text + "\n"
                self.write("".join(lines))
            else:
                raise IndexError("Line number out of range")
        except Exception as e:
            raise FileCorrupted(f"Cannot edit line: {e}")

def show_help():
    print("\nAvailable commands:")
    print(" read   - read file with line numbers")
    print(" write  - rewrite file completely")
    print(" add    - add text to file")
    print(" clear  - delete ALL content from file")
    print(" delete - delete one line by number")
    print(" edit   - edit one line by number")
    print(" help   - show this list")
    print(" exit   - exit program")

def main():
    print("Basic Word Processor")
    file_path = "lab6_file.txt"
    
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found.")
        choice = input("Do you want to create a new file? (y/n): ").strip().lower()
        if choice == 'y':
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("")
                print(f"File '{file_path}' has been created.")
            except Exception as e:
                print(f"Failed to create file: {e}")
                return
        else:
            print("Exiting program.")
            return

    fh = FileHandler(file_path)
    show_help()

    while True:
        command = input("\nInput Command: ").strip().lower()

        try:
            if command == "read":
                os.system('cls')
                lines = fh.read()
                if not lines:
                    print("[File is empty]")
                else:
                    for i, line in enumerate(lines, 1):
                        print(f"{i}. {line.rstrip()}")

            elif command == "write":
                os.system('cls')
                text = input("Input text: ")
                fh.write(text)
                print("File was rewrited.")

            elif command == "add":
                os.system('cls')
                text = input("Input text: ")
                fh.add(text)
                print("Text was added.")

            elif command == "clear":
                os.system('cls')
                fh.clear()
                print("File was cleared.")

            elif command == "delete":
                os.system('cls')
                lines = fh.read()
                if not lines:
                    print("[File is empty]")
                    continue
                for i, line in enumerate(lines, 1):
                    print(f"{i}. {line.rstrip()}")
                try:
                    line_num = int(input("\nEnter line number to delete: "))
                    fh.delete_line(line_num)
                    print(f"Line {line_num} was deleted.")
                except ValueError:
                    print("Invalid number.")
                except IndexError as e:
                    print(e)

            elif command == "edit":
                os.system('cls')
                lines = fh.read()
                if not lines:
                    print("[File is empty]")
                for i, line in enumerate(lines, 1):
                    print(f"{i}. {line.rstrip()}")
                try:
                    line_num = int(input("\nEnter line number to edit: "))
                    new_text = input("Enter new text: ")
                    fh.edit_line(line_num, new_text)
                    print(f"Line {line_num} was updated.")
                except ValueError:
                    print("Invalid number.")
                except IndexError as e:
                    print(e)

            elif command == "help":
                os.system('cls')
                show_help()

            elif command == "exit":
                print("Exit...")
                break

            else:
                print("Incorrect command, try again.")

        except FileCorrupted as e:
            print(f"File operation failed: {e}")

if __name__ == "__main__":
    main()
