#-*-coding: utf-8-*-
#!/usr/bin/env python

import sys
import tempfile

from email.parser import Parser

if __name__ == '__main__':

    stdin = sys.stdin.read()

    headers = Parser().parsestr(stdin)

    sender = headers['From']
    receiver = headers['To']
    subject = headers['Subject']

    #in my own experience the mail content is separated
    #from the headers by 2 new lines

    start = stdin.find('\n\n') + 2
    end = len(stdin)
    mail = stdin[start:end]

    phonenumber = receiver.split('@')[0]

    sms = 'To: {0}\n\n{1}\n--\n{2}'.format(phonenumber,
                                           mail, sender)

    #now we create the temporary file for smstools outgoing queue
    tmp = tempfile.mkstemp(prefix='send_',
                           dir='/var/spool/sms/outgoing/', text=True
                          )
    with open(tmp[1],'w') as f:
        f.write(sms)
