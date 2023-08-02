import requests
from bs4 import BeautifulSoup
from mail_sender import *

URL = "https://www.amazon.in/Samsung-Internal-Solid-State-MZ-V7S500BW/dp/B07MFBLN7K"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0"}


def getPageHTML(URL):
    page = requests.get(url=URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def getProductTitle(soup):
    title = soup.find(id="productTitle").get_text()
    title = title.strip()
    return title


def getProductCurrentPrice(soup):
    product_price = soup.find(class_="a-price-whole").get_text()
    product_price = product_price.strip()

    current_price = float(product_price.replace(".", "").replace(",", ""))
    return current_price


if __name__ == "__main__":
    soup = getPageHTML(URL)

    title = getProductTitle(soup)
    current_price = getProductCurrentPrice(soup)

    target_price = 2800.0

    if (current_price <= target_price):
        # Send the email
        send_secure_email(sender_email, sender_password,
                          receiver_email, subject, body)
