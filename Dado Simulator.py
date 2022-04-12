from os import system


def run() -> None:
    """
    :return: Instala os requisitos e inicia a aplicação.
    """
    system('pip install -r requirements.txt')
    system('streamlit run main.py')


if __name__ == '__main__':
    run()
