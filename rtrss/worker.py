"""Scheduler initialization and worker entry point"""
import sys
import logging
from rtrss import config
from rtrss.scheduler import Scheduler
from rtrss.database import clear_db, init_db, session_scope, engine, Session
from rtrss.manager import Manager

_logger = logging.getLogger(__name__)

logging.basicConfig(
    level=config.LOGLEVEL, stream=sys.stdout,
    format='%(asctime)s %(levelname)s %(name)s %(message)s')

# Limit 3rd-party packages logging
logging.getLogger('schedule').setLevel(logging.WARNING)
logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('googleapiclient').setLevel(logging.WARNING)
logging.getLogger('oauth2client').setLevel(logging.WARNING)


def populate_categories():
    with session_scope(Session) as db:
        manager = Manager(config, db)
        manager.populate_categories()


def import_categories():
    with session_scope(Session) as db:
        manager = Manager(config, db)
        manager.import_categories()


def main():
    if len(sys.argv) < 2 or sys.argv[1] == 'run':
        scheduler = Scheduler(config)
        return scheduler.run()

    elif sys.argv[1] == 'import_categories':
        import_categories()

    elif sys.argv[1] == 'populate_categories':
        populate_categories()

    elif sys.argv[1] == 'initdb':
        init_db(engine)

    elif sys.argv[1] == 'cleardb':
        clear_db(engine)

    else:
        _logger.error("Invalid parameters: %s", sys.argv)

if __name__ == '__main__':
    sys.exit(main())
