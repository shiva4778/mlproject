import os
import sys
class CustomException:
    def __init__(self,error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message
    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
        _,_,exec_tb=error_detail.exc_info()
        line_number=exec_tb.tb_frame.f_lineno
        file_name=exec_tb.tb_frame.file_code.co_file_name
        error_message=f"Error occured in script:[{file_name}] at line number [{line_number}] error_message:[{error_message}]"
        return error_message
    def __str__(self):
        return self.error_message
    def __repr__(self) -> int:
        return CustomException.__name__.str()
    