from flask import Flask, request, render_template
import requests

app = Flask(__name__)

NEWS_API_KEY = "8cedfd48661e444da6d9ff1c9c8242c7"

@app.route('/')
def home():
    """Menampilkan berita utama di halaman utama"""
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return render_template("index.html", articles=[])

    data = response.json()
    return render_template("index.html", articles=data.get("articles", []))

@app.route('/search', methods=['GET'])
def search_news():
    keyword = request.args.get('q', '')
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return render_template("index.html", articles=[])

    data = response.json()
    return render_template("index.html", articles=data.get("articles", []))

@app.route('/category', methods=['GET'])
def get_news_by_category():
    category = request.args.get('category', 'business')
    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return render_template("index.html", articles=[])

    data = response.json()
    return render_template("index.html", articles=data.get("articles", []))

if __name__ == '__main__':
    app.run(debug=True)
