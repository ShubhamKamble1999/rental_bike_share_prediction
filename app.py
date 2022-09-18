import sys
from bike.logger import logging
from bike.exception import BikingException
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    try:
        raise Exception(" Testing ----->")
    except Exception as e:
        biking = BikingException(e,sys)
        logging.info(biking.error_message)
        logging.info("I am testing")
    return "CI CD pipeline estabilish"

    


if __name__ == "__main__":
    app.run(debug=True)