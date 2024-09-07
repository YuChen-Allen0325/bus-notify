import asyncio
import logging.config
from app.adaptor import pgsql
from app import logging_config
from app.handler.bus_notify import do_async_notify


log = logging.getLogger(__name__)


async def main():

    logging.config.dictConfig(logging_config.CONF)
    pgsql.init()

    while True:
        tasks = []
        notify_informations = pgsql.get_user_reservation_information()

        for notify_information in notify_informations:   ## 創建通知任務list
            id = notify_information.get('id')
            bus_number = notify_information.get('bus_number')
            destination_stop = notify_information.get('destination_stop')
            bus_id = notify_information.get('bus_id')
            email = notify_information.get('email')
            tasks.append(asyncio.create_task(do_async_notify(id, bus_number, destination_stop, bus_id, email)))

        await asyncio.gather(*tasks)


asyncio.run(main())
