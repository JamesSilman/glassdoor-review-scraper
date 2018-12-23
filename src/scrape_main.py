import re
import requests
import error_log as log
import review_scrape as rs

from bs4 import BeautifulSoup


headers = {
    'authority': 'www.glassdoor.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'dnt': '1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

url = 'https://www.glassdoor.com/Reviews/Nuix-Reviews-E257627.htm'

response = requests.get(url, headers=headers)

c = response.content
soup = BeautifulSoup(c, 'html.parser')

samples = soup.find_all("div", "hreview")


def number_of_pages():
	number_of_pages = soup.find_all("li", "page last")
	number_of_pages = (str(number_of_pages).split("</a></li>")[0])
	return (str(number_of_pages)[-1:])

num_of_pages = (int(number_of_pages()))

temp = []

for i in range(0, num_of_pages):
	temp.append(url[0:-4] + "_P" + (str(i+1)) + ".htm")

for t in temp:
	samples = soup.find_all("div", "hreview")
	
	for x in samples:
		scrape = rs.ReviewScrape(x)
		scrape.scrape_date_and_time()
		scrape.scrape_review_title()
		scrape.scrape_star_rating()
		scrape.scrape_employee_type()
		scrape.scrape_job_title()
		scrape.scrape_recomends()
		scrape.scrape_outlook()
		scrape.scrape_approves_of_ceo()
		scrape.scrape_time_period()
		scrape.scrape_pros_text()
		scrape.scrape_cons_text()
		scrape.scrape_advice_text()
		scrape.scrape_helpful_count()



		
