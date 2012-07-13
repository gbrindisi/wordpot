#!/usr/bin/env python

from wordpot import app
import logging
import logging.handlers

def logging_setup():
    # File handler
    fh = logging.handlers.RotatingFileHandler('logs/wordpot.log', 'a', 2097152, 10)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    fh.setFormatter(formatter)

    # Add handlers
    app.logger.addHandler(fh)
   
    # Set level
    app.logger.setLevel(logging.INFO)
    return True
