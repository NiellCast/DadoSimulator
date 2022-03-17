import streamlit as st


def criar_metrica(nome: str, valor: int) -> None:
    """
    :param nome: Recebe o nome da métrica a ser criada.
    :param valor: Recebe o valor da métrica a ser criada.
    :return: Cria um widget métrica na tela do usuário.
    """

    result = st.metric(
        label=f'Dado {nome}',
        value=valor
    )
