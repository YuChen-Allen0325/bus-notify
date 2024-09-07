import asyncio
import logging.config

from app.adaptor import pgsql
from app import logging_config
from app.handler.notify import do_async_notify


log = logging.getLogger(__name__)

def main():
    logging.config.dictConfig(logging_config.CONF)
    pgsql.init()
    # task1 = asyncio.create_task(do_async_notify('672', '博仁醫院', 'FAA-162'))
    # task2 = asyncio.create_task(do_async_notify('672', '博仁醫院', 'FAA-162'))
    # task3 = asyncio.create_task(do_async_notify('672', '博仁醫院', 'FAA-162'))
    # await asyncio.gather(task1, task2, task3)



    # while True:
    a = pgsql.get_user_reservation_information()
    print(a)
    for i in a:
        print(i.get('bus_number'))
main()
# asyncio.run(main())