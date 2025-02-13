#!/usr/bin/env python3

import sys
import email
import hashlib

def testmsg(filename):
    with open(f"Lib/test/test_email/data/{filename}", encoding="utf-8") as fp:
        data = fp.read()
    msg = email.message_from_string(data)
    asbytes = msg.as_bytes()
    print(f"data:  len={len(data)} hash={hashlib.md5(data.encode()).hexdigest()}")
    print(f"bytes: len={len(asbytes)} hash={hashlib.md5(asbytes).hexdigest()} ")

def main():
    testmsg('msg_50.txt')
    testmsg('msg_51.txt')
    
if __name__ == '__main__':
    main()
