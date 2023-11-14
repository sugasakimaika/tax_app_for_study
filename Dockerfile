FROM python:3.7.5-slim

WORKDIR /work

# コードと必要なファイルをコピー
COPY Womanmoneycareer Womanmoneycareer
COPY tests tests
COPY setup.py setup.py
COPY MANIFEST.in MANIFEST.in
COPY requirements.txt requirements.txt  # 追加

# pipをアップグレードし、依存関係をインストール
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install pytest

# 実行コマンド、例えばgunicornなど
CMD ["gunicorn", "Womanmoneycareer:app", "--config", "gunicorn_config.py"]
