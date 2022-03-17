import streamlit as st
from config.configuracao import configurar
from widgets.header.create_header import criar_header
from widgets.radio_button.create_radio_button import criar_radio_button
from widgets.button.create_button import criar_botao
from sorteio.sortear_numeros import Dado


def run() -> None:
    """
    :return: Inicia a aplicação.
    """

    resultado = Dado()

    configurar()

    criar_header('Simulador de dados')

    col1, col2, col3 = st.columns(3)

    with col1:
        botao_radio = criar_radio_button()

    with col2:
        criar_botao(botao_radio, resultado)


if __name__ == '__main__':
    run()
