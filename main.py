from functools import wraps
from flask import Flask, request, jsonify
from flask_cors import CORS
import app.utils.res_data as res_data
import json
import asyncio

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "API is Alive with new!", 200
@app.route('/info')
def get_account_info():
    uid = request.args.get('uid')
    
    if not uid:
        response = {
            "error": "Invalid request",
            "message": "Empty 'uid' parameter. Please provide a valid 'uid'."
        }
        return jsonify(response), 400, {'Content-Type': 'application/json; charset=utf-8'}


    return_data = asyncio.run(res_data.GetAccountInformation(uid, "7","/GetPlayerPersonalShow"))
    formatted_json = json.dumps(return_data, indent=2, ensure_ascii=False)
    return formatted_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


if __name__ == '__main__':
    app.run(port=3000, host='0.0.0.0', debug=True)
