import html as html_converter


class FileReader:

    def __init__(self, full_filename_with_path: str) -> None:
        self.full_filename_with_path = full_filename_with_path

    def read(self) -> list[str]:
        with open(self.full_filename_with_path, "r") as file:
            return file.readlines()


class UnicodeFileToHtmlTextConverter:

    def __init__(self, full_filename_with_path: str) -> None:
        self.file_reader = FileReader(full_filename_with_path)

    def convert_to_html(self) -> str:
        file_content = self.file_reader.read()

        html = ""
        for line in file_content:
            line = line.rstrip()
            html += html_converter.escape(line, quote=True)
            html += "<br />"

        return html
