# host-blocker
---

Adds and/or removes rules in the Windows 'hosts' file in order to block/unblock a list of defined domains. Originally written to prevent impulse clicking on social media. Must be run as admin in order to read/write the 'hosts' file (resides within system32 folder).

## Usage

---

This can be run as a standalone script or it can be scheduled to be run so that any defined sites are blocked for a given time frame (e.g., run script at 9 AM at start of work hours and then again at 5 PM when you're done).

For ease of use, you can create a shortcut with the following target structure: 
```<C:path\to\python> <C:\path\to\this\script>```

As an example:
```
C:\Users\johnsmith\AppData\Local\Microsoft\WindowsApps\python.exe E:\Documents\host-blocker\host-blocker.py
```

After the shortcut is created you can view its 'Properties' and under the 'Shortcut' tab, click on 'Advanced' and check the box to run as administrator.
