# Update Solr via FGS by PID
A script that will parse a list of PIDs to update their index information in FGS and Solr.

Requirements
--
Python 3.x

Modules: requests, getpass

`pip install <module name>` should work for each required module.


What does this do?
--
when provided a list of PIDs (url encoded, i.e.: ':' becomes '%3A') this script
logs in to Fedora Generic Search and updates by PID. This update by PID forces
FGS to check that PID and send index data to Solr.

Solr MUST be optimized after running this script. @TODO: explain how to opt Solr index.


How to use:
--
@TODO