import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from io import StringIO
from unittest.mock import patch
from tax_game import play_game

class TestTaxGame(unittest.TestCase):
    def test_play_game_correct_answer(self):
        questions_answers = {
            "What is the capital of Japan?": ("Tokyo", "Article 1"),
            "What is the currency of France?": ("Euro", "Article 2"),
            "Who is the current president of the United States?": ("Joe Biden", "Article 3")
        }
        user_input = ["Tokyo", "Euro", "Joe Biden"]
        expected_output = [
            "\n問題： What is the capital of Japan?\n関連する条文： Article 1\n答えを入力してください: 正解！所要時間: 0.00秒",
            "\n問題： What is the currency of France?\n関連する条文： Article 2\n答えを入力してください: 正解！所要時間: 0.00秒",
            "\n問題： Who is the current president of the United States?\n関連する条文： Article 3\n答えを入力してください: 正解！所要時間: 0.00秒",
            "\nゲーム終了！3問中、3問正解でした。"
        ]

        with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new=StringIO()) as fake_output:
            play_game(questions_answers)
            output = fake_output.getvalue().strip().split("\n")

        self.assertEqual(output, expected_output)

    def test_play_game_incorrect_answer(self):
        questions_answers = {
            "What is the capital of Japan?": ("Tokyo", "Article 1"),
            "What is the currency of France?": ("Euro", "Article 2"),
            "Who is the current president of the United States?": ("Joe Biden", "Article 3")
        }
        user_input = ["Tokyo", "Dollar", "Donald Trump"]
        expected_output = [
            "\n問題： What is the capital of Japan?\n関連する条文： Article 1\n答えを入力してください: 正解！所要時間: 0.00秒",
            "\n問題： What is the currency of France?\n関連する条文： Article 2\n答えを入力してください: 不正解。正しい答えは「Euro」で、関連する条文は「Article 2」です。",
            "\n問題： Who is the current president of the United States?\n関連する条文： Article 3\n答えを入力してください: 不正解。正しい答えは「Joe Biden」で、関連する条文は「Article 3」です。",
            "\nゲーム終了！3問中、1問正解でした。"
        ]

        with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new=StringIO()) as fake_output:
            play_game(questions_answers)
            output = fake_output.getvalue().strip().split("\n")

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
