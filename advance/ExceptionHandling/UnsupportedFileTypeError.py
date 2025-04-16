class UnsupportedFileTypeError(Exception):
    def __init__(self, file_type):
        super().__init__(f"File type '{file_type}' is not supported. Only .txt and .csv allowed.")

def process_file(filename):
    if not (filename.endswith('.txt') or filename.endswith('.csv')):
        raise UnsupportedFileTypeError(filename.split('.')[-1])
    print("Processing file:", filename)

try:
    process_file("data.json")
except UnsupportedFileTypeError as e:
    print("File error:", e)
