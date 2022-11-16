""" Routing and Start the application """
from flask import render_template, request
from . import app
from . import dao


@app.route('/')
def index():
    """ Route index page (home) """
    cate = dao.load_categories()
    cate_id = request.args.get('category')
    proc = dao.load_products(category_id=cate_id if cate_id else 1)
    return render_template('index.html', categories=cate, products=proc)


if __name__ == '__main__':
    app.run(debug=True)
