##we'll make custom exception
import sys
import os

# Append 'src' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from mlproject.logger import logging 

def error_message_detail(error,error_detail:sys): ##this fun to give us errors in details as not done in sys
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename ##from exc_tb we get file name and everything req, i.e. wherever the exceptions occurs we'll get the filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
    ##{0} will be replaced by file name, {1} will be replaced by exc_tb, {2} will be replaced by error

    return error_message




class CustomException(Exception):
    def __init__(self,error_message,error_details:sys): ##initialization constructor
        ##custom excception is inheriting exception
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details)  ##this is the fun that will bring the error message
    def __str__(self):
        return self.error_message