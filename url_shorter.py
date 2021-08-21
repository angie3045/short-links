from flask import Flask, request, render_template, redirect

app = Flask(__name__)

base_62_to_url = dict() # Dictionary that stores base62 to long URL


def base_62_encode(string):
    """
    Encodes the string (on this case URL) to base 62
    :param string: string to encode
    :return: encoding result
    """
    deci = len(string)
    s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str_out = ""
    while deci > 0:
        str_out = s[int(deci % 62)] + str_out
        deci = int(deci / 62)
    return str_out


@app.route("/")
def index():
    """
    Just shows the main page
    :return:
    """
    return render_template("index.html", short_url="")


@app.route('/<short>', methods=['GET'])
def decode_url(short):
    """
    Finds the long url based on the short URL and redirects the page to it
    :param short:
    :return:
    """
    # We need to find the URL and redirect to that
    print(short)
    url = base_62_to_url[short]
    return redirect(url)


@app.route('/', methods=['POST'])
def encode_url():
    """
    Gets triggered when clicking submit.
    Gets the long URL, applies the base62 encoding and stores it in our dictionary
    It also generates the url to display on the front end as shot_url variable
    :return:
    """
    url = request.form['text']
    short_url = base_62_encode(url)
    base_62_to_url[short_url] = url
    return render_template("index.html", short_url=request.url + short_url)
