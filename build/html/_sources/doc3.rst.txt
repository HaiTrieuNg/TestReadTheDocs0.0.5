**Doc 3**

**Version 1.0.0**

Version Notes：

========== ======= ================================
Date       Version Description
========== ======= ================================
2020/05/12 1.0.0   Phase-1 AT commands, first draft
\                  
========== ======= ================================

**Table of Contents**

1 Command Description 1

2 Basic AT Commands 2

2.1 Overview 2

2.2 Commands 2

2.2.1 AT \- Test AT 2

2.2.2 ATE \- Configure echo of AT commands 2

2.2.2 AT+RST \- Restart module 2

2.2.3 AT+GMR – Check version information 3

2.2.4 AT+RESTORE \- Restore factory default setting 3

2.2.5 AT+UART_CUR \- Current UART configuration, not save in Flash 3

2.2.6 AT+UART_DEF \- Default UART configuration, save in Flash 4

2.2.7 AT+SYSRAM \- Check the available RAM size 5

5 CSV Table Sample 1


1 Command Description
======================

.. raw:: html

    <font color="blue">Blue word,</font>




Some :red:`red colored text`.

Some :blue:`blue colored text`. Not blue anymore.

Some :big:`big text`.

Each command set contains four types of AT commands：

+-----------------+--------------+-----------------------------------+
| type            | format       | description                       |
+=================+==============+===================================+
| Test Command    | AT+<x>=?     | Queries the Set Command’s         |
|                 |              | internal parameters and their     |
|                 |              | range of values.                  |
+-----------------+--------------+-----------------------------------+
| Query Command   | AT+<x>?      | Return the current value of       |
|                 |              | parameters.                       |
+-----------------+--------------+-----------------------------------+
| Set Command     | AT+<x>=<...> | Sets the value of user-defined    |
|                 |              | parameters in commands,           |
|                 |              |                                   |
|                 |              | and runs these commands.          |
+-----------------+--------------+-----------------------------------+
| Execute Command | AT+<x>       | Runs commands with no             |
|                 |              | user-defined parameters.          |
+-----------------+--------------+-----------------------------------+


Some :red:`red colored text` again!

Notes：

.. raw:: html

<font color="blue">1. Not all AT commands support all four variations mentioned above.<br>2. Square brackets [ ] designate the default value; it is either not required or may not appear.</font>

3. String values need to be included in double quotation marks, for
   example: AT+CWSAP="BFQ756290","21030826", 1,4

4. The default baud rate is 115200

5. AT commands have to be capitalized, and must end with a new line (CR
   LF)


2 Basic AT Commands
====================================

2.1 Overview
------------

=========== =============================================
commands    description
=========== =============================================
AT          Test AT
ATE         Configure echo of AT commands
AT+RST      Restart module
AT+GMR      Check version info
AT+RESTORE  Restore factory default setting
AT+UART_CUR Current UART configuration, Not save in Flash
AT+UART_DEF Default UART configuration, save in Flash
AT+SYSRAM   Check the available RAM size
=========== =============================================

2.2 Commands
------------

2.2.1 AT \- Test AT
~~~~~~~~~~~~~~~~~~

=============== ==
Execute Command AT
=============== ==
Response        OK
Parameters       \-
=============== ==

2.2.2 ATE \- Configure echo of AT commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ==
Execute Command AT
=============== ==
Response        OK
Parameters      \-
=============== ==

2.2.2 AT+RST \- Restart module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ======
Execute Command AT+RST
=============== ======
Response        OK
Parameters      \-
=============== ======

2.2.3 AT+GMR – Check version information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ==================
Execute Command AT+GMR
=============== ==================
Response        <AT version info >
                
                <SDK version info>
                
                <compile time>
                
                OK
Parameters      \-
example         AT+GMR
=============== ==================

2.2.4 AT+RESTORE \- Restore factory default setting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------+---------------------------------------------------+
| Execute Command | AT+RESTORE                                        |
+=================+===================================================+
| Response        | OK                                                |
+-----------------+---------------------------------------------------+
| Parameters      | \-                                                 |
+-----------------+---------------------------------------------------+
| Note            | The execution of this command will reset all      |
|                 | parameters saved in flash and restore the factory |
|                 | default settings of the module. The chip will be  |
|                 | restarted when this command is executed           |
|                 |   The execution of this command will reset all    |
|                 | parameters saved in flash and restore the factory |
|                 | default settings of the module. The chip will be  |
|                 | restarted when this command is executed           |
|                 |                                                   |
+-----------------+---------------------------------------------------+

