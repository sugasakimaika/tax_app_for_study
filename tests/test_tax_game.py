import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from unittest.mock import patch
from src.ConsumptionTaxLawFill_in_the_BlankQuestions.tax_game import QuizGame

class TestQuizGame(unittest.TestCase):
    def test_play_correct_answer(self):
        questions_answers = {'What is the capital of Japan?': 'Tokyo'}
        game = QuizGame(questions_answers)

        with patch('builtins.input', return_value='Tokyo'):
            with patch('time.time', return_value=0):
                with patch('builtins.print') as mock_print:
                    game.play()

        mock_print.assert_called_with('\nゲーム終了！1問中、1問正解でした。')

    def test_play_incorrect_answer(self):
        questions_answers = {'What is the capital of Japan?': 'Tokyo'}
        game = QuizGame(questions_answers)

        with patch('builtins.input', return_value='Osaka'):
            with patch('time.time', return_value=0):
                with patch('builtins.print') as mock_print:
                    game.play()

        mock_print.assert_called_with('\nゲーム終了！1問中、0問正解でした。')

if __name__ == '__main__':
    unittest.main()
