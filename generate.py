import json

import feedparser

BASE_DIR = './api'


def write_file(path, content):
    with open(path, 'w+') as f:
        f.write(content)


def gen_topics():
    data = [
        {
            'id': '3643', 'title': 'Mars Curiosity',
            'imageUrl': 'https://images-assets.nasa.gov/image/PIA14760/PIA14760~orig.jpg',
        },
        {
            'id': '3456', 'title': 'Space Station',
            'imageUrl': 'https://images-assets.nasa.gov/image/9131518/9131518~large.jpg'
        },
        {
            'id': '3451', 'title': 'Hubble Space Telescope',
            'imageUrl': 'https://images-assets.nasa.gov/image/9015550/9015550~orig.jpg'
        },
        {
            'id': '3631', 'title': 'Jono: Mission at Jupiter',
            'imageUrl': 'https://images-assets.nasa.gov/image/PIA13087/PIA13087~orig.jpg'
        },
    ]
    write_file(f'{BASE_DIR}/topics.json', json.dumps(data))


def gen_today():
    today_rss_link = 'https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss'
    rss = feedparser.parse(today_rss_link)
    data = []
    for entry in rss['entries']:
        title = entry['title']
        description = entry['summary']
        date = entry['published']
        link = entry['link']
        image_url = entry['links'][1]['href']
        data.append({
            'title': title,
            'description': description,
            'date': date,
            'link': link,
            'imageUrl': image_url,
        })
    write_file(f'{BASE_DIR}/today.json', json.dumps(data))


if __name__ == '__main__':
    gen_topics()
    gen_today()
