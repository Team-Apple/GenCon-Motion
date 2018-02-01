import make_sentence
import datetime
import json
import requests

def str_to_date(str_date_time):
    str_date = str_date_time.split(' ')[0]
    date_time = datetime.datetime.strptime(str_date, '%Y-%m-%d')
    date = datetime.date(date_time.year, date_time.month, date_time.day)
    return date

def priority_to_value(priority):
    if priority == 'high': value = 1
    elif priority == 'normal': value = 2
    elif priority == 'low': value = 3
    else: value = -1
    return value

def get_talk_list():
    print 'Getting talk list.'
    talk_list = []
    now = datetime.datetime.now()
    now_time = datetime.time(now.hour, now.minute, now.second)
    today = datetime.date(now.year, now.month, now.day)
    tommorow = today + datetime.timedelta(days=1)
    pm = datetime.time(13,0,0)
    test_time = datetime.time(18,0,0)
    #Night
    if test_time >= pm:
        #tommorow event
        mode = 'b_event'
        url = 'https://gencon-web.herokuapp.com/api/events.json?start_at_date=' + str(tommorow)
        req = requests.get(url)
        event_list = json.loads(req.text)
        if event_list == []: print 'Tommorow event data does not exist.'
        for event in event_list:
            title = event['title']
            memo = event['memo']
            priority = event['priority']
            value = priority_to_value(priority)
            sentence = make_sentence.make_sentence(mode, title, memo)
            talk_list.append([sentence, value])
        #tommorow deadline task
        mode = 'b_task' 
        url = 'https://gencon-web.herokuapp.com/api/tasks.json?deadline_date=' + str(tommorow)
        req = requests.get(url)
        task_list= json.loads(req.text)
        if task_list == []: print 'Tommorow deadline task data does not exist.'
        for task in task_list:
            title = task['title']
            memo = task['memo']
            priority = task['priority']
            value = priority_to_value(priority)
            sentence = make_sentence.make_sentence(mode, title, memo)
            talk_list.append([sentence, value])
        #today start task
        mode = 's_task'
        url = 'https://gencon-web.herokuapp.com/api/tasks.json?start_from_date=' + str(today)
        req = requests.get(url)
        task_list= json.loads(req.text)
        if task_list == []: print 'Today start task data does not exist.'
        for task in task_list:
            title = task['title']
            memo = task['memo']
            priority = task['priority']
            value = priority_to_value(priority)
            sentence = make_sentence.make_sentence(mode, title, memo)
            talk_list.append([sentence, value])
    #Moring
    else:
        #today event
        mode = 'c_event'
        url = 'https://gencon-web.herokuapp.com/api/events.json?start_at_date=' + str(today)
        req = requests.get(url)
        event_list = json.loads(req.text)
        if event_list == []: print 'Today event data is not exist.'
        for event in event_list:
            title = event['title']
            memo = event['memo']
            priority = event['priority']
            value = priority_to_value(priority)
            sentence = make_sentence.make_sentence(mode, title, memo)
            talk_list.append([sentence, value])
        #today deadline task
        mode = 'c_task'
        url = 'https://gencon-web.herokuapp.com/api/tasks.json?deadline_date=' + str(today)
        req = requests.get(url)
        task_list= json.loads(req.text)
        if task_list == []: print 'Today deadline task data is not exist.'
        for task in task_list:
            title = task['title']
            memo = task['memo']
            priority = task['priority']
            value = priority_to_value(priority)
            sentence = make_sentence.make_sentence(mode, title, memo)
            talk_list.append([sentence, priority])

    """
    url = 'https://gencon-web.herokuapp.com/api/announcements.json'
    req = requests.get(url)
    lis = json.loads(req.text)
    print lis
    """
    talk_list = sorted(talk_list, key=lambda x: x[1])
    out = []
    for talk in talk_list:
        print talk[0].decode('utf-8')
        print str(talk[1])
        out.append(talk[0])
    print 'Done.'
    return out
