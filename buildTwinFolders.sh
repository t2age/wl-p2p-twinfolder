# remove auxiliar files
rm unoConfig/original.config
rm unoConfig/config.with-device
rm duoConfig/original.config

# make the build directory
mkdir  build

echo "creating  build/twin-UNO  folder..."
mkdir  build/twin-UNO
echo "creating  build/twin-DUO  folder..."
mkdir  build/twin-DUO
echo

echo "copying  'unoConfig/'  to 'build/twin-UNO/'"
cp -pr  unoConfig/  build/twin-UNO/
echo "copying  'duoConfig/'  to 'build/twin-DUO'"
cp -pr  duoConfig/  build/twin-DUO/
echo

echo "copying  runUno.sh  to build/twin-UNO"
cp  runUNO.sh  build/twin-UNO/
echo "copying  runDUO.sh  to build/twin-DUO"
cp  runDUO.sh  build/twin-DUO/
echo

echo "copying  'syncthing' binary  to build/twin-UNO/"
cp  syncthing   build/twin-UNO/
echo "copying  'syncthing' binary  to build/twin-DUO/"
cp  syncthing   build/twin-DUO/
echo 

echo "*********************************************************"
echo "*********************************************************"
echo "Inside the folder 'build/' you find the 2 twinfolders..."
echo
echo "REMEBER,"
echo "The twin-folders have the syncthing binary that works"
echo "on the current platform ONLY..."
echo "If you want to run any of the twins on different"
echo "platforms (PC x86, ARM64, ARM, etc),"
echo "you need to download the correct binary version"
echo "for each platform that you want to run!!!"
echo "*********************************************************"
echo "*********************************************************"
echo
