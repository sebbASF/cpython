#!/usr/bin/env python3

import sys
import email
# from test.test_email import openfile
import hashlib

def msgobj(filename):
    with open(filename, encoding="utf-8") as fp:
        data = fp.read()
    msg = email.message_from_string(data)
    return msg, data

def main():
    msg, data = msgobj('Lib/test/test_email/data/msg_50.txt')
    asbytes = msg.as_bytes()
    print(sys.version)
    print(f"data:  len={len(data)} hash={hashlib.md5(data.encode()).hexdigest()}")
    print(f"bytes: len={len(asbytes)} hash={hashlib.md5(asbytes).hexdigest()} ")
    
if __name__ == '__main__':
    main()
