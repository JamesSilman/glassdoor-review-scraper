import requests
import re
from bs4 import BeautifulSoup


class ReviewScrape:

	review = ""
	
	def __init__(self, review):
		self.review = BeautifulSoup(str(review), 'html.parser')	

	if __name__ == '__main__':
		pass

	def scrape_date_and_time(self):
		temp = self.review.find_all("time", {"class", "date subtle small"})
		string_date = temp[0].string
		number_date = re.search(r'\d\d\d\d[-]\d\d[-]\d\d', str(temp)).group()
		return number_date
		#print(number_date)

	def scrape_review_title(self):
		title = self.review.find_all("span", "summary")[0].string.replace("\"", "")
		print(title)

	def scrape_star_rating(self):
		temp = self.review.find_all("i", {"class", "star"})
		print(len(temp))

	def scrape_employee_type(self):
		temp = self.review.find_all("span", {"class", "authorJobTitle middle reviewer"})[0].string
		temp = temp.split("-")[0].strip()
		print(temp)

	def scrape_job_title(self):
		temp = self.review.find_all("span", {"class", "authorJobTitle middle reviewer"})[0].string
		temp = temp.split("-")[1].strip()
		print(temp)

	def scrape_recomends(self):
		temp = self.review.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['middle'])

		temp_array = []
		for val in temp:
			temp_array.append(val.string)

		if "Recommends" in temp_array:
			print("Recommends")
		elif "Doesn't Recommend" in temp_array:
			print("Doesn't Recommend")
		else:
			print("n/a")

	def scrape_outlook(self):
		temp = self.review.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['middle'])

		temp_array = []
		for val in temp:
			temp_array.append(val.string)

		if "Positive Outlook" in temp_array:
			print("Positive Outlook")
		elif "Neutral Outlook" in temp_array:
			print("Neutral Outlook")
		elif "Negative Outlook" in temp_array:
			print("Negative Outlook")
		else:
			print("n/a")

	def scrape_approves_of_ceo(self):
		temp = self.review.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['showDesk'])

		for idx, val in enumerate(temp):
			if "Disapproves of" == val.string:
				temp = (str(val.string) + temp[idx].string.next)
			elif "Approves of" == val.string:
				temp = (str(val.string) + temp[idx].string.next)
			else:
				temp = "n/a"
				
			print(temp)

	def scrape_time_period(self):
		temp = self.review.find_all("p", {"class", " tightBot mainText"})[0].string
		print(temp)

	def scrape_pros_text(self):
		temp = self.review.find_all("p", {"class", " pros mainText truncateThis wrapToggleStr"})[0].string
		print(temp)

	def scrape_cons_text(self):
		temp = self.review.find_all("p", {"class", " cons mainText truncateThis wrapToggleStr"})[0].string
		#print(temp)

	def scrape_advice_text(self):
		temp = self.review.find_all("p", {"class", " adviceMgmt mainText truncateThis wrapToggleStr"})[0].string
		#print(temp)

	def scrape_helpful_count(self):
		temp = self.review.find_all("span", {"class", "count"})
		temp = BeautifulSoup(str(temp), 'html.parser').find("span").get_text()
		count = re.search(r'\d', str(temp)).group()
		print(count)

	def work_life_balance(self):
		temp = self.review.find_all("div", {"class", "subRatings module"})
		temp = BeautifulSoup(str(temp), 'html.parser')	
		temp = temp.find_all("span", {"class", "gdBars gdRatings med "})
		
		print(temp)

