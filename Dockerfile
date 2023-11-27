# Pythonの軽量化されたスリムバージョンをベースイメージとして使用
FROM python:3.8-slim

# 作業ディレクトリの設定
WORKDIR /work

# アプリケーションのコードと必要なファイルをコピー
COPY tests tests
COPY setup.py setup.py
COPY requirements.txt requirements.txt
COPY gunicorn_config.py gunicorn_config.py

# pipをアップグレードし、必要な依存関係をインストール
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install pytest

# アプリケーションの実行コマンドを設定
CMD ["gunicorn", "Womanmoneycareer:app", "--config", "gunicorn_config.py"]
