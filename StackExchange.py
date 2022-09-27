import requests
from datetime import datetime


def get_questions_staroverflow(tagged):
    url = 'https://api.stackexchange.com/2.3/questions'
    from_date = round(datetime.now().timestamp()) - 172800
    to_date = round(datetime.now().timestamp())
    question_tag_python = []
    params = {'page': 1,
              'pagesize': 100,
              'fromdate': from_date,
              'todate': to_date,
              'order': 'desc',
              'sort': 'creation',
              'tagged': tagged,
              'site': 'ru.stackoverflow',
              'filter': '!4)LbtfpmvKGD8R16j'}
    while True:
        response = requests.get(url, params=params)
        questions = response.json()
        question_tag_python.append(questions)
        params['page'] += 1
        if not questions['has_more']:
            break
    return question_tag_python


def get_questions(tagged):
    count = 0
    questions_list = get_questions_staroverflow(tagged=tagged)
    for question in questions_list[0]['items']:
        print(f'Дата публикации вопроса: '
              f'{datetime.utcfromtimestamp(question["creation_date"]).strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'Опубликовал пользователь "{question["owner"]["display_name"]}" ID: {question["owner"]["account_id"]}\n'
              f'Cсылка на аккаунт пользователя: {question["owner"]["link"]}\n'
              f'Опубликованный вопрос: "{question["title"]}"\n'
              f'Ссылка на вопрос: {question["link"]}')
        print()
        print()
        count += 1
    print('Всего вопросов за последние два дня:', count)
