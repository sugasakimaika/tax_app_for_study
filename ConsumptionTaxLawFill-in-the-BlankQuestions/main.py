from scraper import Scraper
from quiz_game import QuizGame

def main():
    url = 'ここにスクレイピングしたいウェブページのURLを入れます'
    scraper = Scraper(url)
    questions_answers = scraper.scrape()

    game = QuizGame(questions_answers)
    game.play()

if __name__ == "__main__":
    main()
