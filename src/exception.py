import os
import sys




class customException(Exception):
    def __init__(self,error_details):
        self.error_details=error_details
        _,_,error_tb=sys.exc_info()
        self.error_message=f"in your file name ({error_tb.tb_frame.f_code.co_filename}) error occurred in line number ({error_tb.tb_lineno}) and error details are ({error_details})"
    def __str__(self):
        return self.error_message
    
    
if __name__=="__main__":
    try :
        a=3/0
        
    except Exception as e:
       raise customException(e)