# SaneLogger
Sane logger for Python.

Default python logger is hard to use. So I made my own simple and sane logger.

# Usage

import sanelogger

logger = sanelogger.SaneLogger()

logger.trace("This is a TRACE message")
logger.debug("This is a DEBUG message")
logger.info("This is an INFO message")
logger.warn("This is a WARN message")
logger.error("This is an ERROR message")
logger.fatal("This is a FATAL message")



