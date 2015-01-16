import sys
import os
import logging
import atexit
from rtrss.basedaemon import BaseDaemon

_logger = logging.getLogger(__name__)


class WorkerDaemon(BaseDaemon):
    def run(self):
        _logger.info('Daemon started ith pid %d', os.getpid())
        
        from rtrss.worker import app_init, worker_action
        worker_action('import_categories') # TODO run()
        
        _logger.info('Daemon is done and exiting')

    def start(self):
        _logger.info('Starting daemon')
        super(WorkerDaemon, self).start()

    def stop(self):
        _logger.info('Stopping daemon')
        super(WorkerDaemon, self).stop()

    def restart(self):
        _logger.info('Restarting daemon')
        super(WorkerDaemon, self).restart()
    

def make_daemon(config):
    '''Returns WorkerDaemon instance'''
    pidfile = os.path.join(config.DATA_DIR, 'daemon.pid')
    logdir = os.environ.get('OPENSHIFT_LOG_DIR') or config.DATA_DIR
    logfile = os.path.join(logdir, 'daemon.log')
    return WorkerDaemon(pidfile, stdout=logfile, stderr=logfile)
    