class FileMaxTriesException(Exception):
    def __init__(self, path_to_file: str) -> None:
        self.msg = f'Cant delete file: {path_to_file}'
        super().__init__(self.msg)
    
    def __str__(self):
        return self.msg
