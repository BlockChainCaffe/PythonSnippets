import logging

##### Basic use
# use the module itself, no objects
logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(filename)-15s %(lineno)-5d : %(message)s'
    )
#logging.debug("Record created: {} (${})".format(name, value))

# fire
logging.debug("so that you know something")
logging.info("this is just an info")
logging.warning("could be better")
logging.error("Huston...")
logging.critical("Program can't continue")

##### Log Levels
#CRITICAL 	50	logging.critical()
#ERROR		40	logging.error()
#WARNING	30	logging.warning()
#INFO		20	logging.info()
#DEBUG		10	logging.debug()
#NOTSET		0
