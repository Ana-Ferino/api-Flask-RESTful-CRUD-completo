import logging

custom_log = logging.basicConfig(filename='flask.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')