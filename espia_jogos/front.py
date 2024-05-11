import streamlit as st
from espia_jogos.usuarios import usuarios
from espia_jogos.ludopedia import Ludopedia


def display_collection(usuario, colecao):
    if colecao:
        name_to_display = usuario.nome_legivel if usuario.nome_legivel else usuario.usuario
        thumbnail_url = usuario.thumb
        # Start an HTML table
        html_content = "<style>td, th {{text-align: left; padding: 8px;}}</style>"
        html_content += "<table border='1'>"
        html_content += "<tr><th>Jogo</th><th>Nota</th></tr>"
        
        for jogo in colecao:
            nota = jogo["vl_nota"] if jogo["vl_nota"] is not None else '-'
            game_name = jogo['nm_jogo']
            # Add a row for each game with an image and text in the same cell
            html_content += f"<tr><td><img src='{jogo["thumb"]}' style='height:50px;'> {game_name}</td><td>{nota}</td></tr>"
        
        html_content += "</table>"
        col1, col2 = st.columns(2)
        with col1:
            st.image(thumbnail_url, caption=name_to_display)
        with col2:
            st.markdown(html_content, unsafe_allow_html=True)

def app():
    st.title('Espia Jogos dos Amigos')

    with st.form("Jogos"):
        nome_jogo = st.text_input("Digite o nome do jogo para buscar:")
        submit_button = st.form_submit_button("Buscar jogos")
        
        if submit_button and nome_jogo:
            for usuario in usuarios:
                colecao = Ludopedia.request_collection(usuario.id_usuario, nome_jogo)
                if colecao:
                    display_collection(usuario, colecao)

if __name__ == '__main__':
    app()
