import sys
import logging

def error_message_details(error, error_details):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_details):
        super().__init__(self.error_message)  
        self.error = error
        self.error_details = error_details
        self.error_message = error_message_details(error, error_details)
          

    def __str__(self):
        return self.error_message

# if __name__ == '__main__':
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by zero error")
#         raise CustomException(e, sys)
    
