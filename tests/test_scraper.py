import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from unittest.mock import patch
from src.ConsumptionTaxLawFill_in_the_BlankQuestions.scraper import Scraper

class TestScraper(unittest.TestCase):
    @patch('scraper.requests.get')
    @patch('scraper.BeautifulSoup')
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

        # Assert that the find_all method was called with the correct arguments
        mock_soup.find_all.assert_called_once_with(...)

        # Assert that the result is the expected dictionary
        expected_result = {'Question 1': 'Answer 1', 'Question 2': 'Answer 2'}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
