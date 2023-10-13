# mrsocko
The sophisticated socket activation tool, with client activity awareness and other features such as IP filtering and more.

## Why use socket activation, and why use mr socko? 
Socket activation has been a feature of *NIX type operating systems for many years, traditionally managed by inetd, and later by systemd in more modern systems.  This allows for functions to only be started on demand thereby saving system resources when they are not needed. 

The biggest issue with inetd and systemd for this purpose is that one a service has been started, then it will continue to run indefinitely with no awareness of what is going on.  Traditionally shutdown would occur via some timer, which can mean that the service will close down in the middle of activity or when providing services to clients, and there is no granularity over which IP addresses can activate the service.

Mr Socko solves these issues, allowing for services to be gracefully started and shut down only when they are not needed.  Furthermore, it is lightweight with no dependency requiremenets beyond the standard Python libraries. It has been tested on resource depleted systems such as the rasperry pi zero and has very low overhead.

## Features
- Time based socket inactivation
- Activity based socket inactivation with client whitelists
- IP Filtering and custom subnet binding for socket activation
- Client activity awareness with the ability for specific clients to prevent service inactivaion via IP whitelists 
- TCP and UDP service support
- Full support for forking processes
- Ability to launch services via alternative user credentials
- Support for custom stop scripts *(useful to manage docker services)*
- Logging with automatic log rotation
- Low resource usage
- Low dependencies *(only requires Python 3 standard libraries)*

## Installation
Installation is very simple.  Either download the main executable and chmod u+x and run mrsocko. 
Alternatively clone this repositority and run ./mrsocko
No dependencies are required outside of Python 3.
See systemd.conf for examples of systemd service configurations.

```
git clone https://github.com/barkerstuff/mrsocko
cd mrsocko
/mrsocko
```

To install system wide run ./install.sh

## Roadmap
- BSD support (not tested) 
- Support for port knocking sequences for service activation
- Optional startup messages for HTTP(s) clients so that users are made aware when a service is starting
- Windows and Mac OS X support
