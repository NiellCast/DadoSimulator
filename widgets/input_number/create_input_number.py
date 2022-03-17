import streamlit as st


def mostrar_input_number() -> str:
    """
    :return: retorna o número inserido pelo usuário.
    """

    escolhido = st.number_input(
        label='Quantidade de jogadas.',
        min_value=1,
        max_value=5,
        value=1,
        step=1,
        help='Escolha quantas vezes o dado será jogado.',
        key='jogadas'
    )

    return escolhido
