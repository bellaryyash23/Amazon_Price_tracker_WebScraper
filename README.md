# 🛒Amazon Product Price Tracker🏷 using WebScraping BeautifulSoup of Python

🌟A program which automates the process of tracking the price of a product on Amazon to ensure you get the best deal.

🌟The Program makes use of WebScraping with the BeautifulSoup package to scrape the product website daily and compare the acquired price with the threshold price set in the program.
If the price is less than the cutoff price then a mail alert is sent to the user using the SMTP module with the details of price of product and its url.

👉In the 'main.py' file, first the product details are acquired using the requests module and stored as respones.

👉Then the BeautifulSoup Object is used to parse throught the website data and find the relevant price of the product. This is done using the '.find()' method of the
BeautifulSoup class.

![Product Website](https://github.com/bellaryyash23/Amazon_Price_tracker_WebScraper/blob/master/product.jpg?raw=true)

👆Product Website👆

👉Once the price is acquired it is compared with the cutoff price set in the program. If the price is less than the Threshold price then the SMPT mail method gets
called.

👉The SMTP mail method is used to send an email alert to the user on his mail Id with the details of product like Product name, Price Drop and Product URL attached 
to the mail. Using this information the user can avail this price drop offer.

![Mail Alert](https://github.com/bellaryyash23/Amazon_Price_tracker_WebScraper/blob/master/mail.jpg?raw=true)

👆Mail alert of Price drop👆

🌟In this way, using WebScraping the process of Price tracking is automated.
