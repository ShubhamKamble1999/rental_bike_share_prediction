import sys
from bike.logger import logging
from bike.exception import BikingException
from flask import Flask
from bike.config.configuration import Configuration
app = Flask(__name__)
from bike.constant import *
@app.route('/', methods=['GET','POST'])
def index():
    try:
        # raise Exception(" Testing ----->")
        config = Configuration(config_file_path=CONFIG_FILE_PATH)
        result = config.get_data_ingestion_config()
        print("result -> ",result)
        logging.info(result)
    except Exception as e:
        biking = BikingException(e,sys)
        logging.info(biking.error_message)
        logging.info("I am testing")
    return "CI CD pipeline estabilish"

    


if __name__ == "__main__":
    app.run(debug=True)