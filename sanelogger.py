OFF = 1
FATAL = 2
ERROR = 4
WARN = 8
INFO = 16
DEBUG = 32
TRACE = 64
ALL = FATAL + ERROR + INFO + WARN + DEBUG + TRACE

def level_name(level):
    if level == OFF:
        return "OFF"
    if level == TRACE:
        return "TRACE"
    if level == DEBUG:
        return "DEBUG"
    if level == WARN:
        return "WARN"
    if level == INFO:
        return "INFO"
    if level == ERROR:
        return "ERROR"
    if level == FATAL:
        return "FATAL"
    return "ALL"


class SaneLogger(object):
    OFF = 1
    FATAL = 2
    ERROR = 4
    WARN = 8
    INFO = 16
    DEBUG = 32
    TRACE = 64
    ALL = FATAL + ERROR + INFO + WARN + DEBUG + TRACE

    def __init__(self, name="", level=ALL, frmt=None):
        """
        A logger that acts sane.

        :param name: Logger name
        :param level: Log level
        :param frmt: Message format.
        """
        self.name = name
        self.level = level
        self.frmt = frmt

        if frmt is None:
            if name == "":
                self.set_format("{level}: {message}")
            else:
                self.set_format("{level}({name}): {message}")

    def build_message(self, level, message):
        return self.frmt.replace("{name}", self.name).replace("{level}", level_name(level)).replace("{message}",
                                                                                                    str(message))

    def set_level(self, level):
        self.level = level
        return level

    def set_format(self, frmt):
        self.frmt = frmt

    def trace(self, message):
        if self.level >= self.TRACE:
            print(self.build_message(self.TRACE, message))

    def debug(self, message):
        if self.level >= self.DEBUG:
            print(self.build_message(self.DEBUG, message))

    def info(self, message):
        if self.level >= self.INFO:
            print(self.build_message(self.INFO, message))

    def warn(self, message):
        if self.level >= self.WARN:
            print(self.build_message(self.WARN, message))

    def error(self, message):
        if self.level >= self.ERROR:
            print(self.build_message(self.ERROR, message))

    def fatal(self, message):
        if self.level >= self.FATAL:
            print(self.build_message(self.FATAL, message))


log = SaneLogger()


# log1 = SaneLogger()
# for i in range(8):
#     level = 2**i
#     log1.set_level(level)
#     print("==== Level set to " + level_name(log1.level))
#     log1.trace("TRACE")
#     log1.debug("debug")
#     log1.info("this is an info")
#     log1.warn("this is a warning")
#     log1.error("error message")
#     log1.fatal("fatal message")
