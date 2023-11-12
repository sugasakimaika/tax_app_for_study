from setuptools import setup, find_packages

setup(
    name="my_app_for_Womanmoneycareer",
    version='1.2',
    description='Pythonのディレクトリ構成のテスト用',
    author='Maika Sugasaki',
    author_email='sakimaikawahaha@gmail.com',
    url='https://github.com/sugasakimaika/my_app_for_Womanmoneycareer',
packages=find_packages(),
    entry_points="""
      [console_scripts]
      Womanmoneycareer = Womanmoneycareer.cli:execute
    """,
)