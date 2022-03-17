import streamlit as st


def criar_radio_button() -> str:
    """
    :return: Retorna a quantidade de dados escolhida pelo usuário.
    """

    dados_num = st.radio(
        label='Quantidade de dados.',
        options=['1 Dado', '2 Dados'],
        index=0,
        help='Escolha quantos dados serão jogados.'
    )

    return dados_num
