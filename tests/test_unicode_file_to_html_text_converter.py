import pytest
from approvaltests import verify, Options

from html_converter_kata.unicode_file_to_html_text_converter import UnicodeFileToHtmlTextConverter


class TestUnicodeFileToHtmlTextConverter:

    @pytest.fixture(autouse=True)
    def setup_reporter(self, intellij_diff_reporter):
        self.reporter = intellij_diff_reporter

    def test_html_converter(self):
        file_to_convert = "test_file.txt"
        converter = UnicodeFileToHtmlTextConverter(file_to_convert)

        converted_text = converter.convert_to_html()

        verify(
            converted_text,
            options=Options().with_reporter(self.reporter)
        )
