unoIDFile = open("unoID", "r")
unoID = unoIDFile.readline().strip();
print "UNO ID: ", unoID

duoIDFile = open("duoID", "r")
duoID = duoIDFile.readline().strip();
print "DUO ID: ", duoID

print
print "Adding DUO device ID to UNO profile..."
newCfgFile = open("unoConfig/config.with-device", "w");
cfgFile = open("unoConfig/original.config", "r")

for line in cfgFile.readlines():
	if (line.find(unoID) > 0):
		# insert another DEVICE ID here
		newCfgFile.write( '    <device id="' + duoID + "\"" )
		newCfgFile.write( ' name="DUOdevice" compression="metadata" introducer="false" skipIntroductionRemovals="false" introducedBy="">' + "\n")
		newCfgFile.write( "        <address>dynamic</address>" + "\n")
		newCfgFile.write( "        <paused>false</paused>" + "\n")
		newCfgFile.write( "        <autoAcceptFolders>true</autoAcceptFolders>" + "\n")
		newCfgFile.write( "        <maxSendKbps>0</maxSendKbps>" + "\n")
		newCfgFile.write( "        <maxRecvKbps>0</maxRecvKbps>" + "\n")
		newCfgFile.write( "        <maxRequestKiB>0</maxRequestKiB>" + "\n")
		newCfgFile.write( "    </device>" + "\n")
	
		pass
	
	newCfgFile.write(line)
	pass
cfgFile.close()

newCfgFile.close()

print
