#!/bin/bash 

function forceIDLE {
  # Unplug battery to power/charging 
  adb shell dumpsys battery unplug

  # Force Idle 
  adb shell dumpsys deviceidle force-idle
  adb shell am set-inactive $APP true

  # Force Standby buckets 
  adb shell am set-standby-bucket $APP rare  
}

function checkIDLE {
  adb shell am get-inactive $APP
  adb shell am get-standby-bucket $APP
}
