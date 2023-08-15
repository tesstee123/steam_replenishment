import streamlit as st
import yoomoney
import requests
from yoomoney import Client
from yoomoney import Quickpay
import time
try:
    token = st.secrets["ytoken"]
    api_access_token = st.secrets["qtoken"]
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
            
        summ = st.number_input(step=1,min_value=35,max_value=1000,label="Введите сумму, которую вы хотите пополнить")
        if summ:
            comis = summ + summ / 100 * 15
            com = st.text(f"Комиссия : {int(comis - summ)} - 15 %")
            summ_in_tenge = (summ * 3,8)

        if st.button("Пополнить счет"):
            t = time.time()
            quickpay = Quickpay(
                receiver="4100116565978076",
                quickpay_form="shop",
                targets="Sponsor this project",
                paymentType="SB",
                sum=comis + 1,
                label=f"{login}{t}"
                )
            print(quickpay.base_url)
            print(quickpay.redirected_url)
            
            st.warning(f"[Для оплаты нажмите на этот текст]({quickpay.redirected_url})")
            while True:
                history = client.operation_history(label=f"{login}{t}")
                for operation in history.operations:
                    if operation.status == "success":
                        print(1)
                        s = requests.Session()
                        s.headers['Accept'] = 'application/json'
                        s.headers['Content-Type'] = 'application/json'
                        s.headers['authorization'] = 'Bearer 36b2e468eb77427af2e2c5a9a6e38738'

                        data = {
                            "id":f'{str(int(time.time() * 1000))}',
                            "sum": {"amount":f"{summ_in_tenge}",
                            "currency":"398"},
                            "paymentMethod": {"type":"Account",
                            "accountId":"643"},
                            "fields": {"account":f"{login}"}
                            }
                        res = s.post('https://edge.qiwi.com/sinap/api/v2/terms/31212/payments', json = data)

                        st.warning("ожидайте поступления средств")
                        time.sleep(60)
                        break
    if __name__ == "__main__":
        main()
except:
    pass