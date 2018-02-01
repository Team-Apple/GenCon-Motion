# -*- coding: utf-8 -*-
import sys
import random

def check_error(args):
    modes = ['event', 's_task', 'b_task', 'c_task']
    if not len(args) == 4:
        print('Set three argments, mode(event, s_task, b_task, c_task), title and memo.')
        sys.exit()
    if not args[1] in modes:
        print('Set first argment event, s_task, b_task or c_task.')
        sys.exit()

def get_file_message(path):
    m_list = []
    f = open(path, "r")
    for line in f:
        line = line.replace('\n', '')
        m_list.append(line)
    f.close()
    random.shuffle(m_list)
    return m_list[0]

def make_sentence(mode, title, memo):
    out = get_file_message(mode + '.txt')
    if not title == '':
        out = out.replace('-', title.encode('utf_8'))
    if not memo == '':
        memorize = get_file_message('memo.txt')
        memo_out = memorize.replace('-', memo.encode('utf_8'))
        out += memo_out
    return out
