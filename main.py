from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def home():
    blog_response = requests.get(url="https://api.npoint.io/b69453e72726a7b84bb3")
    all_posts = blog_response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/guess/<name>")
def guessing(name):
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    data = gender_response.json()
    gender = data['gender']
    age_response = requests.get(url=f"https://api.agify.io/?name={name}")
    data = age_response.json()
    age = data['age']

    return render_template("guess.html", gender=gender, name=name, age=age)

@app.route("/blog/<int:num>")
def get_blog(num):
    blog_response = requests.get(url="https://api.npoint.io/b69453e72726a7b84bb3")
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts, num=num-1)


if __name__ == "__main__":
    app.run(debug=True)
