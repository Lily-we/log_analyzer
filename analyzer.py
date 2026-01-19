import re


LOG_PATTERN = re.compile(
    r'(?P<date>\d{4}-\d{2}-\d{2})\s+'
    r'(?P<time>\d{2}:\d{2}:\d{2})\s+'
    r'(?P<level>INFO|WARNING|ERROR)\s+'
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s+'
    r'(?P<message>.+)'
)


def parse_log_line(line: str) -> dict | None:
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    return match.groupdict()

def main():
    test_line = "2026-01-08 12:45:33 INFO 192.168.1.10 User logged in"
    parsed = parse_log_line(test_line)
    return parsed

if __name__ == "__main__":
    main()