import logging

# logging.basicConfig(filename='log.txt', level=30) // Even you are not setting also it is by default WARNING only.
# Filename:-
logging.basicConfig(filename="F:\Restful-API's\RestAPI\log files\est.log",
                    level=logging.error('Raghu raising a warning...'),
                    filemode='a')  # W override, a append, default value is append
# logging.basicConfig(format='%(levelname)s') # I want level name only
# logging.basicConfig(format='%(levelname)s:%(message)s') # Level name and message by default is going to come
# logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s') # Level name and message with data and time.
# date/month/Year hour/min/sec p-means AM and Pm for 12 hor scale only.

log = logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
print(log)

# print('logging module demo') # It is the normal print statement it is going to print only in the cosole not in the log file.
logging.debug('debug information')  # 10
logging.info('info information')  # 20
logging.warning('warning information')  # 30
logging.error('error information')  # 40
logging.critical('critical information')  # 50

log = logging.info('Just a random string...')
print(log)

# filename='D:\\log.txt'
# F:\Restful-API's\Restful-API's\log files
