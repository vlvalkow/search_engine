from pathlib2 import Path
import json


class Filesystem:
    def save(self, file_path, contents):
        contents = json.dumps(contents)
        Path(file_path).write_text(contents)
        pass

    def get(self, file_path):
        file = Path(file_path)

        if not file.is_file():
            return False

        return json.loads(Path(file_path).read_text())
