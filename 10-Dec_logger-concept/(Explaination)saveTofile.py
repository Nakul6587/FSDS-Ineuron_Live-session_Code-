#this file is module and employee is current file
import os
import logging

# When we import module it will overright its log configuration in current file so that we can not create the another file through current file to overcome this we use logger 
# below there are the format for logger use as it is in any code
# If you are using the logger then replace logging by logger
# Need to use this logger format in current file also



logger=logging.getLogger(__name__) # Get the logger # this __name__ is will replace with file name i.e save to file because its a module so it will reflect with module file name in log file
logger.setLevel(logging.DEBUG)     # set the level

f=logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')  # Set the format here format stored in a f variable

fh=logging.FileHandler('saveTofile.log')    # create the file handler which will creat the file for you store this code in f varibale
fh.setFormatter(f)                          # set the format for new savetofile.log file which will handle by file handler

logger.addHandler(fh)

#logging.basicConfig(filename='saveTofile.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')   # no need to use this configuration delete it


def namecheck(name):
    logger.debug(f'checking name "{name}"....')
    if os.path.exists('data.txt'):
        with open('data.txt','r') as readFile:
            for line in readFile:
                if line.lower().startswith(f'name: {name.lower()}'):
                    logger.error(f'Name: "{name}" already exists')
                    return False
            if len(name) == 0:
                logger.critical('Name cannot be blank')
                return False
            elif not name.isalpha():
                logger.critical('name must be an alphabet')
                return False
            else:
                logger.error(f'check successfull')
                return True
    else:
        logger.debug('No data found')
        return True


def saveData(name,age,email):
    logger.debug(f'Saving details of {name}...')
    with open('data.txt','a') as appendFile:
        appendFile.write(f'Name: {name} - Age: {age} - Email: {email}\n')
        print(f'Details saved successfully')

logger.info('End of saveToFile Program')
logger.debug('########################')
