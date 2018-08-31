# SaneLogger
Sane logger for Python.

Default python logger is hard to use. So I made my own simple and sane logger.

# Usage

```python
from sanelogger import SaneLogger

if __name__ == '__main__':
    log1 = SaneLogger(level=SaneLogger.ALL)
    for i in range(8):
        level1 = 2 ** i
        log1.set_level(level1)
        print("==== Level set to " + log1.level_name(log1.level))
        log1.trace("This is an trace message")
        log1.debug("This is an debug message")
        log1.info("This is an info message")
        log1.warn("This is a warning message")
        log1.error("This is en error message")
        log1.fatal("This is a fatal message")

    print('--- Following messages are not based on log level. They will always be printed.')
    log1('This is a regular message')
    log1.pos('This is a positive message')
    log1.neg('This is a negative message')
```


![output](https://github.com/ramazanpolat/sanelogger/raw/master/sane.PNG)
