# PSL
from urllib.parse import unquote, urlparse
from pathlib import PurePosixPath

# Third part
from flask import send_file
import re
from PIL import Image
import threading
import yaml
import requests
import io
import os
from PIL import Image
import time
from typing import List

from fpdf import FPDF


def separate_list_for_values(data_list: list, step: int) -> List[str]:
    if isinstance(step, type(None)):
        return data_list

    output_list = []
    for i in range(0, len(data_list), step):
        out_list = data_list[i:i + step]
        output_list.append(out_list)
    return output_list


def parse_output(data, book_dir, headers):
    path = os.path.join(book_dir, f'{data["Page"]}.png')
    resp = requests.get(data['Url'], headers=headers)
    by = resp.content
    image = Image.open(io.BytesIO(by))
    os.makedirs(os.path.join(os.path.abspath(os.path.dirname(path))),
                exist_ok=True)
    # Cropping an image to delete the footer.
    image = image.crop((0, 0, 1100, 1300))
    image.save(path)


def create_image_list(max_page: int) -> List[str]:
    return [str(x) + ".png" for x in range(1, max_page + 1)]


def create_pdf(book_dir: str, image_list: List[str]):
    pdf = FPDF()
    for image in image_list:
        print("done" + image)
        pdf.add_page()
        pdf.image(book_dir + "\\" + image, 0, 0, 210, 297)

    pdf.output(book_dir + ".pdf", "F")
    print("All pdf file is successfully created")


def convert_url(book_url: str) -> str:
    """Convert a book url to validate address for scrap."""
    book_url = re.sub(r'page=[0-9]*', 'page={page}', book_url)
    book_url = re.sub(r'resolution=[0-9]*', 'resolution={resolution}', book_url)
    return book_url


def pass_headers_information(referer: str, cookie: str) -> None:
    """Update headers information in config file"""
    with open('headers.yaml', 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        data['Referer'] = referer
        data['Cookie'] = cookie

    with open("headers.yaml", 'w') as file:
        yaml.dump(data, file)


def extract_book_name(url: str) -> str:
    return PurePosixPath(unquote(urlparse(url).path)).parts[2]


def download_pdf(file_name: str) -> object:
    path = file_name + ".pdf"
    print(path)
    return send_file(path, as_attachment=True)