2.2.5 AT+UART_CUR \- Current UART configuration, not save in Flash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------------------------+----------------------------+
| Command  | Query Command:             | Set Command：              |
|          |                            |                            |
|          | AT+UART_CUR?               | AT+UART                    |
|          |                            | _CUR=<baudrate>,<databits> |
|          |                            | ,<stopbits>,<parity>,<flow |
|          |                            | control>                   |
+==========+============================+============================+
| Response | +UART                      | OK                         |
|          | _CUR:<baudrate>,<databits> |                            |
|          |                            |                            |
|          | ,<stopbits>,<parity>,<flow |                            |
|          | control>                   |                            |
|          |                            |                            |
|          | OK                         |                            |
+----------+----------------------------+----------------------------+
| Example  | AT+UART_CUR?               | AT+UART_CUR=115200,8,1,0,3 |
+----------+----------------------------+----------------------------+
| Note     | <baudrate>：UART baud rate |                            |
|          |                            |                            |
|          | <databits>：data bits      |                            |
|          |                            |                            |
|          | 5： 5-bit data             |                            |
|          |                            |                            |
|          | 6： 6-bit data             |                            |
|          |                            |                            |
|          | 7： 7-bit data             |                            |
|          |                            |                            |
|          | 8： 8-bit data             |                            |
|          |                            |                            |
|          | <stopbits>：stop bits      |                            |
|          |                            |                            |
|          | 1： 1-bit stop bit         |                            |
|          |                            |                            |
|          | 2： 1.5-bit stop bit       |                            |
|          |                            |                            |
|          | 3： 2-bit stop bit         |                            |
|          |                            |                            |
|          | <parity>：parity bit       |                            |
|          |                            |                            |
|          | 0： None                   |                            |
|          |                            |                            |
|          | 1： Odd                    |                            |
|          |                            |                            |
|          | 2： Even                   |                            |
|          |                            |                            |
|          | <flow control>：flow       |                            |
|          | control                    |                            |
|          |                            |                            |
|          | 0：disable                 |                            |
|          |                            |                            |
|          | 1：enable RTS              |                            |
|          |                            |                            |
|          | 2：enable CTS              |                            |
|          |                            |                            |
|          | 3：enable both RTS and CTS |                            |
+----------+----------------------------+----------------------------+

2.2.6 AT+UART_DEF \- Default UART configuration, save in Flash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------------------------+----------------------------+
| Command  | Query Command:             | Set Command：              |
|          |                            |                            |
|          | AT+UART_DEF?               | AT+UART                    |
|          |                            | _DEF=<baudrate>,<databits> |
|          |                            | ,<stopbits>,<parity>,<flow |
|          |                            | control>                   |
+==========+============================+============================+
| Response | +UART                      | OK                         |
|          | _DEF:<baudrate>,<databits> |                            |
|          |                            |                            |
|          | ,<stopbits>,<parity>,<flow |                            |
|          | control>                   |                            |
|          |                            |                            |
|          | OK                         |                            |
+----------+----------------------------+----------------------------+
| Example  | AT+UART_DEF?               | AT+UART_DEF=115200,8,1,0,3 |
+----------+----------------------------+----------------------------+
| Note     | <baudrate>：UART baud rate |                            |
|          |                            |                            |
|          | <databits>：data bits      |                            |
|          |                            |                            |
|          | 5： 5-bit data             |                            |
|          |                            |                            |
|          | 6： 6-bit data             |                            |
|          |                            |                            |
|          | 7： 7-bit data             |                            |
|          |                            |                            |
|          | 8： 8-bit data             |                            |
|          |                            |                            |
|          | <stopbits>：stop bits      |                            |
|          |                            |                            |
|          | 1： 1-bit stop bit         |                            |
|          |                            |                            |
|          | 2： 1.5-bit stop bit       |                            |
|          |                            |                            |
|          | 3： 2-bit stop bit         |                            |
|          |                            |                            |
|          | <parity>：parity bit       |                            |
|          |                            |                            |
|          | 0： None                   |                            |
|          |                            |                            |
|          | 1： Odd                    |                            |
|          |                            |                            |
|          | 2： Even                   |                            |
|          |                            |                            |
|          | <flow control>：flow       |                            |
|          | control                    |                            |
|          |                            |                            |
|          | 0：disable                 |                            |
|          |                            |                            |
|          | 1：enable RTS              |                            |
|          |                            |                            |
|          | 2：enable CTS              |                            |
|          |                            |                            |
|          | 3：enable both RTS and CTS |                            |
+----------+----------------------------+----------------------------+

2.2.7 AT+SYSRAM \- Check the available RAM size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

================ ==================================================
Query Command    AT+SYSRAM?
================ ==================================================
Response         +SYSRAM:<remain RAM size>
                 
                 OK
Example          AT+SYSRAM?
Response Example +SYSRAM:30000
                 
                 OK
Note             <remain RAM size>：remain space of RAM, unit: Byte
================ ==================================================


5 CSV Table Sample
==================

.. csv-table:: Sample table
   :file: tables/sampleCSV.csv
   :header-rows: 1
   :class: longtable
   :widths: auto

.. _section-1:
