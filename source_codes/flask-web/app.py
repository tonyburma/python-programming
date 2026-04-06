from flask import Flask, render_template

app = Flask(__name__)

# Mock Data: In a real app, this would come from a database!
product_list = [
    {"name": "Vintage Camera", "price": "$120", "description": "A classic film camera for enthusiasts."},
    {"name": "Leather Journal", "price": "$25", "description": "Hand-stitched with recycled paper."},
    {"name": "Wireless Headphones", "price": "$89", "description": "Noise-canceling and ergonomic."},
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    # We pass the 'product_list' variable to the HTML template
    return render_template('products.html', products=product_list)

if __name__ == '__main__':
    app.run(debug=True)