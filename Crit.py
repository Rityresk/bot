from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def form_sample():
    return '''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <title>Привет, Марс!</title>
  </head>
  <body>
    <div class="alert alert-ligh" role="alert">
      <h1>Моё предложение: Марс</h1>
    </div>
    <div class="alert alert-ligh" role="alert">
      Эта планета близка к Земле;
    </div>
    <div class="alert alert-success" role="alert">
      На ней много необходимых ресурсов;
    </div>
    <div class="alert alert-secondary" role="alert">
      На ней есть вода и атмосфера;
    </div>
    <div class="alert alert-warning" role="alert">
      На ней есть небольшое магнитное поле;
    </div>
    <div class="alert alert-danger" role="alert">
      Наконец, она просто красива!
    </div>
  </body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')