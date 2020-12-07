from flask import *

app = Flask(__name__)

url_black_list = ['%1c', '%1d', '%1f', '%1e', '%20', '%2b', '%2c', '%3c', '%3e']
black_list = ['.', '[', ']', '{{', '=', '_', '\'', '""', '\\x', 'request', 'config', 'session', 'url_for', 'g',
              'get_flashed_messages', '*', 'for', 'if', 'format', 'list', 'lower', 'slice', 'striptags', 'trim',
              'xmlattr', 'tojson', 'set', '=', 'chr']


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'try to check /test?url=xxx'


@app.route('/test', methods=['GET'])
def testing():
    url = request.url
    for black in url_black_list:
        if black in url:
            return '<h1>do a real p1g</h1>'
    url = request.args.get('url')
    for black in black_list:
        if black in url:
            return '<h1>do a real p1g</h1>'
    return render_template_string('<h1>this is your url {}</h1>'.format(url))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8899, debug=True)
