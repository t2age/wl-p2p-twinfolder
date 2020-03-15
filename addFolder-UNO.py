unoIDFile = open("unoID", "r")
unoID = unoIDFile.readline().strip();
print "UNO ID: ", unoID

duoIDFile = open("duoID", "r")
duoID = duoIDFile.readline().strip();
print "DUO ID: ", duoID

print
print "Adding new shared folder to UNO profile..."
newCfgFile = open("unoConfig/config.xml", "w");
cfgFile = open("unoConfig/config.with-device", "r")

for line in cfgFile.readlines():
	newCfgFile.write(line)
	if (line.find("configuration version") > 0):
		# insert another DEVICE ID here
		newCfgFile.write('    <folder id="twinfolder" label="TwinFolder" path="./TwinFolder" type="sendreceive" rescanIntervalS="3600" fsWatcherEnabled="true" fsWatcherDelayS="10" ignorePerms="false" autoNormalize="true">' + "\n")
		newCfgFile.write("        <filesystemType>basic</filesystemType>" + "\n")
		
		# following 2 lines are for uno and for duo 
		newCfgFile.write('        <device id="'  + duoID + "\"" )
		newCfgFile.write(' introducedBy=""></device>' + "\n")
		newCfgFile.write('        <device id="'  + unoID + "\"" )
		newCfgFile.write(' introducedBy=""></device>' + "\n")
		
		newCfgFile.write('        <minDiskFree unit="%">1</minDiskFree>' + "\n")
		newCfgFile.write("        <versioning></versioning>" + "\n")
		newCfgFile.write("        <copiers>0</copiers>" + "\n")
		newCfgFile.write("        <pullerMaxPendingKiB>0</pullerMaxPendingKiB>" + "\n")
		newCfgFile.write("        <hashers>0</hashers>" + "\n")
		newCfgFile.write("        <order>random</order>" + "\n")
		newCfgFile.write("        <ignoreDelete>false</ignoreDelete>" + "\n")
		newCfgFile.write("        <scanProgressIntervalS>0</scanProgressIntervalS>" + "\n")
		newCfgFile.write("        <pullerPauseS>0</pullerPauseS>" + "\n")
		newCfgFile.write("        <maxConflicts>-1</maxConflicts>" + "\n")
		newCfgFile.write("        <disableSparseFiles>false</disableSparseFiles>" + "\n")
		newCfgFile.write("        <disableTempIndexes>false</disableTempIndexes>" + "\n")
		newCfgFile.write("        <paused>false</paused>" + "\n")
		newCfgFile.write("        <weakHashThresholdPct>25</weakHashThresholdPct>" + "\n")
		newCfgFile.write("        <markerName>.stfolder</markerName>" + "\n")
		newCfgFile.write("        <copyOwnershipFromParent>false</copyOwnershipFromParent>" + "\n")
		newCfgFile.write("        <modTimeWindowS>0</modTimeWindowS>" + "\n")
		newCfgFile.write("    </folder>" + "\n")
		
cfgFile.close()

newCfgFile.close()

print
