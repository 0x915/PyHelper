import logging

import colorlog

logprint = True
logsave = False
logfile = "_debug.log"

log_colors_config = {
    'DEBUG'    : 'white',
    'INFO'     : 'green',
    'WARNING'  : 'yellow',
    'ERROR'    : 'red',
    'CRITICAL' : 'bold_red'}

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

if logsave :
    logfile_handler = logging.FileHandler(filename=logfile, mode='a', encoding='utf8')
    logfile_handler.setLevel(logging.INFO)
    logfile_formatter = logging.Formatter(
        fmt='[%(asctime)s.%(msecs)d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    logfile_handler.setFormatter(logfile_formatter)
    if not logger.handlers and logsave :
        logger.addHandler(logfile_handler)
    if logsave : logfile_handler.close()

if logprint :
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = colorlog.ColoredFormatter(
        fmt='%(log_color)s[%(asctime)s] %(message)s',
        datefmt='%m-%d %H:%M:%S',
        log_colors=log_colors_config)
    console_handler.setFormatter(console_formatter)
    if not logger.handlers and logprint :
        logger.addHandler(console_handler)
    if logprint : console_handler.close()


if __name__ == '__main__' :
    logger.debug('Debug')
    logger.info('Info')
    logger.warning('Warning')
    logger.error('Error')
    logger.critical('Critical')
