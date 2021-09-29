from book_scraper.services.helpers import (
    create_input_data,
    create_image_list,
    convert_url,
    extract_book_name,
    separate_list_for_values,
)


def test_create_input_data():
    """

    """
    max_page = 1
    link = (
        "https://biblio.ebookpoint.pl/index.php/cshelf/zine?doc"
        "=f054785d2bfe614a8d6a193201df5be5&format=jpg&page={"
        "page}&resolution={resolution}"
    )
    assert create_input_data(max_page, link) == [
        {
            "Page": 1,
            "Url": "https"
            "://biblio.ebookpoint.pl/index.php/cshelf/zine?doc"
            "=f054785d2bfe614a8d6a193201df5be5&format=jpg&page=1"
            "&resolution=1300",
        }
    ]


def test_separate_list_from_values():
    number_of_pages = 1
    url = convert_url(
        "https://biblio.ebookpoint.pl/index.php/cshelf/zine?doc"
        "=f054785d2bfe614a8d6a193201df5be5&format=jpg&page=2&resolution=200"
    )
    data = create_input_data(number_of_pages, url)
    assert separate_list_for_values(data, 50) == [
        [
            {
                "Page": 1,
                "Url": "https://biblio.ebookpoint.pl/index.php/cshelf/zine"
                       "?doc=f054785d2bfe614a8d6a193201df5be5&format=jpg&page"
                       "=1&resolution=1300",
            }
        ]
    ]


def test_create_image_list():
    max_page = 5
    assert create_image_list(max_page) == ["1.png", "2.png", "3.png", "4.png",
                                           "5.png"]


def test_convert_url():
    book_url = "https://biblio.ebookpoint.pl/index.php/cshelf/zine?doc" \
               "=f054785d2bfe614a8d6a193201df5be5&format=jpg&page=2" \
               "&resolution=200"
    assert (
        convert_url(book_url)
        == "https://biblio.ebookpoint.pl/index.php/cshelf/zine?doc"
           "=f054785d2bfe614a8d6a193201df5be5&format=jpg&page={"
           "page}&resolution={resolution}"
    )


def test_extract_book_name():
    url = "https://biblio.ebookpoint.pl/153901/zaawansowany-python-jasne" \
          "-zwiezle-i-efektywne-programowanie-luciano-ramalho/czytaj-pozycje" \
          ".html "
    assert (
        extract_book_name(url)
        == "zaawansowany-python-jasne-zwiezle-i-efektywne-programowanie"
           "-luciano-ramalho"
    )
