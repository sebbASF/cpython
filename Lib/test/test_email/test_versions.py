#!/usr/bin/env python3

# Show that msg.as_bytes() is not consistent across Python versions

import email
import email.policy
import hashlib

def testmsg(filename):
    print(filename)
    policy = email.policy.default.clone(refold_source='none')
    with open(f"Lib/test/test_email/data/{filename}", encoding="utf-8") as fp:
        data = fp.read()
    msg = email.message_from_string(data,policy=policy)
    asbytes = msg.as_bytes()
    print(f"data:  len={len(data)} hash={hashlib.md5(data.encode()).hexdigest()}")
    print(f"bytes: len={len(asbytes)} hash={hashlib.md5(asbytes).hexdigest()} ")
    print(msg)

def main():
    testmsg('msg_50.txt')
    testmsg('msg_51.txt')

if __name__ == '__main__':
    main()
