import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from unittest.mock import patch, call
from src.ConsumptionTaxLawFill_in_the_BlankQuestions.scraper import Scraper

class TestScraper(unittest.TestCase):
    @patch('src.ConsumptionTaxLawFill_in_the_BlankQuestions.scraper.requests.get')
    @patch('src.ConsumptionTaxLawFill_in_the_BlankQuestions.scraper.BeautifulSoup')
    def test_scrape(self, mock_bs, mock_requests):
        # Mock the response and soup objects
        mock_response = mock_requests.return_value
        mock_soup = mock_bs.return_value

        # Mock the find_all method to return sample data
        mock_soup.find_all.return_value = ['Question 1', 'Question 2']

        # Create an instance of the Scraper class
        scraper = Scraper('https://example.com')

        # Call the scrape method
        result = scraper.scrape()

        # Assert that the requests.get method was called with the correct URL
        mock_requests.assert_called_once_with('https://example.com')

        # Assert that the BeautifulSoup constructor was called with the correct arguments
        mock_bs.assert_called_once_with(mock_response.content, 'html.parser')

        # 質問と答えで二回分呼ぶことを確認
        mock_soup.find_all.assert_has_calls([call('p'), call('div')])

        # ここでassertできていないが、ここまでの実装は完了
        expected_result = {'Question 1': 'Answer 1', 'Question 2': 'Answer 2'}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
