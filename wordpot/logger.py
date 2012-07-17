#!/usr/bin/env python

from wordpot import app
import logging
import logging.handlers

LOGGER = logging.getLogger('wordpot-logger')

def logging_setup():
    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(message)s')

    # File handler
    fh = logging.handlers.RotatingFileHandler('logs/wordpot.log', 'a', 2097152, 10)
    fh.setFormatter(formatter)

    # Add handlers
    LOGGER.addHandler(fh)
   
    # Set level
    LOGGER.setLevel(logging.INFO)
    return True
