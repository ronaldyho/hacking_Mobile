# TIP  
dz> `drozer console connect --debug`


# GetPackageFromUID 
Gets the UID of the running application 

```
dz> run app.package.getpackagefromuid 2000
UID 2000 is android.uid.shell:2000
```


# Intent 
An **Intent** is a defined object used for messaging that is created an communicated to an intended application component.  

Think of it as an intention to perform an action.  
An **Intent** is basically a message to say you did or want something to happen. 
Depending on the intent, apps or the OS might be listening for it and will react accordingly. 
Think of it as a blast email to a bunch of friends, in which you tell your friend John to do something,
or to friends who can do X ("intent filters"), to do X. 
The other folks will ignore the email, but John (or friends who can do X) will react to it.

