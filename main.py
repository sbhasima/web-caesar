from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
    
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form method ="post">
            <label>Rotated by:
                <input type= "text" name= "rot" value ='0' />
            </label>
                <textarea type= "textarea" name= "text" /></textarea>
            
            <input type="submit"/>

      </form>
    </body>
</html>

"""


@app.route("/")
def index():
    return form
    #return "hello World"

@app.route("/",  methods=['POST'])
def encrypt():
    rotated_by = int(request.form["rot"])
    text = request.form["text"]
    rotated_text = rotate_string(text, rotated_by)
    result = '<h1>' + rotated_text + '</h1>'
    return result

app.run()   