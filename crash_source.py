import os

from configman import Namespace

class CrashSourceClass(object):
    app_name = 'crash_source_class'
    app_version = '0.1'
    app_description = 'crash source'
    
    required_config = Namespace()
    
    required_config.add_option(
        'file_location',
        doc='the location of crash files',
        default=None,
    )
    
    def __init__(self, config):
        self.config = config
    
    def new_crashes(self):
        for x in os.listdir(self.config.file_location):
            yield x
            
    def get_file_contents(self, file_name):
        file_path = os.path.join(self.config.file_location, file_name)
        with open(file_path) as my_file:
            return my_file.readlines()