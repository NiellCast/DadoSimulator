import streamlit as st
from widgets.metrics.create_metrics import criar_metrica
from widgets.header.create_header import criar_header
from widgets.loading.loading import Carregamento


def criar_botao(radio_button: str, dado: object) -> None:
    """
    :param radio_button: recebe o valor escolhido pelo usuário equivalente à quantidade de dados.
    :param dado: Recebe um objeto "dado".
    :return: Retorna ao usuário os números sorteados.
    """

    def clicar() -> None:
        """
        :return: Invoca o método de sortear números da classe "Dado".
        """

        criar_header('Resultados')
        Carregamento.carregar()

        col1, col2, col3 = st.columns(3)

        if radio_button == '1 Dado':
            dado.numero1 = True

            with col1:
                criar_metrica('1', dado.numero1)

        else:
            dado.numero1 = True
            dado.numero2 = True

            with col1:
                criar_metrica('1', dado.numero1)

            with col2:
                criar_metrica('2', dado.numero2)

    botao = st.button(
        label='Jogar',
        on_click=clicar
    )

