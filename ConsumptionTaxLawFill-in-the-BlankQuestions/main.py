from scraper import Scraper
from quiz_game import QuizGame

def main():
    url = 'https://elaws.e-gov.go.jp/document?lawid=340AC0000000034'
    scraper = Scraper(url)
    questions_answers = scraper.scrape()

    game = QuizGame(questions_answers)
    game.play()

if __name__ == "__main__":
    main()
