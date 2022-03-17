import streamlit as st
from time import sleep


class Carregamento:
    @staticmethod
    def carregar() -> None:
        """
        :return: Mostra um widget de carregamento para o usuário.
        """

        with st.spinner('Jogando dados...'):
            sleep(0.5)
