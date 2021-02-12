from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['firstname']
    lastname_from_form = request.form['lastname']
    email_from_form = request.form['email']
    newsletter_check = request.form.get('publicidadcheck') 
    nota_from_form = request.form['exampleRadios']

    if newsletter_check == None:
        newsletter_check = "no"
    else:
        newsletter_check = "si"


    return render_template("result.html", name_on_template=name_from_form, lastname_on_template=lastname_from_form, email_on_template=email_from_form, newsletter = newsletter_check, nota_on_template = nota_from_form)

if __name__ == "__main__":
    app.run(debug=True)
