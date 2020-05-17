# Reverse engineer an Android app API

### Set up mitmproxy with an Android emulator

* Follow this tutorial to set up emulator and mitmproxy:
https://appiumpro.com/editions/63-capturing-android-emulator-network-traffic-with-appium

(Note: Make sure emulator image has "(Google API)" in the name, since you won't be able to install Play Store otherwise.)

### Install Play Store in the emulator

These steps were extracted from the following tutorial:
https://medium.com/@dai_shi/installing-google-play-services-on-an-android-studio-emulator-fffceb2c28a1

1. Make sure emulator image has (Google API) in the name, since you won't be able to install Play Store otherwise.
2. Download the apps for your image: https://opengapps.org/
3. Extract everything: 
```sh
unzip open_gapps-x86_64-6.0-pico-20170304.zip 'Core/*'
rm Core/setup*
lzip -d Core/*.lz
for f in $(ls Core/*.tar); do
  tar -x --strip-components 2 -f $f
done
```
4. Start emulator with `emulator -avd "emulator_name" -writable-system &`
5. Install extracted packages with:
```sh
adb remount
adb push etc /system
adb push framework /system
adb push app /system
adb push priv-app /system
```
6. Restart:
```sh
adb shell stop
adb shell start
```

### Finishing

1. Download the app and use it
2. `mitmproxy` starts intercepting requests. You can select one and:
    * Type 'w' to enter export mode
    * Enter 'export.clip curl @focus' to copy curl request to clipboard
    * (you can add an actual key binding so that you just need to press a key, like https://howdoitestthat.com/export-curl-from-mitm-proxy/ )
3. Paste on a terminal and run. You should see the same response as in `mitmproxy`

