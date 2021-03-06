#!/usr/bin/python2

DOMAIN = "formatstick"
PATH = "/usr/share/khrysro/locale"

import os, gettext, sys
sys.path.append('/usr/lib/khrysro/common')
import additionalfiles

os.environ['LANGUAGE'] = "en_US.UTF-8"
gettext.install(DOMAIN, PATH)

prefix = """[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Icon=usb-creator
Exec=formatstick -m iso
Categories=PyQt5;Utility;
NotShowIn=KDE;
"""

additionalfiles.generate(DOMAIN, PATH, "share/applications/formatstick.desktop", prefix, _("USB Image Writer"), _("Make a bootable USB stick"), "")

prefix = """[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Icon=system-run
Exec=formatstick -m iso
Categories=System;
OnlyShowIn=KDE;
"""

additionalfiles.generate(DOMAIN, PATH, "share/applications/formatstick-kde.desktop", prefix, _("USB Image Writer"), _("Make a bootable USB stick"), "", genericName=_("Make a bootable USB stick"))

prefix = """[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Icon=usb-creator
Exec=formatstick -m format
Categories=PyQt;Utility;
NotShowIn=KDE;
"""

additionalfiles.generate(DOMAIN, PATH, "share/applications/formatstick-format.desktop", prefix, _("USB Stick Formatter"), _("Format a USB stick"), "")

prefix = """[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Icon=system-run
Exec=formatstick -m format
Categories=System;
OnlyShowIn=KDE;
"""

additionalfiles.generate(DOMAIN, PATH, "share/applications/formatstick-format-kde.desktop", prefix, _("USB Stick Formatter"), _("Format a USB stick"), "", genericName=_("Format a USB stick"))

prefix="""[Nemo Action]
Active=true
Exec=formatstick -m iso -i "%F"
Icon-Name=edit-clear-all-symbolic
Selection=S
Extensions=iso;img;
"""
additionalfiles.generate(DOMAIN, PATH, "share/nemo/actions/formatstick.nemo_action", prefix, _("Make bootable USB stick"), _("Make a bootable USB stick"), "")

prefix="""[Nemo Action]
Active=true
Exec=formatstick -m format -u %D
Icon-Name=media-removable-symbolic
Selection=S
Extensions=any;
Conditions=removable;
"""
additionalfiles.generate(DOMAIN, PATH, "share/nemo/actions/formatstick-format.nemo_action", prefix, _("Format"), _("Format a USB stick"), "")
