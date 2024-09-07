import requests
import gzip
import io
import json
from app.config import BusConfig

def get_routeId_by_bus_number(bus_number):
    with requests.get(BusConfig.Route_URL) as response:
        
        compressed_file = io.BytesIO(response.content)
        with gzip.open(compressed_file, 'rb') as f_in:
            decompressed_data = f_in.read()

        all_routes = json.loads(decompressed_data.decode('utf-8')).get("BusInfo")

        for i in all_routes:
            if i.get("nameZh") == bus_number:
                return i.get('Id')
    return None


def get_bus_stops_to_notify(routeId, stopZh):   # 前3-5站  10785,   博仁醫院
    with requests.get(BusConfig.Stop_URL) as response:
        arr = []
        counter = 0
        dest_idx = None

        compressed_file = io.BytesIO(response.content)
        with gzip.open(compressed_file, 'rb') as f_in:
            decompressed_data = f_in.read()

        all_stops = json.loads(decompressed_data.decode('utf-8')).get("BusInfo")

        for i in all_stops:
            if i.get('routeId') == routeId:

                arr.append((i.get('nameZh'), i.get('Id')))
                if i.get('nameZh') == stopZh:
                    dest_idx = counter
                counter += 1
        
        if dest_idx is None:  # 找不到站點
            return []

    return arr[dest_idx-5:dest_idx-2]  # 前 3-5 站


def get_bus_event(BusID):
    with requests.get(BusConfig.Event_URL) as response:
        compressed_file = io.BytesIO(response.content)
        with gzip.open(compressed_file, 'rb') as f_in:
            decompressed_data = f_in.read()

        all_events = json.loads(decompressed_data.decode('utf-8')).get("BusInfo")
        for i in all_events:
            if i.get("BusID") == BusID:
                return i
    return {}


def notify_info(bus_number, destination): 
    notify_stops = []   ### 找不到路線回傳空
    route_id = get_routeId_by_bus_number(bus_number)   ## 公車號   '672'

    if route_id:
        notify_stops = get_bus_stops_to_notify(route_id, destination)  ## 目的地站點  '博仁醫院'

    return notify_stops