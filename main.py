import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
# main.pyはルートディレクトリに置くのが一般的。src配下のファイルをimportできるが、これをmain.pyに使っていいのか

from scraper import Scraper
from tax_game import QuizGame

def main():
    url = 'https://elaws.e-gov.go.jp/document?lawid=340AC0000000034'
    scraper = Scraper(url)
    questions_answers = scraper.scrape()

    game = QuizGame(questions_answers)
    game.play()

if __name__ == "__main__":
    main()
