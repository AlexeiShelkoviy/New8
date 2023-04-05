from bs4 import BeautifulSoup
import requests

# !!! Этот код выводит текущий курс доллара, а также позволяет конвертировать гривны в доллары !!!

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
if response.status_code == 200:
   soup = BeautifulSoup(response.text, features="html.parser")
   soup_list = soup.find_all("td", string="36,5686")
   # for elem in soup_list:
   #     print(elem)
   print(soup_list[0].text)


url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange'
params = {'valcode': 'USD', 'date': '20230405'}
response = requests.get(url, params=params)
xml_response = response.content.decode('utf-8')
start = xml_response.find('<rate>') + 6
end = xml_response.find('</rate>')
rate = float(xml_response[start:end])
uah = float(input('Введите сумму в гривнах: '))
usd = round(uah / rate, 2)
print(f'{uah} грн = {usd} $.')