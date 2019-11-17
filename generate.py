import json

import feedparser

BASE_DIR = './api'


def write_file(path, content):
    with open(path, 'w+') as f:
        f.write(content)


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
    gen_today()
