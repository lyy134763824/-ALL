import logging
filename = 'test_log'
logging.basicConfig(
   level=logging.DEBUG,
    filename = filename+'.log',
   filemode='a',
   format= '%(asctime)s-[line:%(lineno)d]-%(levelname)s-%(message)s'
)

logging.info('info+iiii')
logging.debug('debug+dddd')
logging.warning('warning+www')
logging.error('error+eee')
logging.critical('critical+ccc')




