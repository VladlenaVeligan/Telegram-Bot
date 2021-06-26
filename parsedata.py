from bs4 import BeautifulSoup
import random
import re
import requests
from telebot.types import Video



def parse(your_URL):
	HEADERS = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
	}

	s = requests.Session()

	response = s.get(your_URL, headers = HEADERS) 
	soup = BeautifulSoup(response.content, 'html.parser')
	values = soup.find_all('div', style = 'overflow:auto;')
	
	
	filmName = []
	filmRating = []
	filmDescription = []


	for value in values:
		film_tag = value.find('a', 'titlefilm')
		filmName.append(film_tag.get_text())
		rating_tag = value.find('span','rating-big')
		filmRating.append(rating_tag.get_text())

	index = random.randint(0, 99)
	film = filmName[index]
	rating = filmRating[index]


	href_tag = soup.find('a', text=re.compile(film)).get('href')


	response_des = s.get('https://www.kinonews.ru' + href_tag, headers = HEADERS)
	soup_des = BeautifulSoup(response_des.content, 'html.parser')
	description_tag = soup_des.find('div', attrs={'itemprop':'description'})
	filmDescription = description_tag.get_text()

	href_videos = soup_des.find_all('div', attrs={'class' : 'dopblock mright'})
	global href_video
	for value in href_videos:
		href_video = value.find('a').get('href')
	
	response_video = s.get('https://www.kinonews.ru' + href_video, headers = HEADERS)
	soup_video = BeautifulSoup(response_video.content, 'html.parser')



	video_tag = soup_video.find('meta', attrs={'itemprop' : 'contentUrl'})
	video = video_tag['content']
	if 'mp4' not in video:
		video = ''
		
	res = ['📌 «‎' + film + '»', '📌 Рейтинг: ' + rating, '📌 Описание: ' + filmDescription, video]

	return '\n'.join(res)


def parseanime(your_URL):
	HEADERS = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
	}

	s = requests.Session()

	response = s.get(your_URL, headers = HEADERS) 
	soup = BeautifulSoup(response.content, 'html.parser')
	values = soup.find_all('div', style = 'overflow:auto;')
	
	
	filmName = []
	filmRating = []
	filmDescription = []


	for value in values:
		film_tag = value.find('a', 'titlefilm')
		filmName.append(film_tag.get_text())
		rating_tag = value.find('span','rating-big')
		filmRating.append(rating_tag.get_text())

	index = random.randint(0, 99)
	film = filmName[index]
	rating = filmRating[index]


	href_tag = soup.find('a', text=re.compile(film)).get('href')


	response_des = s.get('https://www.kinonews.ru' + href_tag, headers = HEADERS)
	soup_des = BeautifulSoup(response_des.content, 'html.parser')
	description_tag = soup_des.find('div', attrs={'itemprop':'description'})
	filmDescription = description_tag.get_text()

	res = ['📌 «‎' + film + '»', '📌 Рейтинг: ' + rating, '📌 Описание: ' + filmDescription]

	return '\n'.join(res)
