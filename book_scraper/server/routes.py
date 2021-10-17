# Third part
from flask import render_template, redirect, request, url_for, send_file

# Own
from . import SERVER_BLUEPRINT
from ..services.helpers import convert_url, pass_headers_information,\
    extract_book_name, download_pdf


@SERVER_BLUEPRINT.route("/index", methods=["GET", "POST"])
def index():
    return render_template("index.html"), 200


@SERVER_BLUEPRINT.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":  ### 1
        email = request.form['email']  ### 2
        password = request.form['password']  ###
        return redirect(url_for("app_server.main"))
    return render_template("login.html")


@SERVER_BLUEPRINT.route("/main", methods=["GET", "POST"])
def main():
    pass_headers_information('Referer', "Cookie")
    if request.method == "POST":
        book_url: str = request.form['book_url']
        file_name: str = request.form['file_name']
        number_of_pages: int = int(request.form['number_of_pages'])
        resolution: int = int(request.form['page_quality'])
        #TODO CREATE VIA PARAMTERS

        # create_pdf(number_of_pages, image_list=create_image_list(qwert))
        book_url = convert_url(book_url)
        # print(book_url)
        print(file_name)
        print(number_of_pages)
        print(resolution)
        #session['book_url'] = book_url
        #session['book_name'] = extract_book_name(book_url)
        book_name = extract_book_name(book_url)
        return redirect(url_for("app_server.after_submit",
                                book_name=book_name))
    return render_template("main.html")

@SERVER_BLUEPRINT.route("/after_submit", methods=["GET", "POST"])
def after_submit():
    book_name = request.args.get("book_name")
    file_name = "test"
    if request.method == "POST":
        if request.form.get('download'):
            # TODO download a PDF as file.

            print("You downloaded the PDF")

        elif request.form.get('add_database'):
            print("You added to database")
        elif request.form.get('delete'):
            return redirect(url_for("app_server.main"))

    return render_template("after_submit_main_form.html", book_name=book_name)

@SERVER_BLUEPRINT.route("/download-pdf")
def download_pdf():
    path = "test.pdf"
    return send_file(path, as_attachment=True)