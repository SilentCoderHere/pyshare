kb = 1024
mb = 1024**2
gb = 1024**3
tb = 1024**4


def sizeFormat(byte: int, round_: int = 2) -> str:
    byte = int(byte)
    if byte < kb:
        return f"{byte} B"
    elif byte < mb:
        size, unit = byte / kb, "KB"
    elif byte < gb:
        size, unit = byte / mb, "MB"
    elif byte < tb:
        size, unit = byte / gb, "GB"
    else:
        size, unit = byte / tb, "TB"
    return f"{round(size, round_)} {unit}"
