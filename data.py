import configparser
import os
import logging

# Change this as desired:
settings_file = "settings.cfg"

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    )

config = configparser.ConfigParser(interpolation=None)
config.read(settings_file)

if not os.path.exists(settings_file):
    logging.critical("Settings file '" + settings_file +
                     "' could not be found.")
    raise FileNotFoundError

api_id = int(config["settings"]["api_id"])
api_hash = str(config["settings"]["api_hash"])
delay_seconds = int(config["settings"]["delay_seconds"])
