import streamlit as st
import yoomoney
from yoomoney import Client
from yoomoney import Quickpay
import time
token = st.secrets["ytoken"]
client = Client(token)
user = client.account_info()
st.set_page_config(page_title="пополнение баланса стим")

def main():
    st.title("Пополнение счета Steam")
    login =  st.text_input("логин стим")
    if login:
        cor = st.error("Убедитесь что верно указали логин!")
        time.sleep(3)
        del cor
        
    summ = st.number_input(step=1,min_value=50,max_value=1000,label="Введите сумму, которую вы хотите пополнить")
    if summ:
        comis = summ + summ / 100 * 3
        com = st.text(f"Комиссия : {int(comis - summ)}")

    if st.button("Пополнить счет"):
        quickpay = Quickpay(
            receiver="4100116565978076",
            quickpay_form="shop",
            targets="Sponsor this project",
            paymentType="SB",
            sum=comis + 1,
            label=f"{login}"
            )
        print(quickpay.base_url)
        print(quickpay.redirected_url)
        st.warning(f"[Для оплаты нажмите на этот текст]({quickpay.redirected_url})")
        while True:
            history = client.operation_history(label=f"{login}")
            for operation in history.operations:
                if operation.status == "success":
                    print(1)
                    st.warning("ожидайте поступления средств")
                    break
if __name__ == "__main__":
    main()