import streamlit as st


def criar_header(txt: str) -> None:
    """
    :param txt: Recebe uma string para ser adicionada em um header.
    :return: Cria um header na página da aplicação.
    """

    st.header(txt)
