from calculate.view import View

def test_print_menu(capsys):
    sut = View()
    sut.print_menu()
    captured = capsys.readouterr() 
    x = captured.out.split("\n")
    assert x[0] == ""
    assert x[1] == "=========== MENU ==========="
    assert x[2] == "1 - Addition"
    assert x[3] == "2 - Soustraction"
    assert x[4] == "3 - Multiplication"
    assert x[5] == "4 - Division"
    assert x[6] == "5 - Quitter"
    assert x[7] == "============================"
    assert x[8] == ""
    assert x[9] == ""

def test_end_message(capsys):
    sut = View()
    sut.end_message()
    captured = capsys.readouterr() 
    assert captured.out == "=========== GOOD-BYE ===========\n"

def test_print_result_not_none(capsys):
    sut = View()
    operation = "5+4"
    result = "9" 
    sut.print_result(operation, result)
    captured = capsys.readouterr() 
    assert captured.out == "RESULTAT : 5+4 = 9\n"

def test_print_result__none(capsys):
    sut = View()
    operation = "5+4"
    result = None
    sut.print_result(operation, result)
    captured = capsys.readouterr() 
    assert captured.out == "Votre operation est incorrect ! : 5+4\n"


