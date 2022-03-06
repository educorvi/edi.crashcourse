# edi.crashcourse

Das Plone-Add-On bietet die Möglichkeit zur Veröffentlichung von Online-Kursen mit dem Content-Management-System Plone

## Features

- Ordnertyp Crashkurs
- Ordnertyp MeinKurs, die eine Speicherung von Tracking-Daten im persönlichen Ordner des Benutzers erlauben
- Portlet mit Kursinformationen
- Vorwärts- Rückwärts- Navigation
- Optional: Speicherung der Tracking-Daten für den Benutzer in MeinOrdner 


## Screenshot/Beispiel

![Crashkurs in Plone](images/Crashkurs.png "Crashkurs in Plone")

[Link text Here](http://kurse.uv-kooperation.de/)


## Installation

Die Installation von edi.crashkurs erfordert die Installation von edi.skillpill

Install edi.crashcourse by adding it to your buildout::

```
    [buildout]

    ...

    eggs +=
        edi.skillpill
        edi.crashcourse

    develop +=
        src/edi.skillpill
        src/edi.crashcourse

    [sources]
    edi.skillpill = git https://github.com/educorvi/edi.skillpill.git
    edi.crashcourse = git https://github.com/educorvi/edi.crashcourse.git

```

Danach Ausführung von: ``bin/buildout``


## Contribute

- Issue Tracker: https://github.com/educorvi/edi.crashcourse/issues
- Source Code: https://github.com/educorvi/edi.crashcourse


## Support

Lars Walther (info@educorvi.de)


## Lizenz

MIT License
