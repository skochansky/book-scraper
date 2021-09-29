# PSL
import shutil
from urllib.parse import unquote, urlparse
from pathlib import PurePosixPath, Path

# Third part
import re
import threading
import yaml
import requests
import io
import os
from PIL import Image
from typing import List, Dict
from fpdf import FPDF

# CONST
RESOLUTION = 1300
YAML_FILE = "headers.yaml"
HEADERS = yaml.load(open(YAML_FILE), Loader=yaml.FullLoader)
BOOK_DIR = "Book/"
OPERATION_PATH = Path(__file__).parent.parent.parent


def separate_list_for_values(data_list: list, step: int) -> List[str]:
    if isinstance(step, type(None)):
        return data_list

    output_list = []
    for i in range(0, len(data_list), step):
        out_list = data_list[i : i + step]
        output_list.append(out_list)
    return output_list


def create_input_data(max_page: int, link: str) -> List[Dict]:
    """Create the input data links for scraping."""
    input_data = []
    for page in range(1, max_page + 1):
        url = link.format(page=page, resolution=RESOLUTION)
        input_data.append({"Page": page, "Url": url})
    return input_data


def parse_output(data) -> None:
    """Make the better output of images and crop the images to delete the
    footer """
    path = os.path.join("Book", f'{data["Page"]}.png')
    resp = requests.get(data["Url"], headers=HEADERS)
    by = resp.content
    image = Image.open(io.BytesIO(by))
    os.makedirs(os.path.join(os.path.abspath(os.path.dirname(path))), exist_ok=True)
    # Cropping an image to delete the footer.
    image = image.crop((0, 0, 1300, 1700))
    image.save(path)


def scrap_data(chunks: List[str]) -> None:
    """Main scraping function"""
    i = 0
    for chunk in chunks:
        i += 1
        print(f"Scraping chunk: {i}/{len(chunks)}")
        threads = []
        for url in chunk:
            target_function = parse_output
            thread = threading.Thread(target=target_function, args=(url,))
            threads.append(thread)

        [x.start() for x in threads]
        [x.join() for x in threads]


def create_image_list(max_page: int) -> List[str]:
    """Create list of all images what we scrapped"""
    return [str(x) + ".png" for x in range(1, max_page + 1)]


def create_pdf(file_name: str, image_list: List[str]):
    """Create PDF from the scrapped images."""
    pdf = FPDF()
    for image in image_list:
        print("done: " + image)
        pdf.add_page()
        pdf.image(os.path.join(OPERATION_PATH, "Book/") + image, 0, 0, 210, 297)

    pdf.output(file_name + ".pdf", "F")
    print("All pdf file is successfully created")


def convert_url(book_url: str) -> str:
    """Convert a book url to validate address for scrap."""
    book_url = re.sub(r"page=[0-9]*", "page={page}", book_url)
    book_url = re.sub(r"resolution=[0-9]*", "resolution={resolution}", book_url)
    return book_url


def pass_headers_information(referer: str, cookie: str) -> None:
    """Update headers information in config file"""
    with open(YAML_FILE, "r") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        data["Referer"]: str = referer
        data["Cookie"]: str = cookie

    with open(YAML_FILE, "w") as file:
        yaml.dump(data, file)


def extract_book_name(url: str) -> str:
    """Function to extract the book name from the given url to use as pdf
    name. """
    return PurePosixPath(unquote(urlparse(url).path)).parts[2]


def clear_downloaded_files() -> None:
    """Delete all scrapped images after the PDF is generated."""
    for filename in os.listdir(os.path.join(OPERATION_PATH, BOOK_DIR)):
        filepath = os.path.join(OPERATION_PATH, BOOK_DIR, filename)
        try:
            shutil.rmtree(filepath)
        except OSError: 
            os.remove(filepath)
