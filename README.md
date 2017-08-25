# ALH protocol "Hello World" example

This is a minimal example of using ALH protocol to communicate between a VESNA
node and a Python script on a Linux system.

More about ALH:

 * [VESNA ALH tools](https://github.com/avian2/vesna-alh-tools) is a Python
   library for talking the ALH protocol that works through various transports.
   We are using direct serial connection in this example.

 * ALH protocol is described in more detail in this [Google
   document](https://docs.google.com/document/d/1-MZuzc70BdjLh3vHt7e3vrt4-ABZV4do3vuVWwiyKqI/edit)

 * Computer-side of the communication can also be handled by the [Logatec
   infrastructure](https://github.com/sensorlab/logatec-infrastructure) Java
   application.

## Setup

These steps assume that you have a working development environment setup. See
the [VESNA manual](https://sensorlab.github.io/vesna-manual/) for details on
how to setup. You need to have a VESNA SNC connected over JTAG to an Olimex
ARM-USB-OCD programmer. The USART1 should be connected over the serial-to-USB
converter to `/dev/ttyUSB0` device (if you are using another device, you should
first correct the device path in `hello.py`).

Download VESNA firmware:

    $ git clone -b add-parser-example git@github.com:avian2/vesna-drivers.git

Compile firmware:

    $ cd vesna-drivers/Examples/VSNFunctions/LogatecParser
    $ make

Upload firmware (using OpenOCD 0.8.0 and Olimex ARM-USB-OCD):

    $ make LogatecParserDemo.load8

Setup Python environment. Note that we are using Python 2.7 and an older
version of the `vesna-alh-tools` package. There are some unresolved problems
with Python 3 support at the moment:

    $ cd ../../../..
    $ virtualenv -p python2.7 venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt

Run the example:

    $ python hello.py
    Making GET request
    INFO:vesna.alh:     GET: hello?arg1=value1
    INFO:vesna.alh:response: Hello World!
    I got a GET request:
        args="arg1=value1
    "
    Response: Hello World!
    I got a GET request:
        args="arg1=value1
    "

    Making POST request
    INFO:vesna.alh:    POST: hello?arg2=value2
    INFO:vesna.alh:    DATA: example post data
    INFO:vesna.alh:response: Hello World!
    I got a POST request:
        args="arg2=value2"
        data="\x65\x78\x61\x6D\x70\x6C\x65\x20\x70\x6F\x73\x74\x20\x64\x61\x74\x61"
        len=17
    Response: Hello World!
    I got a POST request:
        args="arg2=value2"
        data="\x65\x78\x61\x6D\x70\x6C\x65\x20\x70\x6F\x73\x74\x20\x64\x61\x74\x61"
        len=17
