from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/greet/<name>')
def greet(name):
  return render_template('greet.html', name=name)

@app.route('/products')
def products():
  products = [
    {'name': 'Product A', 'price': 10},
    {'name': 'Product B', 'price': 20},
    {'name': 'Product C', 'price': 30}
  ]
  return render_template('products.html', products=products)

if __name__ == '__main__':
  app.run(debug=True)