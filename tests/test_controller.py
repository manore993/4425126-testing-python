from calculate.controller import Controller
from calculate.view import View
from calculate.operators import Operators

class MockOperators:
    user_output_database = []  
    addition_counter = 0
    add_output_database = []
    substraction_counter = 0
    sub_output_database = []
    multiplication_counter = 0
    multi_output_database = []
    division_counter = 0
    div_output_database = []

    @staticmethod
    def addition(self, operation):
        
        value = MockOperators.add_output_database[MockOperators.addition_counter]
        MockOperators.addition_counter += 1 
        return value
    
    @staticmethod
    def substraction(self, operation):

        value = MockOperators.sub_output_database[MockOperators.substraction_counter]
        MockOperators.substraction_counter += 1
        return value
    
    @staticmethod
    def multiplication(self, operation):

        value = MockOperators.multi_output_database[MockOperators.multiplication_counter]
        MockOperators.multiplication_counter += 1
        return value
    
    @staticmethod
    def division(self, operation):
        print(MockOperators.division_counter)
        value = MockOperators.div_output_database[MockOperators.division_counter]
        MockOperators.division_counter += 1
        print(value)
        return value

class MockView:
    get_user_input_counter = 0
    print_result_call = []
    user_input_database = []

    @staticmethod
    def print_menu():
        pass     

    @staticmethod
    def get_user_input(input_msg):        

        value = MockView.user_input_database[MockView.get_user_input_counter]
        MockView.get_user_input_counter += 1
        return value
        
       
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
    MockOperators.addition_counter = 0
    MockOperators.substraction_counter = 0
    MockOperators.multiplication_counter = 0
    MockOperators.division_counter = 0

    mocker.patch.object(View, 'print_menu', MockView.print_menu)
    mocker.patch.object(View, 'get_user_input', MockView.get_user_input)
    mocker.patch.object(View, 'end_message', MockView.end_message)
    mocker.patch.object(View, 'continue_message', MockView.continue_message)
    mocker.patch.object(View, 'print_result', MockView.print_result)
    mocker.patch.object(Operators, 'addition', MockOperators.addition)
    mocker.patch.object(Operators, 'substraction', MockOperators.substraction)
    mocker.patch.object(Operators, 'multiplication', MockOperators.multiplication)
    mocker.patch.object(Operators, 'division', MockOperators.division)


def test_run_add(mocker):
    sut = Controller()
    MockView.user_input_database = ("1", "100+40", "5")
    MockOperators.add_output_database = [140]

    setup_mock(mocker)

    sut.run()

    assert len(MockView.print_result_call) == 1
    assert MockView.print_result_call[0] == ("100+40", 140)

def test_run_add_bis(mocker):
    sut = Controller()
    MockView.user_input_database = ("1", "100+40+50","5")
    MockOperators.add_output_database = [190]
    
    setup_mock(mocker)

    sut.run()

    assert len(MockView.print_result_call) == 1
    assert MockView.print_result_call[0] == ("100+40+50", 190)

def test_run_add_bis_another(mocker):
    sut = Controller()
    MockView.user_input_database = ("1", "100+40+50", "1", "1+2+3+4+5", "5")
    MockOperators.add_output_database = [190, 15]
    
    setup_mock(mocker)

    sut.run()

    assert len(MockView.print_result_call) == 2
    assert MockView.print_result_call[0] == ("100+40+50", 190)
    assert MockView.print_result_call[1] == ("1+2+3+4+5", 15)

def test_run_sub(mocker):
    sut = Controller()
    MockView.user_input_database = ("2", "100-60", "5")
    MockOperators.sub_output_database = [40]

    setup_mock(mocker)

    sut.run()
    
    assert len(MockView.print_result_call) == 1
    assert MockView.print_result_call[0] == ("100-60", 40.0)

def test_run_multi(mocker):
    sut = Controller()
    MockView.user_input_database = ("3", "2*3","3", "4*6", "5")
    MockOperators.multi_output_database  = [6, 24]
    
    setup_mock(mocker)

    sut.run()
    
    assert len(MockView.print_result_call) == 2
    assert MockView.print_result_call[0] == ("2*3", 6) 
    assert MockView.print_result_call[1] == ("4*6", 24)

def test_run_div(mocker):
    sut = Controller()
    MockView.user_input_database = ("4", "6.0 / 2.0", "4", "6.0 / 0.0", "5")
    MockOperators.div_output_database  = [3.0, None]
    
    setup_mock(mocker)

    sut.run()
    
    assert len(MockView.print_result_call) == 2
    assert MockView.print_result_call[0] == ("6.0 / 2.0", 3.0)
    assert MockView.print_result_call[1] == ("6.0 / 0.0", None)

def test_run_allfunctions(mocker):
    sut = Controller()
    MockView.user_input_database = ("3", "2*3","3", "4*6","4", "6.0 / 2.0", "4", "6.0 / 0.0", "5")
    MockOperators.multi_output_database = [6, 24]
    MockOperators.div_output_database = [3.0, None]
    
    setup_mock(mocker)

    sut.run()
    
    assert len(MockView.print_result_call) == 4
    assert MockView.print_result_call[0] == ("2*3", 6) 
    assert MockView.print_result_call[1] == ("4*6", 24)
    assert MockView.print_result_call[2] == ("6.0 / 2.0", 3.0)
    assert MockView.print_result_call[3] == ("6.0 / 0.0", None)
