

Getting Started, by 

https://stackoverflow.com/questions/3437686/how-to-use-adb-to-send-touch-events-to-device-using-sendevent-command#5392547
```
uiautomator events
adb shell getevent -l
```

```
adb shell input tap 757 1694
```

# References 

* ADB Shell - GetEvent | http://adbcommand.com/articles/adb%20shell%EF%BC%9Agetevent%20and%20sendevent
* Android Source : Touch  | https://source.android.com/devices/input/touch-devices.html 
* Android Source : GetEvent | http://source.android.com/devices/input/getevent.html



# Pre-requisites 

ADB wireless
```
$ adb devices
List of devices attached
60cce206	device

$ adb tcpip 5555
restarting in TCP mode port: 5555

$ adb connect 192.168.1.205:5555
connected to 192.168.1.205:5555
```
