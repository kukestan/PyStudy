import logging
from datetime import datetime
import os

__inited = False

def init():
    if not os.path.exists('D:/code/python/log/'):
        os.mkdir('D:/code/python/log/')
    fn = 'D:/code/python/log/%s_%s_%d.txt'%(datetime.now().date(), \
                                       datetime.now().time().strftime('%H_%M_%S'), \
                                                    datetime.now().time().microsecond)
    logging.basicConfig(filename = fn, format = '%(asctime)s: %(levelname)-8s: %(message)s', level=logging.DEBUG)
    logging.addLevelName
    __inited = True

def logd(log, tag = ''):
    if not __inited:
        init()

    if len(tag) == 0:
        logging.debug('%s'%log)
    else:
        logging.debug('%s: %s'%(tag, log))

def clean():
    filelist = os.listdir('D:/code/python/log/')
    for f in filelist:
        os.remove('D:/code/python/log/%s'%f)
    os.removedirs('D:/code/python/log')

#remove('D:/code/python/log/')
#logging.warning('456')
#logging.critical('789')