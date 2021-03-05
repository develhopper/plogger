#!/usr/bin/env python3

import sys

sys.path.append("../plogger")

from plogger import Logger
from plogger import LoggerInterface

class Log2File(LoggerInterface):
    
    __file_path=None
    append=True

    def __init__(self,file_path="log.txt",append=True):
        self.__file_path=file_path
        self.append=append

    def write(self,message):
        message+="\r\n"
        mode="w"
        if self.append:
            mode="a"
        with open(self.__file_path,mode) as log_file:
            log_file.write(message)



logger=Logger()

output=Log2File()
# output.append=False

logger.log("WARNING"," this is a warning")

logger.setOuput(output)

logger.info("this is just an info")
logger.warning("but this is a warning")
logger.error("and this is an error")
