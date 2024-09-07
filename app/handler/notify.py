import asyncio
from app.handler.bus_service import notify_info, get_bus_event

def notify(bus_number, destination, BusID):  ## 將通知及查詢即時資訊包成一個耗時很久的工作

    info_stops = notify_info(bus_number, destination)  ## 672 路線動態資訊的routeID與靜態資源的routeID不一 動態資訊多一個0
    bus_event = get_bus_event(BusID)
    current_bus_stop_id = bus_event.get('StopID', -1)   ## -1 表示找不到該公車當前位置

    for i in info_stops:
        stop_name, StopID = i
        if StopID == current_bus_stop_id:   ## 提醒站點
            #####
            ##### 通知區
            #####
            print('yes')


async def do_async_notify(bus_number, destination, BusID):
    await asyncio.to_thread(notify(bus_number, destination, BusID))    # 使用to_thread來處理IO耗時很久問題