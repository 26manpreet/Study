#Logging levels:
- Not Set : NO LOGGING
- Debug   : Detailed info   
- Info    : info that operation is performed
- Warning : Some error may occur in future , but operation is being performed  --Default Level
- Error   : Error occured and some operation is not perfomed.
- Critical: Error occured and program itself failed

Logging is done by 2 Types of Loggers:
    1) Root Logger (simple logging)
    2) Custom Logger


#================================================
#-------SIMPLE APPROACH (Root Logger)-------
#================================================

import logging,datetime
  
# configure logger 
log_filename='Logfile_'+datetime.datetime.now().strftime('%d%b%Y_%H%M%S')+'.log'

logging.basicConfig(filename=log_filename,filemode='w', #a           , logger automatically takes care of file, if not exists create it
    format='%(asctime)s:: %(levelname)s :: %(filename)s :: Line no :: %(lineno)d -- %(message)s'    
    ,level=logging.ERROR)  #---Better  to put logging level in some config file and change when requires

logging.debug("its debug Message") 
logging.info("its an information") 
logging.warning("Its a Warning") 
logging.error("Its an error") 
logging.critical("its critical")

# log file will have error and critical message only.
# to displayo on console only avoid using filename
# By default format is : DEBUG: ROOT: MESSAGE




#================================================
#--------------CUSTOM LOGGER---------------------
#================================================


#WHY ROOT LOGGER IS NOT GOOD??

#test_module.py
import logging
logging.basicConfig(filename= file,level=logging.ERROR)
logging.error('Test Module error')

#main.py
import logging
import test_module
logging.basicConfig(filename = file,level=logging.DEBUG)  # No effect , since level will be setup by test_module.py
logging.info('main info')
logging.debug('main debug')
logging.error('main error')
logging.critical('main critical')

#output
ERROR:root:Test Module error
ERROR:root:main error
CRITICAL:root:main critical

#Reasons:
- Once Root logger is configured while importing tets_module, main module wont be able to change the settings
  Because, the logging.basicConfig() once set cannot be changed.
- That means, if you want to log the messages from test_module to one file and 
  the logs from the main module in another file, root logger can’t that.



# Create logger --> FileHandler -->  Formatter  --> add filehandler to logger
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  #wont effect
logger.error('my logging error') # wont display for info, as default level is Warning


#--------FileHandler and Formatter----------
    import logging
    
    # Gets or creates a logger
    logger = logging.getLogger(__name__)  
    
    # set log level
    logger.setLevel(logging.WARNING)   #Logger logging level, can also be also set at formmatter level e.,r either file_hadndler or stream_handler
    
    # create file handler and set formatter
    file_handler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')  # name -- __main__
    file_handler.setFormatter(formatter)   # name would be __main__ for same script
    #file_handler.setLevel(logging.CRITICAL)   # if want to set level at file_handler
    
    # add file handler to logger
    logger.addHandler(file_handler)
    
    """
    **********if want log on console only*********************
    stream_handler=logging.StreamHandler()   # this is only diff except same as file handler
    stream_handler.setFormatter(formatter)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    #file_handler.setLevel(logging.ERROR)
    logger.addHandler(stream_handler)
    """
    
    
    # Logs
    logger.debug('A debug message')
    logger.info('An info message')
    logger.warning('Something is not right.')
    logger.error('A Major error has happened.')
    logger.critical('Fatal error. Cannot continue')



NOTE:
- logger.exception
- __init__='__main__' will work for logger

- better to set logging level in cofig file, and change accordingly to debug the code at production

- try to create logger object in __name__=='__main__' part so that logger object dont need to pass in each function