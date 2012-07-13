#!/usr/bin/env python

import logging

LOGGER = logging.getLogger('wordpot')

def logging_setup():
    # File handler
    fh = logging.FileHandler('wordpot.log')
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    fh.setFormatter(formatter)

    # Add handlers
    LOGGER.addHandler(fh)
   
    # Set level
    LOGGER.setLevel(logging.INFO)
    
    return True
