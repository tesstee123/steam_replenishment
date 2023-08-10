import streamlit as st
import webbrowser
st.set_page_config(page_title="пополнение баланса стим")

def main():
    st.title("Пополнение счета Steam")
    if st.text_input("логин стим"):
        st.error("Убедитесь что верно указали логин!")
    
    sum = st.number_input(step=1,min_value=100,max_value=1000,label="Введите сумму, которую вы хотите пополнить")
    if sum:
        com = st.text(f"Комиссия : {sum}")


    if st.button("Пополнить счет"):
        # здесь вы можете добавить код для пополнения счета Steam
        #st.success(f"Счет {steam_username} успешно пополнен на {amount} рублей!")
        webbrowser.open_new_tab(st.secrets["url"])
        # st.markdown(f'<meta http-equiv="refresh" content="0;URL={st.secrets["url"]}" />', unsafe_allow_html=True)
        # print(1)

if __name__ == "__main__":
    main()