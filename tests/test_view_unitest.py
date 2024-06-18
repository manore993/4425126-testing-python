import unittest
from calculate.view import View

class TestUtils(unittest.TestCase):
    def test_print_menu(self,capsys):
        sut = View()
        sut.print_menu()
        captured = capsys.readouterr() 
        x = captured.out.split("\n")
        self.assertEqual(x[0],"")
        self.assertEqual(x[1],"=========== MENU ===========")
        self.assertEqual(x[2],"1 - Addition")
        self.assertEqual(x[3],"2 - Soustraction")
        self.assertEqual(x[4],"3 - Multiplication")
        self.assertEqual(x[5],"4 - Division")
        self.assertEqual(x[6],"5 - Quitter")
        self.assertEqual(x[7],"============================")
        self.assertEqual(x[8],"")
        self.assertEqual(x[9],"")

    def test_end_message(self,capsys):
        sut = View()
        sut.end_message()
        captured = capsys.readouterr() 
        self.assertEqual(captured.out,"=========== GOOD-BYE ===========\n")

    def test_print_result_not_none(self,capsys):
        sut = View()
        operation = "5+4"
        result = "9" 
        sut.print_result(operation, result)
        captured = capsys.readouterr() 
        self.assertEqual(captured.out,"RESULTAT : 5+4 = 9\n")

    def test_print_result__none(self,capsys):
        sut = View()
        operation = "5+4"
        result = None
        sut.print_result(operation, result)
        captured = capsys.readouterr() 
        self.assertEqual(captured.out,"Votre operation est incorrect ! : 5+4\n")

if __name__ == '__main__':
    unittest.main()