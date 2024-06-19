from calculate.controller import Controller
from calculate.view import View
from calculate import view


class MockView:
    get_user_input_counter = 0
    print_result_call = []

    @staticmethod
    def print_menu():
        pass     

    @staticmethod
    def get_user_input(input_msg):        
        # On veut faire 
        # 1 -> addition
        # 42+100 
        # 5 pour quitter
        
        MockView.get_user_input_counter += 1
        
        if MockView.get_user_input_counter == 1:
            return "1"
        
        if MockView.get_user_input_counter == 2:
            return "42+100"
        
        return "5"

    @staticmethod
    def end_message(): 
        pass
    
    @staticmethod
    def continue_message():
       pass

    @staticmethod
    def print_result(operation, result):
        MockView.print_result_call += [(operation, result)]
        

def test_run(mocker):
    sut = Controller()
    mocker.patch.object(View, 'print_menu', MockView.print_menu)
    mocker.patch.object(View, 'get_user_input', MockView.get_user_input)
    mocker.patch.object(View, 'end_message', MockView.end_message)
    mocker.patch.object(View, 'continue_message', MockView.continue_message)
    mocker.patch.object(View, 'print_result', MockView.print_result)
    sut.run()
    assert len(MockView.print_result_call) == 1
    assert MockView.print_result_call[0] == ("42+100", 142.0)

