from bs4 import BeautifulSoup
import os
import requests
import lxml
import smtplib

USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')

PRODUCT_URL = "https://www.amazon.in/Seagate-Expansion-1TB-External-HDD/dp/B08ZJDWTJ1?ref_=Oct_d_obs_d_1375395031" \
              "&pd_rd_w=jZKOy&pf_rd_p=6a6b213b-2f3b-4413-8099-742b8c9f52a9&pf_rd_r=ZW8FMNJ9QWNNN7YSV8NC&pd_rd_r" \
              "=41b3a598-478a-4dac-9473-29b4447732e8&pd_rd_wg=sINnX&pd_rd_i=B08ZJDWTJ1&th=1 "
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 "
                  "Safari/537.36 ",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=PRODUCT_URL, headers=headers)
amaz_web = response.text

soup = BeautifulSoup(amaz_web, parser=lxml, features="lxml")
scrape_price = soup.find(name="span", class_="a-offscreen").get_text().split("₹")[1].split(",")
prd_title = soup.title.get_text()
price = float(scrape_price[0] + scrape_price[1])

if price < 4000:
    connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=USERNAME, password=PASSWORD)
    connection.sendmail(from_addr=USERNAME,
                        to_addrs=os.environ.get('SEND'),
                        msg=f"Subject:Amazon Price Alert \n\n {prd_title} on available at Rs.{price} only.\n"
                            f"Hurry Buy now: {PRODUCT_URL}")
    print("Mail Sent.")
    