import json


def test_login_page(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"login" in response.data


def test_login_page_post(test_client):
    response = test_client.post("/")
    assert response.status_code == 302


def test_dashboard_page(test_client):
    response = test_client.get("/dashboard")
    assert response.status_code == 302


def test_dashboard_page_post(test_client):
    data = {
        "book_url": "https://biblio.ebookpoint.pl/index.php/cshelf/zine?doc"
        "=f054785d2bfe614a8d6a193201df5be5&format=jpg&page=2"
        "&resolution=200",
        "number_of_pages": 5,
        "cookie": "Apache=361e4791.5c898534c660d; "
        "_ga=GA1.2.846913163.1627931426; "
        "Apache=185.129.114.194.1630694419782452; "
        "_gid=GA1.2.1229856109.1635722110; "
        "_gcl_au=1.1.462960876.1635722110; _gat=1; "
        "biblio=d27009f747fdd6e6c36b884262596f511acf19c8; "
        "sf_frontend=tughpf7vuuumtvceak09u7b246",
        "referer": "https://biblio.ebookpoint.pl/153901/zaawansowany-python"
        "-jasne-zwiezle-i-efektywne-programowanie-luciano-ramalho"
        "/czytaj-pozycje.html",
    }
    response = test_client.post(data=json.dumps(data))
    assert response.status_code == 302


def test_after_submit_page(test_client):
    response = test_client.post("/")
    assert response.status_code == 302


def test_after_submit_page_post(test_client):
    response = test_client.post("/")
    assert response.status_code == 302


def test_logout_page_post(test_client):
    response = test_client.post("/logout")
    assert response.status_code == 405
