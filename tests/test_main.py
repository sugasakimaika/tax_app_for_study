import unittest
from unittest.mock import patch
from main import main

class TestMain(unittest.TestCase):
    @patch('main.Scraper')
    @patch('main.tax_game')
    def test_main(self, mock_tax_game, mock_scraper):
        # Mock the return values of the Scraper and QuizGame classes
        mock_scraper_instance = mock_scraper.return_value
        mock_scraper_instance.scrape.return_value = {'question': 'What is the answer?'}
        mock_tax_game_instance = mock_tax_game.return_value

        # Call the main function
        main()

        # Assert that the Scraper and QuizGame classes were called with the correct arguments
        mock_scraper.assert_called_once_with('https://elaws.e-gov.go.jp/document?lawid=340AC0000000034')
        mock_tax_game.assert_called_once_with({'question': 'What is the answer?'})

        # Assert that the play method of the QuizGame instance was called
        mock_tax_game_instance.play.assert_called_once()

if __name__ == '__main__':
    unittest.main()
