# FamilarizeWithJinja
In this code you'll get familiar with Jinja, a fast expressive template engine from Flask
Flask Blog and Guessing App

Description:
This Flask application features:

    Blog Home Page: Displays a list of blog posts fetched from an external API.
    Guessing Page: Predicts and shows the gender and age of a person based on their name using external APIs.
    Blog Detail Page: Shows detailed information for each blog post.

Technologies Used:

    Flask: A micro web framework for Python.
    Requests: A library for making HTTP requests.
    HTML/CSS: For front-end design.

File Structure:

    app.py: The main application file.
    templates/: Contains HTML templates (index.html, guess.html, blog.html).
    static/: For static files like CSS and JavaScript.
    requirements.txt: List of dependencies.

Usage:

    Home Page: Visit http://127.0.0.1:5000/ to view the list of blog posts.
    Guessing Page: Visit http://127.0.0.1:5000/guess/<name> to predict the gender and age based on a name. Replace <name> with the desired name.
    Blog Detail Page: Visit http://127.0.0.1:5000/blog/<num> to view detailed information about each blog post. Replace <num> with the blog post number.
