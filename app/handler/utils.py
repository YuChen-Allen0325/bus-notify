def safe_slice(lst, start, end):
    if start >= len(lst) or end <= 0 or start >= end:
        return lst  
    start_index = max(0, start)
    end_index = min(len(lst), end)
    return lst[start_index:end_index]