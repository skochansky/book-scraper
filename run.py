from book_scraper import create_app

APP = create_app()

if __name__ == '__main__':
    APP.run(debug=True, host="0.0.0.0", port=5000)
