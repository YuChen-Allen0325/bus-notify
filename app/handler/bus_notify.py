import asyncio
from app.adaptor import pgsql
from app.handler.gmail_service import send_email
from app.handler.bus_service import notify_info, get_bus_event

def notify(table_id, bus_number, destination, BusID, email):  ## 將通知及查詢即時資訊包成一個耗時很久的工作

    info_stops = notify_info(bus_number, destination)  ## 通知站點list, 672 路線動態資訊的routeID與靜態資源的routeID不一 動態資訊多一個0
    bus_event = get_bus_event(BusID)
    current_bus_stop_id = bus_event.get('StopID', -1)   ## -1 表示找不到該公車當前位置

    for i in info_stops:
        stop_name, notify_stop_id = i
        if notify_stop_id == current_bus_stop_id:   ## 提醒站點
            send_email(email)
            pgsql.update_notify_flag(table_id)  ## 通知成功把notify_flag 更新為 1


async def do_async_notify(table_id, bus_number, destination, BusID, email):
    await asyncio.to_thread(notify, table_id, bus_number, destination, BusID, email)    # 使用to_thread來處理IO耗時很久問題, 注意傳參比較特別