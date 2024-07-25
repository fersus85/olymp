from datetime import timedelta


def format_timedelta(td: timedelta) -> str:
    total_seconds = int(td.total_seconds())
    _, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = td.microseconds // 100000
    return f"{minutes:02}:{seconds:02},{milliseconds:02}"
