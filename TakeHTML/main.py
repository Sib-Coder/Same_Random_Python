import requests

urls = 'https://habr.com/ru/post/480838/'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}


def take_html(url, headers):
    r = requests.get(url, headers)
    with open('test.html', 'w+', encoding='utf-8') as output_file:
        output_file.write(r.text)


take_html(urls, header)
