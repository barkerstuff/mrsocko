# mrsocko
The sophisticated socket activation tool, with client activity awareness and other features such as IP filtering and more.

## Why use socket activation, and why use mr socko? 
Socket activation has been a feature of *NIX type operating systems for many years, traditionally managed by inetd, and later by systemd in more modern systems.  This allows for functions to only be started on demand thereby saving system resources when they are not needed. 

The biggest issue with inetd is that one a service has been started, then it will continue to run indefinitely, meaning that resources would not be reclaimed until a reboot, or if e.g. shut down via a timed script.  Systemd allows for time based inactivation of the process.  However, the problem with these is that they may shut down when clients are accessing the service.  This can be a problem if a service is needed only on occasion but once started may be required to do an indeterminate amount of work, meaning that services are unintelligently terminated while they are still required.  Furthermore, there is no ability to only activate the service when specific IP addresses access the service, or to e.g. filter IP addresses which can prevent service shutdown. 

Mr Socko allows for much more sophisticated control is a lightweight with no dependency requiremenets beyond Python. It has been tested on severely resource depleted systems such as the rasperry pi zero and has very low overhead.

## Features
- Time based socket inactivation
- Activity based socket inactivation
- IP Filtering for socket activation
- Client activity detection with the ability for specific clients to prevent service inactivaion via IP filtering 
- Arbitrary binding options *(e.g. to only listen and activate when requests are received via specific hosts such as localhosts, or VPN clients*)
- TCP and UDP service support
- Full support for forking processes
- Ability to launch services via alternative user credentials
- Support for custom stop scripts *(useful to manage docker services)*
- Logging with log rotation
- Low resource usage
- Low dependencies *(only requires Python 3 standard libraries)*

## Installation
Installation is very simple.  Either download the main executable and chmod u+x and run mrsocko. 
Alternatively clone this repositority and run ./mrsocko
No dependencies are required outside of Python 3.
See systemd.conf for examples of systemd service configurations.

'git clone https://github.com/barkerstuff/mrsocko'
'cd mrsocko'
'./mrsocko'

To install system wide run ./install.sh

## Roadmap
- BSD support (not tested) 
- Support for port knocking sequences for service activation
- Optional startup messages for HTTP(s) clients so that users are made aware when a service is starting
- Windows and Mac OS X support
