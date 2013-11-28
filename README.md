mailtosms
=========

Small python script allowing to forward emails to a GSM modem

It's quite simple to use:

0. install the package smstools

        apt-get install smstools

Installing this tool creates a user called 'smsd' who will be in charge
of the whole SMS Server architecture

(Setup How-To: http://smstools3.kekekasvi.com/index.php?p=configure)

1. set up a rule in your Postfix installation that forwards emails
addressed to phonenumber@your.domain to the script

    * in /etc/postfix/master.cf

        transport_rule_name:	unix -	n	n	-	-	pipe
                flags=F user=smsd argv=/path/to/your/script

    * in /etc/postfix/transport

        your.domain	transport_rule_name:

There you go! Every mail sent to addresses like phonenumber@your.domain
should be sent to the phonenumber-part of the address.