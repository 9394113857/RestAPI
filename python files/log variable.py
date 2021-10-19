# import logging
# raghu = logging.critical(' critical information')  # 50
# print(raghu)

# import logging
#
# logging.basicConfig(
#     format='%(asctime)s %(levelname)s %(message)s',
#     level=logging.DEBUG,
#     datefmt='%Y-%m-%d %H:%M:%S'
# )
#
# logging.debug('debug information')  # 10
# logging.info('info information')  # 20
# logging.warning('warning information')  # 30
# logging.error('error information')  # 40
# logging.critical('critical information') = raghu  # 50

# raghu = logging.critical(' critical information')  # 50
# print(raghu)



# raghu = logging.critical('critical information')  # 50
# print(raghu)

# log = logging.info('Just a random string...')
# logging.info('Just a random string...')
# print(log)

# 2030-01-01 00:00:00 INFO Just a random string...


from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

# print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)
# dt_string
Time = ("date and time =", dt_string)
print(Time)