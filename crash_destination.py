import json
import os

from configman import Namespace

class CrashDestinationClass(object):
    
    required_config = Namespace()
    
    required_config.add_option(
        'crashstorage_location',
        doc='the location for storing transformed crashes',
        default=None,
    )
    
    def __init__(self, config):
        self.config = config
        
    def save_raw_data(self, file_name, raw_data):
        file_path = os.path.join(self.config.crashstorage_location, file_name)
        with open(file_path, 'w') as f:
            json.dump(raw_data, f)
        
