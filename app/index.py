""" Routing and Start the application """
from flask import render_template, request
from . import app
from . import dao


@app.route('/')
def index():
    """ Route index page (home) """
    cate = dao.load_categories()
    cate_id = request.args.get('category_id')
    kw = request.args.get('keyword')
    proc = dao.load_products(category_id=cate_id, kw=kw)
    return render_template('index.html',  products=proc, categories=cate)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    p = dao.get_product_by_id(product_id)
    return render_template('details.html', product=p)

if __name__ == '__main__':
    app.run(debug=True)
