=======
Roadmap
=======


Feature List
============
 * Online Hosted Services
    * Synchronization Service
    * Managed Platform
 * CLI Tool
    * Use sshOCK without Webinterface
    * Control Online Hosted sshOCK Service (needed also for deploy keys to services)
 * SSH Jump Host
    * use sshOCK's structured data to display a list of all servers the user has access to
 * Share Public Keys via
    * sshOCK OnlineServces
    * E-Mail
    * Holepunching (also onlineservice)
    * Past/hastbin
    * FTP
    * syncthing
 * Imitieren bekannter APIs. z.B. GithubAPI zum abfragen der user public keys ODer LaunchPads
    * Diese funktion soll es ermöglichen, das der DNS so manipuliert wird, das z.B. bei der installation von Ubuntu
      die Public Keys direkt von sshOCK geladen werden.

v1.0.0
===========

Documentation:
  * Develop Roadmap
  * Descripe Key Concepts
  * Explain Database Structure
  * Embedd Code Autodocumentation

WebPortal:
  * Define Database Structure
  * Create Admin-UI for every Model
  * Create Frontend-UI for every Model
  * Unittests
  * Basic Functionality (SSHPublicKeys, KeyGroup, PublishGroup)
  * Celery Task Queuing (Deploy to OAuth2-Platform or Server)


v2.0.0
======

Documentation
 * Descripe Syncing over NATs

WebPortal
 * Implement Sync KeyGroups for two or more Instances


v3.0.0
======

Documentation
 *

WebPortal
 * Create a SSH-Jump Host Applicaiton