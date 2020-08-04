# Created by Yoo Ju Jin(jujin@100fac.com) 
# Created Date : 2020/08/03
# Copyright (C) 2020, Centum Factorial all rights reserved.
from flask import Flask, render_template, request, redirect
from werkzeug.exceptions import BadRequest, NotFound

from chapter1 import models

app = Flask(__name__, template_folder='views')


@app.route("/")
def index():
    return render_template('main_page.html')


@app.route("/shorten/")
def shorten():
    full_url = request.args.get('url')
    if not full_url:
        raise BadRequest()

    url_model = models.Url.shorten(full_url)
    short_url = request.host + '/' + url_model.short_url
    return render_template('success.html', short_url=short_url)


@app.route('/<path:path>')
def redirect_to_full(path=''):
    url_model = models.Url.get_by_short_url(path)
    if not url_model:
        raise NotFound()
    return redirect(url_model.full_url)


if __name__ == '__main__':
    app.run(debug=True)
