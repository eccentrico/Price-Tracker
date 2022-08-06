import requests
import smtplib
from bs4 import BeautifulSoup
URL='https://www.amazon.in/Ankaret-Stainless-Steel-Bottle-Sipper/dp/B08LQJYDWV/?_encoding=UTF8&pd_rd_w=vYppA&pf_rd_p=6486d470-f2a3-47ef-9df5-cd76607dc002&pf_rd_r=S3GNCZT0D4KXN6E4SWMG&pd_rd_r=5ea456b4-44a6-465d-80fe-6f4946ef9f6d&pd_rd_wg=HD0f9&ref_=pd_gw_ci_mcx_mi'
email="youaremyfire46@gmail.com"
password="johnwick4567"
response=requests.get('https://www.amazon.in/Ankaret-Stainless-Steel-Bottle-Sipper/dp/B08LQJYDWV/?_encoding=UTF8&pd_rd_w=vYppA&pf_rd_p=6486d470-f2a3-47ef-9df5-cd76607dc002&pf_rd_r=S3GNCZT0D4KXN6E4SWMG&pd_rd_r=5ea456b4-44a6-465d-80fe-6f4946ef9f6d&pd_rd_wg=HD0f9&ref_=pd_gw_ci_mcx_mi',headers={"Accept-Language":"en-US,en;q=0.9,hi;q=0.8","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"})
soup=BeautifulSoup(response.text,"lxml")
price=soup.find(name="span",class_="a-offscreen").getText()
price_without_currency=float(price.split("₹")[1])
if price_without_currency>320:
    connection=smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(to_addrs="zagrim7011@gmail.com",from_addr=email,msg=f"Subject: Price Drop\n\n THe price has dropped down to {price_without_currency} Hurry Up !!!!!!!!!!!!!{URL}")