============
Key Concepts
============

presumption
============
The user has SSH keys for each device he uses and for each project.

As an example:

+---------------------------------------+------------------------------------+------------------------------------+
| Device: Laptop                        | Device: Desktop PC                 | Device: iPad                       |
|  * Work                               |  * Work                            |  * Work                            |
|  * Private                            |  * Private                         |  * Private                         |
|  * One-million-dollar Idea Project    |  * One-million-dollar Idea Project |  * One-million-dollar Idea Project |
+---------------------------------------+------------------------------------+------------------------------------+

One user alone already has 9 SSH keys that have to be managed and named. And each SSH key must be registered on different servers.
For a company with several users, there are several SSH Keys available.

Not to mention that the SSH keys must not only be entered on servers, but also on platforms like Gitlab/Github etc.

Another problem:
With each change, all locations where the SSH key was entered must be rolled out and changed again.

solution approach
=================

SSH Manager solves many of these problems.
The software is designed to solve these problems for a single user as well as for an entire company.

Several users can be created in the application, who can enter SSH keys for each of their devices and for each of their projects.
A trusted person can create publication "points", e.g. servers, platforms etc. and can check and roll out the keys of the different groups.

The same key can be used for several servers or for several users on one server.

Besides:Da SSH-Manager den verwaltungs overhead so gering wie möglich halten möchte ist es möglich SSH-Keys/Groups sowohl direkt einzutragen als auch über eine zweite Instanz zu beziehen

If the software is used within a company, an employee can link his Privately Installed version of the software to the installation of the company.
So he only has to manage the keys in his private installation. The program automatically synchronizes its keys with the installation in the company.


technical details
=================

Users can create multiple public ssh keys. ( The fingerprint is only allowed once per user).
The ssh keys are assigned to one device and one or more KeyGroup(s).

A trusted person or a user with appropriate rights can create publication points.
And the keys/groups of the users assign these publication points.

Publication points can be SSH servers or platforms.
The keys or key groups assigned to the publication points are assigned cyclically, event-bassiert or assigned and rolled out on manual triggering.

Since SSH-Manager wants to keep the administration overhead as low as possible it is possible to enter SSH-Keys/Groups directly as well as to get them from a second instance.