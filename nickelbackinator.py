from flask import Flask
#from redis import Redis


#redis = Redis()

app = Flask(__name__)

@app.route('/')
def home():
    return 'Here be Nickelback'

# @app.route('/random')
# def random():
#     nickelback = redis.srandmember("nickelbacks", 1)
#     return nickelback.as_json()
