#!/usr/bin/env python3
'''
logging module
'''
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''replace sensitive info with redacted value'''
    for value in fields:
        message = re.sub(f'{value}=.*?{separator}'
                         f'{value}={redaction}{separator}', message)
    return message
