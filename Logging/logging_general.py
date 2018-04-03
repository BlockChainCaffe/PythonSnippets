import logging

##### Basic use
# use the module itself, no objects
logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )
logging.debug("Record created: {} (${})".format(name, value))



##### Advanced use

### Create logger object
# generic
logger = logging.getLogger('myapp')
## module specific with no name collision
logger = logging.getLogger('__name__')
## hierarchical multi logging:
# with logger.propagate=True, events in sonlog will
# be in fatherlog too
fatherlog = logging.getLogger('father')
sonlog = logging.getLogger('father.son')

### Create Handlers
# file logging
hdlr = logging.FileHandler('/var/tmp/myapp.log')

# create formats
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(lineno)d %(message)s')
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)-15s %(lineno)-5d : %(message)s')

# put it all together (handler, format and level)
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)

# fire
logger.debug("so that you know something")
logger.info("this is just an info")
logger.warning("could be better")
logger.error("Huston...")
logger.critical("Program can't continue")

##### Log Levels
#CRITICAL 	50	logging.critical()
#ERROR		40	logging.error()
#WARNING	30	logging.warning()
#INFO		20	logging.info()
#DEBUG		10	logging.debug()
#NOTSET		0