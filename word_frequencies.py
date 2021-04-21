"""Count amount of words on a webpage"""

from bs4 import BeautifulSoup
import requests


def get_all_texts(url):
	"""Gets all texts on a webpage"""
	res = requests.get(url)
	html_page = res.content
	soup = BeautifulSoup(html_page, 'html.parser')
	texts = soup.find_all(text=True)
	blacklists = ['\n']
	reasonable_data = []
	for _ in texts:
		if _ not in blacklists:
			reasonable_data.append(_)
	return reasonable_data


def count_word_in_each_sentence(sentence):
	"""Counts the amount each word appears in a sentence"""
	sentence = sentence.lower()
	words = sentence.split()
	count_dict = dict()
	for _ in words:
		if count_dict.get(_):
			count_dict[_] += 1
		else:
			count_dict[_] = 1
	return count_dict


def count_words_in_sentence_list(sentence_list):
	"""Counts the amount each word appears in a list of sentences"""
	total_dict = dict()
	for _ in sentence_list:
		count = count_word_in_each_sentence(_)
		for key, value in count.items():
			if total_dict.get(key):
				total_dict[key] += value
			else:
				total_dict[key] = value
	return total_dict


def word_frequencies(url):
	"""Counts the amount each word appears on a webpage"""
	texts = get_all_texts(url)
	count = count_words_in_sentence_list(texts)
	return count


print(word_frequencies('https://crawler-test.com/'))
