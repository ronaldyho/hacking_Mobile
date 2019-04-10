# Quick Summary 

The default android keyboard that comes with most Android phones are vulnerable to keyloggers and sniffing techniques. For the purpose of this research, we will look into following (most prefered about): 
- Key Sniffing / Logging techniques
  -- https://www.pentestpartners.com/security-blog/key-sniffing-with-android/
- Keylogger tools 
- Keyboards which are actually exploit-kits
- Radare2 or other memory analysis toolkits which can retrieve keyboard's input data 
  - I found the following forensics tool that can capture memory dump ([GIT](https://github.com/MobileForensicsResearch/mem))



# The Dark Arts 

## Dark Art 1: *Apps with Accessibility Permissions*

Accessibility permissions allow the App the to record/simulate touches and key-presses. 

A hypothetical attack scenario can go like this:
- The malicious app can record our Apps' login password. After that it can record all the screen taps and characters typed by the end-user. 
  -- Then, at a time when the actual (human) user is not using the app (e.g. sleeping), it can put the device offline (airplane mode). After that, launch the App, sign in via the captured Username & Password, and performs more screen captures of all the conversations in the screens ... 

Sample:
- Accessibility Hack Demo by some random guy | https://github.com/bpr10/AccessibilityDemo

Reference: 
- Google is Threatening to Remove Apps with Accessibility Services from the Play Store, Mishaal Rahman (Nov 14, 2017), https://www.xda-developers.com/google-threatening-removal-accessibility-services-play-store/

## Dark Art 2: *Function Hooking*

*Function Hooking with Xposed*
- http://tiny.cc/bsidesroc-xposed

*Other References:*

- Basic Security Testing, OWASP (Oct 28, 2018), https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05b-Basic-Security_Testing.md
- Encryption and VPNs alone do not protect you from Pegasus/Trident, Lookout (Sep 2, 2016), https://blog.lookout.com/pegasus-trident-encryption-vpn-protection-detection 



## Dark Art 4: *Side-channel Attack & Other Linux Stuff*

I have added some stuff here with regards to this topic
https://github.com/ronaldyho/hacking_android/wiki/Keyloggers

And just random linux stuff at the moment
- IRQ /dev/interrupt (Requires kernel-level capabilities)
  -- See "Side channel attack", above
- EVENTS /dev/input/eventX (Requires possibly root permissions)
  -- http://manpages.ubuntu.com/manpages/trusty/man1/evtest.1.html
- AUTOMATOR uiautomator (Requires ADB permissions) 
  -- https://www.pentestpartners.com/security-blog/key-sniffing-with-android/



## Dark Art 5: *Capturing of Heap memory and grep strings*

I have successfully performed captured the heap memory of fleksy keyboard app after typing commands into a terminal app. 

- https://github.com/ronaldyho/hacking_android/wiki/Android-Memory-(-Heap---threads-) 
- As a high-level overview on this Proof-of-concept, here are the steps that I took :
   1. Execute and use keyboard application 
   1. Capture heap memory of keyboard process (PID needed) via some memory forensics tool ("mem") 
   1. Use the simple {{strings}} command and grep readable strings 
   1. Browse through the output 



## Dark Art Ultimate: *Remote Administration Tool (RAT)* 

An RAT makes use of a combination of exploits to control a victim's device. This is really a complicated tool that might have incorporated everything that we mentioned above (Hence: Ultimate).

*Reference:*

- Gain Complete control of any Android phone with the AhMyth RAT, (Nov 15, 2017), https://null-byte.wonderhowto.com/how-to/gain-complete-control-any-android-phone-with-ahmyth-rat-0180960/ 
- Pegasus Malware (RAT), https://sea.pcmag.com/news/29458/pegasus-spyware-targets-ios-android-devices-in-the-us 
