from flask import *
import json,requests
from user_agent import generate_user_agent
app = Flask(__name__)
@app.route('/')
    json_string = json.dumps(data, ensure_ascii=False)
    response = Response(json_string, content_type="application/json; charset=utf-8")
    return response
        
app.run()        
