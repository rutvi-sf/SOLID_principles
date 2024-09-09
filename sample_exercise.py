class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, 'r') as file:
            content = file.read()
        print(content)
        return content

    def write_file(self, content):
        with open(self.filename, 'w') as file:
            file.write(content)
        print("Content written to file.")

    def log_to_file(self, message):
        with open('logfile.txt', 'a') as log_file:
            log_file.write(message + '\n')
        print("Logged message.")


file_handler = FileHandler('data.txt')
file_handler.write_file("Hello, world!")
file_handler.read_file()
file_handler.log_to_file("File operations completed.")
