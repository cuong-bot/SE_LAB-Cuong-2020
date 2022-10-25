from app import sale_app
from flask import render_template, request
from app import dao


@sale_app.route('/')
def index():
    cate = dao.load_categories()
    cate_id = request.args.get('category')
    proc = dao.load_products(category_id=cate_id if cate_id else 1)
    return render_template('index.html', categories=cate, products=proc)


if __name__ == '__main__':
    sale_app.run(debug=True)
