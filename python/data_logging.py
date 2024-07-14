import logging

logging.basicConfig(filename='logs/flight_data.log', level=logging.INFO)

def log_data(message):
    logging.info(message)
