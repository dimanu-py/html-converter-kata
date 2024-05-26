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

    def test_new_line_is_converted_to_br_tag(self, mocker):
        file_path = "dummy_path.txt"
        mocker.patch("html_converter_kata.unicode_file_to_html_text_converter.FileReader.read", return_value=["line1", "line2"])
        converter = UnicodeFileToHtmlTextConverter(file_path)
        expected_html = "line1<br />line2<br />"

        converted_text = converter.convert_to_html()

        assert converted_text == expected_html

    @pytest.mark.parametrize(
        "mocked_content, expected_html",
        [('"line1"', "&quot;line1&quot;<br />"), ("10 < 15", "10 &lt; 15<br />"), ("15 > 10", "15 &gt; 10<br />"),
         ("Cut & Paste", "Cut &amp; Paste<br />")]
    )
    def test_special_characters_are_escaped(self, mocker, mocked_content, expected_html):
        file_path = "dummy_path.txt"
        mocker.patch("html_converter_kata.unicode_file_to_html_text_converter.FileReader.read", return_value=[mocked_content])
        converter = UnicodeFileToHtmlTextConverter(file_path)

        converted_text = converter.convert_to_html()

        assert converted_text == expected_html

    def test_empty_file_is_not_processed(self, mocker):
        file_path = "dummy_path.txt"
        mocker.patch("html_converter_kata.unicode_file_to_html_text_converter.FileReader.read", return_value=[])
        converter = UnicodeFileToHtmlTextConverter(file_path)

        converted_text = converter.convert_to_html()

        assert converted_text == ""
