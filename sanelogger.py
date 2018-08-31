from termcolor import cprint
from datetime import datetime
import sys


class SaneLogger(object):
    OFF = 1
    FATAL = 2
    ERROR = 4
    WARN = 8
    INFO = 16
    DEBUG = 32
    TRACE = 64
    ALL = 64
    # ALL = FATAL + ERROR + INFO + WARN + DEBUG + TRACE

    __global_instance = None

    __global_level = None

    def __init__(self, name="", level="ALL", frmt: str = None, write_to_file=False, out_file=None):
        self.name = name
        self.frmt = frmt
        self.level = None
        self.write_to_file = write_to_file
        self.out_file = out_file
        self.set_level(level)
        self.out_file_hook = None
        self.show_caller_in_trace = True
        if write_to_file:
            if out_file is None:
                # USE DEFAULT FILE OUTPUT
                self.out_file = 'sane.log'

        if frmt is None:
            if name == "":
                self.set_format("{level}: {message}")
            else:
                self.set_format("{level}({name}): {message}")

        self.frmt_with_caller = "{level}({name}->{caller}): {message}"

    def build_message(self, level, message):
        new_format = self.frmt
        if level == self.TRACE and self.show_caller_in_trace:
            caller = self.__get_caller(3)
            new_format = self.frmt_with_caller.replace('{caller}', caller)

        if level is None:
            out_msg = message
        else:
            out_msg = new_format.replace(
                "{name}", self.name).replace("{level}", SaneLogger.level_name(level)).replace("{message}", str(message))
        self.__write_to_file('[{}] {}\n'.format(datetime.utcnow(), out_msg))
        return out_msg

    def __write_to_file(self, content):
        if self.write_to_file:
            with open(self.out_file, 'a') as f:
                f.write(content)

    def __get_caller(self, frame):
        return sys._getframe(frame).f_code.co_name

    @staticmethod
    def set_global_level(level):
        if isinstance(level, str):
            SaneLogger.__global_level = SaneLogger.level_value(level.upper())
        else:
            SaneLogger.__global_level = level
        return level

    @staticmethod
    def unset_global_level():
        SaneLogger.__global_level = None

    @staticmethod
    def global_logger(name="GLOBAL", level="ALL", frmt=None):
        if SaneLogger.__global_instance is None:
            def_logger = SaneLogger(name, level, frmt)
            SaneLogger.__global_instance = def_logger
            return def_logger
        return SaneLogger.__global_instance

    @staticmethod
    def level_name(level):
        if level == SaneLogger.OFF:
            return "OFF"
        if level == SaneLogger.TRACE:
            return "TRACE"
        if level == SaneLogger.DEBUG:
            return "DEBUG"
        if level == SaneLogger.WARN:
            return "WARN"
        if level == SaneLogger.INFO:
            return "INFO"
        if level == SaneLogger.ERROR:
            return "ERROR"
        if level == SaneLogger.FATAL:
            return "FATAL"
        return "ALL"

    @staticmethod
    def level_value(level):
        level = level.upper()
        if level == "OFF":
            return SaneLogger.OFF
        if level == "TRACE":
            return SaneLogger.TRACE
        if level == "DEBUG":
            return SaneLogger.DEBUG
        if level == "WARN":
            return SaneLogger.WARN
        if level == "INFO":
            return SaneLogger.INFO
        if level == "ERROR":
            return SaneLogger.ERROR
        if level == "FATAL":
            return SaneLogger.FATAL
        return SaneLogger.ALL

    def demo(self):
        self.fatal('Fatal message')
        self.trace('Trace message')
        self.error('Error message')
        self.warn('Warning message')
        self.debug('Debug message')
        self.info('Info message')
        self('Regular message')

    def set_level(self, level):
        if isinstance(level, str):
            self.level = self.level_value(level.upper())
        else:
            self.level = level
        return level

    def set_format(self, frmt):
        self.frmt = frmt

    def trace(self, message=None):
        if message is None:
            message = 'is called'

        if SaneLogger.__global_level:
            local_level = SaneLogger.__global_level
        else:
            local_level = self.level

        if local_level >= self.TRACE:
            print(self.build_message(self.TRACE, message))

    def debug(self, message):
        if SaneLogger.__global_level:
            local_level = SaneLogger.__global_level
        else:
            local_level = self.level

        if local_level >= self.DEBUG:
            cprint(self.build_message(self.DEBUG, message), color='magenta')

    def info(self, message):
        if SaneLogger.__global_level:
            local_level = SaneLogger.__global_level
        else:
            local_level = self.level

        if local_level >= self.INFO:
            cprint(self.build_message(self.INFO, message), color='green')

    def warn(self, message):
        if SaneLogger.__global_level:
            local_level = SaneLogger.__global_level
        else:
            local_level = self.level

        if local_level >= self.WARN:
            cprint(self.build_message(self.WARN, message), color='yellow')

    def error(self, message):
        if SaneLogger.__global_level:
            local_level = SaneLogger.__global_level
        else:
            local_level = self.level

        if local_level >= self.ERROR:
            cprint(self.build_message(self.ERROR, message), color='red')

    def fatal(self, message):
        if SaneLogger.__global_level:
            local_level = SaneLogger.__global_level
        else:
            local_level = self.level

        if local_level >= self.FATAL:
            cprint(self.build_message(self.FATAL, message), color='grey', on_color='on_red')

    @staticmethod
    def pos(message):
        cprint('{}'.format(message), color='cyan')

    @staticmethod
    def neg(message):
        cprint('{}'.format(message), color='red')

    def __call__(self, message):
        msg = self.build_message(None, message)
        print('{}'.format(msg))


if __name__ == '__main__':
    log1 = SaneLogger()
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
