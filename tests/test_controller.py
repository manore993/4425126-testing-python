from calculate.controller import Controller
from calculate.view import View
from calculate import view


class MockView:
    get_user_input_counter = 0
    print_result_call = []
    # run_method_counter = 0
    user_input_database = []
    #user_input_database = [0,("1","42+100", 142.0),("1","42+100+90", 232.0),("2","100-60", 40.0),("3","2*3", 6),("4","6.0 / 2.0", 3.0)]

    @staticmethod
    def print_menu():
        pass     

    @staticmethod
    def get_user_input(input_msg):        
        # On veut faire 
        # 1 -> addition
        # 42+100 
        # 5 pour quitter
        
        # MockView.get_user_input_counter += 1
        # return MockView.user_input_database[MockView.get_user_input_counter - 1]

        value = MockView.user_input_database[MockView.get_user_input_counter]
        MockView.get_user_input_counter += 1
        return value
        
        #if  MockView.run_method_counter == MockView.user_input_database[ MockView.run_method_counter][0]:
        # if MockView.get_user_input_counter == 1:
        #     return MockView.user_input_database[0]
        
        # if MockView.get_user_input_counter == 2:
        #     return MockView.user_input_database[1]
        
        # if  MockView.run_method_counter == 1 :
        #     if MockView.get_user_input_counter == 1:
        #         return "1"
            
        #     if MockView.get_user_input_counter == 2:
        #         return "42+100"
        
        # if  MockView.run_method_counter == 2 :
        #     if MockView.get_user_input_counter == 1:
        #         return "2"
            
        #     if MockView.get_user_input_counter == 2:
        #         return "100-60"

        # if  MockView.run_method_counter == 3 :
        #     if MockView.get_user_input_counter == 1:
        #         return "3"
            
        #     if MockView.get_user_input_counter == 2:
        #         return "2*3"
            
        # if  MockView.run_method_counter == 4 :
        #     if MockView.get_user_input_counter == 1:
        #         return "4"
            
        #     if MockView.get_user_input_counter == 2:
        #         return "6.0 / 2.0"
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
        
def setup_mock(mocker):
    MockView.print_result_call = []
    MockView.get_user_input_counter = 0

    mocker.patch.object(View, 'print_menu', MockView.print_menu)
    mocker.patch.object(View, 'get_user_input', MockView.get_user_input)
    mocker.patch.object(View, 'end_message', MockView.end_message)
    mocker.patch.object(View, 'continue_message', MockView.continue_message)
    mocker.patch.object(View, 'print_result', MockView.print_result)



def test_run_add(mocker):
    sut = Controller()
    MockView.user_input_database = ("1", "100+40", "5")

    setup_mock(mocker)

    sut.run()

    assert len(MockView.print_result_call) == 1
    assert MockView.print_result_call[0] == ("100+40", 140)

def test_run_add_bis(mocker):
    sut = Controller()
    MockView.user_input_database = ("1", "100+40+50","5")

    setup_mock(mocker)

    sut.run()

    assert len(MockView.print_result_call) == 1
    assert MockView.print_result_call[0] == ("100+40+50", 190)

def test_run_add_bis_another(mocker):
    sut = Controller()
    MockView.user_input_database = ("1", "100+40+50", "1", "1+2+3+4+5", "5")

    setup_mock(mocker)

    sut.run()

    assert len(MockView.print_result_call) == 2
    assert MockView.print_result_call[0] == ("100+40+50", 190)
    assert MockView.print_result_call[1] == ("1+2+3+4+5", 15)



# def test_run_sub(mocker):
#     sut = Controller()
#     MockView.run_method_counter = 2
    
#     setup_mock(mocker)

#     sut.run()
    
#     assert len(MockView.print_result_call) == 1
#     assert MockView.print_result_call[0] == ("100-60", 40.0)

# def test_run_multi(mocker):
#     sut = Controller()
#     MockView.run_method_counter = 3
    
#     setup_mock(mocker)

#     sut.run()
    
#     assert len(MockView.print_result_call) == 1
#     assert MockView.print_result_call[0] == ("2*3", 6)

# def test_run_div(mocker):
#     sut = Controller()
#     MockView.run_method_counter = 4
    
#     setup_mock(mocker)

#     sut.run()
    
#     assert len(MockView.print_result_call) == 1
#     assert MockView.print_result_call[0] == ("6.0 / 2.0", 3.0)