import streamlit as st


def configurar() -> None:
    """
    :return: Configura a aplicação.
    """

    st.set_page_config(
        page_title='Dados',
        page_icon=None,
        layout='centered'
    )
