# prevent Syncthing to create a default share folder
STNODEFAULTFOLDER=true
export STNODEFAULTFOLDER

# create profile/ID for a UNO user
unoID=$(./syncthing  -generate="unoConfig")
echo $unoID | awk '{print $5}' >unoID
echo "Created UNO user profile/ID:"
echo $unoID | awk '{print $5}'
echo 

# create profile/ID for a DUO user
duoID=$(./syncthing  -generate="duoConfig")
echo $duoID | awk '{print $5}' >duoID
echo "Created DUO user profile/ID:"
echo $duoID | awk '{print $5}'
echo 

# rename config.xmls to original.config
mv unoConfig/config.xml  unoConfig/original.config
mv duoConfig/config.xml  duoConfig/original.config
