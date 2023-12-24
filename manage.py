"""
Entrypoint
"""
import sys

from logger import get_logger

import config as _


logger = get_logger('manage')


if __name__ == '__main__':
    try:
        cmd = sys.argv[1]
    except IndexError:
        sys.exit(1)

    match cmd:
        case 'migrate':
            logger.info('Starting migrations')
            from core import db
            db.migrate()

        case 'runbot':
            logger.info('Starting bot')
            import asyncio
            import main
            asyncio.run(main.main())
