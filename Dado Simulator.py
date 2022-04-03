import os


def run():
    os.system('pip install -r requirements.txt')
    os.system('streamlit run main.py')


if __name__ == '__main__':
    run()
