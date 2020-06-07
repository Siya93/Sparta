import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    a_tag = music.select_one('td.info > a.title.ellipsis')
    if a_tag is not None:
        rank_before= music.select_one('td.number')
        rank_before.span.decompose()
        rank=rank_before.text.strip()
        title = a_tag.text.strip()
        artist = music.select_one('td.info > a.artist.ellipsis').text
        print(rank, title, artist)

        #rank_before= music.select_one('td.number').span.decompose()
        #rank=rank_before.text.strip()
        #title = a_tag.text.strip()
        #artist = music.select_one('td.info > a.artist.ellipsis').text
        #print(rank, title, artist)