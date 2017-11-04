from flask import Flask, redirect
import requests

PORT = 80

SHEET_ID = '15iEWBgYIL_K1Q71O3VWzifSvzpxMW-bW_BBDXLm0eFs'
DB_URL = ('https://docs.google.com/spreadsheets/d/{0}/export'
          '?format=csv&id={0}&gid=0').format(SHEET_ID)

app = Flask(__name__)


def look_up_long_url(path):
    csv = requests.get(DB_URL).text
    mappings = dict(mapping.split(',') for mapping in csv.split('\r\n'))
    return mappings[path]


@app.route('/<path>')
def handler(path):
    return redirect(look_up_long_url(path))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
