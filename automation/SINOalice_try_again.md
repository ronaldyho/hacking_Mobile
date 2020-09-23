# Simply

Here is the output from `adb shell getevent -l`, when we touch a button in the game 

```
/dev/input/event4: EV_ABS       ABS_MT_TRACKING_ID   00002710
/dev/input/event4: EV_KEY       BTN_TOOL_FINGER      DOWN
/dev/input/event4: EV_ABS       ABS_MT_POSITION_X    000000ba
/dev/input/event4: EV_ABS       ABS_MT_POSITION_Y    0000070a
/dev/input/event4: EV_ABS       ABS_MT_TOUCH_MINOR   00000003
/dev/input/event4: EV_SYN       SYN_REPORT           00000000
/dev/input/event4: EV_ABS       ABS_MT_TOUCH_MINOR   00000004
/dev/input/event4: EV_SYN       SYN_REPORT           00000000
/dev/input/event4: EV_ABS       ABS_MT_TOUCH_MINOR   00000003
/dev/input/event4: EV_SYN       SYN_REPORT           00000000
/dev/input/event4: EV_ABS       ABS_MT_TOUCH_MINOR   00000004
/dev/input/event4: EV_SYN       SYN_REPORT           00000000
/dev/input/event4: EV_ABS       ABS_MT_TOUCH_MINOR   00000003
/dev/input/event4: EV_SYN       SYN_REPORT           00000000
/dev/input/event4: EV_ABS       ABS_MT_TRACKING_ID   ffffffff
/dev/input/event4: EV_KEY       BTN_TOOL_FINGER      UP
/dev/input/event4: EV_SYN       SYN_REPORT           00000000
```

Converting HEX to decimal ...     
ABS_MT_POSITION_X = 000000ba = 186    
ABS_MT_POSITION_Y = 0000070a = 1802     


The `adb` command to execute for this instance will be this:

`adb shell input touchscreen swipe 186 1802 186 1802 2`    
... *( Pos X, Pos Y, to Pos X, to Pox Y, for this long )*

