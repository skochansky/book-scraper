# PSL
import os

# Third part
from flask import render_template, redirect, request, url_for, send_file, \
    session, flash

# Own
from . import SERVER_BLUEPRINT
from ..services.helpers import (
    convert_url,
    pass_headers_information,
    extract_book_name,
    create_pdf,
    create_image_list,
    create_input_data,
    separate_list_for_values,
    scrap_data,
    OPERATION_PATH,
    clear_downloaded_files,
)
from .forms import LoginForm, BookForm, AfterSubmit

# CONST
LOGIN_PAGE: str = "app_server.login"
DASHBOARD: str = "app_server.dashboard"


@SERVER_BLUEPRINT.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        session.permanent = True
        session.update({"nick": request.form.get("username")})
        flash("You have logged in correctly", "success")
    elif request.method == "GET" and "nick" not in session:
        return render_template("login.html", form=form)
    return redirect(url_for(DASHBOARD))


@SERVER_BLUEPRINT.route("/logout")
def logout():
    try:
        session.pop("nick")
        return redirect(url_for(LOGIN_PAGE))
    except KeyError:
        return redirect(url_for(LOGIN_PAGE))


@SERVER_BLUEPRINT.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    try:
        form = BookForm()
        if request.method == "POST":
            try:
                session["book_url"]: str = request.form.get('book_url')
                session["number_of_pages"]: int = \
                    int(request.form.get("number_of_pages"))
                cookie: str = request.form.get("cookie")
                session["refer"]: str = request.form.get("refer")
                session["book_name"]: str = extract_book_name(session["refer"])
            except ValueError:
                flash(f"You provide wrong Value", "warning")
                return redirect(url_for(DASHBOARD))
            except IndexError:
                flash("You provide wrong Referer", "warning")
                return redirect(url_for(DASHBOARD))
            # Update the headers.yaml
            pass_headers_information(session["refer"], cookie)
            return redirect(url_for("app_server.after_submit"))

        return render_template("main.html", form=form, nickname=session["nick"])
    except KeyError:
        return redirect(url_for(LOGIN_PAGE))


@SERVER_BLUEPRINT.route("/after_submit", methods=["GET", "POST"])
def after_submit():
    form = AfterSubmit()
    if request.method == "POST":
        if request.form["download"]:
            input_data = create_input_data(
                session["number_of_pages"], convert_url(session["book_url"])
            )
            print(input_data)
            image_list = create_image_list(session["number_of_pages"])
            chunks = separate_list_for_values(input_data, 50)
            print(chunks)
            scrap_data(chunks)
            create_pdf(session["book_name"], image_list)
            clear_downloaded_files()
            return redirect(
                url_for("app_server.download_pdf",
                        file_name=session["book_name"])
            )
        elif request.form["previous_page"]:
            return redirect(url_for("app_server.dashboard"))
    return render_template(
        "after_submit_main_form.html",
        form=form,
        book_name=session["book_name"],
        nickname=session["nick"],
    )


@SERVER_BLUEPRINT.route("/download_pdf/<file_name>", methods=["GET"])
def download_pdf(file_name):
    path: str = os.path.join(OPERATION_PATH, f"{file_name}.pdf")
    return send_file(path, as_attachment=True)
