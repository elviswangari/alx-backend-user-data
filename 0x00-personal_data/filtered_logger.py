#!/usr/bin/env python3
'''
logging module
'''
from re import sub
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    '''replace sensitive info with redacted value'''
    for value in fields:
        message = sub(f'{value}=.*?{separator}',
                      f'{value}={redaction}{separator}', message)
    return message
