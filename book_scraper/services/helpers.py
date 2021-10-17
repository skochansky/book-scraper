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
        file.close()

    with open("headers.yaml", 'w') as file:
        yaml.dump(data, file)
        file.close()

def extract_book_name(url: str) -> str:
    url = 'https://biblio.ebookpoint.pl/149181/python-zadania-z-programowania-przykladowe-funkcyjne-rozwiazania-miroslaw-j-kubiak/czytaj-pozycje.html'
    book_name_from_url = re.search(
        r"[^\shttps://biblio.ebookpoint.pl].+?(?=/czytaj-pozycje\.html)", url)
    return book_name_from_url.group()[7:].replace("-", " ")


def download_pdf(file_name: str) -> object:
    path = file_name + ".pdf"
    print(path)
    return send_file(path, as_attachment=True)


