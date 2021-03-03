import requests
import re
from bs4 import BeautifulSoup

url = f'https://djinni.co/jobs/?keywords='


def extract_max_page(keyword):
    request = requests.get(
        f'{url}{keyword}&page=2')

    soup = BeautifulSoup(request.text, 'html.parser')

    paginator = soup.title

    pages = re.findall(r'\d+', paginator.text)
    return int(pages[-1])


def extract_job(html):
    title = html.find('a').text
    link = html.find('a')['href']
    link = f'https://djinni.co{link}'
    company = html.find(
        'div', {'class': 'list-jobs__details__info'}).find_all('a')[-1].text
    location = html.find('i', {'class': 'icon-location'}).next_sibling
    location = ' '.join(location.split())[:-2]
    return {'title': title, 'company': company, 'location': location, 'link': link}


def extract_jobs(last_page, keyword):
    jobs = []
    for page in range(last_page):
        print(f'Djinni: Парсинг страницы {page+1}')
        req_result = requests.get(f'{url}{keyword}&page={page+1}')
        soup = BeautifulSoup(req_result.text, 'html.parser')
        job_result = soup.find_all('li', {'class': 'list-jobs__item'})
        for job_html in job_result:
            job = extract_job(job_html)
            jobs.append(job)
    return jobs


def get_jobs(keyword):
    last_page = extract_max_page(keyword)
    jobs = extract_jobs(last_page, keyword)
    return jobs
