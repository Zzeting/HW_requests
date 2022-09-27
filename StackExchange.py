import requests
from pprint import pprint
from datetime import datetime


def get_questions_staroverflow(tagged):
    url = 'https://api.stackexchange.com/2.3/questions'
    from_date = round(datetime.now().timestamp()) - 172800
    to_date = round(datetime.now().timestamp())
    question_tag_python = []
    while True:
        params = {'page': 1,
                  'pagesize': 100,
                  'fromdate': from_date,
                  'todate': to_date,
                  'order': 'desc',
                  'sort': 'creation',
                  'tagged': tagged,
                  'site': 'ru.stackoverflow'}
        response = requests.get(url, params=params)
        if response.status_code >= 400:
            print('Error:', response.status_code)
            return
        questions = response.json()
        if questions['has_more']:
            question_tag_python.append(questions)
            params['page'] += 1
        else:
            break
    return question_tag_python


if __name__ == '__main__':
    questions_python = get_questions_staroverflow()
    pprint(questions_python)


