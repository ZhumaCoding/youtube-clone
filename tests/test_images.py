from pathlib import Path
from html.parser import HTMLParser

class ImgSrcParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'img':
            for name, value in attrs:
                if name.lower() == 'src':
                    self.paths.append(value)


def test_all_images_exist():
    root = Path(__file__).resolve().parents[1]
    html_file = root / "youtube.html"
    parser = ImgSrcParser()
    parser.feed(html_file.read_text())

    assert parser.paths, "No <img> tags found"

    for src in parser.paths:
        img_path = root / src
        assert img_path.exists(), f"Missing image file: {src}"
