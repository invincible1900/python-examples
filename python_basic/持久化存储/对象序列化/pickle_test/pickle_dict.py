# coding:utf-8
# python2.7
import cPickle as pickle
import os

tasks = [
    {'taskid': '1', 'taskobj': {'a': 1, 'b': 2}},
    {'taskid': '2', 'taskobj': {'a': 1, 'b': 2}},
    {'taskid': '3', 'taskobj': {'a': 1, 'b': 2}},
    {'taskid': '4', 'taskobj': {'a': 1, 'b': 2}},
]

def tasks_save(tasks, path='queue'):
    with open(path, 'wb') as f:
        pickle.dump(tasks, f, True)

def get_tasks(path='queue'):
    if os.path.exists(path):
        for task in pickle.load(open(path, 'rb')):
            print(task)

if __name__ == '__main__':
    tasks_save(tasks)
    get_tasks()
