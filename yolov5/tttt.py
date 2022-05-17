import os
import datetime
log_dir='./log/'+datetime.datetime.now().strftime('%Y%m%d')
if not os.path.exists(log_dir):
    print('creat log')
    os.makedirs(log_dir)
else:
    print(log_dir+' is exist')    
