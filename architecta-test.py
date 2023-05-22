import unittest
from main import *

mock_response_mvc = str('O padrão Model-View-Controller (MVC) é um padrão de design que separa a lógica da aplicação em três componentes interconectados: o modelo, a visão e o controlador.')

class TestArchitecta(unittest.TestCase):
    def test_answer_greatings(self):
        question = "Oi, tudo bem?"
        is_answer_valid = answer_question(question)
        self.assertTrue(is_answer_valid)

    def test_search_with_wikpedia(self):
        question = "o que é MVC?"
        answer_question = search_content(question)
        self.assertTrue(answer_question)
   
    def test_answer_programming(self):
      question = "o que é o padrão mvc?"
      answer = answer_question(question)
      self.assertEqual(str(answer), str(mock_response_mvc))

    def test_answer_leaving(self):
      question = "até mais"
      answer = answer_question(question)
      expected_value = "tchau tchau"
      self.assertEqual(str(answer), str(expected_value))

if __name__ == '__main__':
    unittest.main()
