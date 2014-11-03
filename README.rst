CLick and Dial
==============

This package allow to call a partner or a contact by Openvoip provider.

In partner and contact form, near the Phone and mobile fields,
there is a button 'dial'. Click 'dial' button to call related phone number.


Configuration
-------------

In the company model set up these properties:

* Voip url: the service URL provided by openevoip SIP. You can use these variables inside the URL:
  1. sender
  2. dst
  3. id_call_gr
  4. verify

Eg.:
https://www.openvoip.it/click_and_dial.php?sender={sender}&dst={dst}&id_call_gr={id_call_gr}&verify={verify}

* Voip debug: this flag allow you to debug openvoip service without making a real call. Check you Odoo log for details.


For each user allowed to make a call by openevoip serive you should configure
these parameters

* Call Group Id
* Voip user number
* Voip user password

