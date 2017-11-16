import make_sentence
import datetime
import json
import requests

def get_talk_list():
    talk_list = []
    today = datetime.date.today()
    #event
    url = 'https://gencon-web.herokuapp.com/api/events.json?start_at_date=' + str(today)
    req = requests.get(url)
    event_list = json.loads(req.text)
    mode = 'event'
    for event in event_list:
        title = event['title']
        memo = event['memo']
        sentence = make_sentence.make_sentence(mode, title, memo)
        talk_list.append(sentence)
    #task
    """
    #task
    mode = 's_task'
    url = 'https://gencon-web.herokuapp.com/api/events.json?start_at_date=' + str(today)
    req = requests.get(url)
    task_dic = json.loads(req.text)
    if task_dic == []: print 'task data is not exist.'
    for event in event_list:
        title = event['title']
        memo = event['memo']
        sentence = make_sentence.make_sentence(mode, title, memo)
        talk_list.append(sentence)
    mode = 'b_task'
    mode = 'c_task'
    """
    return talk_list
