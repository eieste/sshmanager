
====
Real
====


Nutzer haben geräte & für jedes gerät unterschiedliche SSH-Keys


Administratoren haben Server, für jeden Server gibt es unterschiedliche User
Administratoren haben Management Platformen z.B. gitlab. Die Platformen haben ebenfalls unterschiedliche Nutzer

Administratoren gewähren dem nutzer Zugang zum Server

Nutzer wählt Gruppen/Keys aus, welche auf den spezifischen Server installiert werden sollen


Account
============

 * Ein Nutzer hat mehrere ``KeyGroups``
 * Ein Nutzer hat mehrere ``Devices``

 * Jedes der ``Geräte`` hat für jede ``KeyGroup`` einen ``SSH-Key``
 * Jeder dieser ``KeyGroups`` hat ein oder mehere ``SSH-Keys``


Publish Group
=============
- Ein Nutzer hat ein oder mehrere ``Publish-Groups``
- Jeder dieser ``Publish Groups`` hat ein oder mehrere 'Publish Targets'

Wenn Server Targets:

- Ein Server hat mehrere ``ServerUser``
- Ein ``Account.SSH-Key`` ist einem oder mehreren ``ServerUsern`` zugewießen

Linking
=======
Jedem Nutzer kann berechtigung ``:Nutzung:`` auf eine Spezifische ``Publish-Group`` gegeben
Die ``Publish Group`` wird von einem Nutzer mit der berechtigung ``:Konfigurieren:`` eingestellt.
d.h. dieser kann Publish-Targets Hinzufügen

Wenn der Nutzer Berechtigung auf eine PublishGroup mit einem OAuth2-Target bekommt:
Wird der nutzer aufgefordert seinen PlatformAccount mit der Publish-Group zu verknüpfen


Publish Targets
---------------
* OAuth2 Platforms like
 * Gitlab
 * Github
* Server - Targets