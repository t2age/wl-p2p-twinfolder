# THIS DOC IS INTENDED FOR TUTORIAL PURPOSE,  
# SO, THE GOAL WAS TO DIVIDE INTO EASY STEPS...  
  
**[DOWNLOADS]**  
1.0.  
Download the Syncthing Binary Package from Syncthing website, for the platform that you are going to use to build (x86, ARM, etc...). Then, extract it...  
Example: if using a PC x86 to run the twinfolder, then download the Syncthing for PC x86, and so on...  
URLS:  
https://github.com/syncthing/syncthing/releases/tag/v1.3.4  
https://github.com/syncthing/syncthing/releases/latest  
  
1.1.  
Download the wl-p2p-twinfolder script from   
https://github.com/t2age/wl-p2p-twinfolder  
Then, extract it...  
  
1.2.   
Copy the binary file "syncthing", from the Syncthing Binary Package folder to the wl-p2p-twingen folder.  
  
  
**[RUN SCRIPTS]**  
2.0.   
Enter the folder wl-twin-folder with a terminal shell  
  
2.1. Run  
```
  ./createTwinConfigs.sh  
```
  
2.2. Run   
```
  python  addDevice-UNO.py  
```
  
2.3. Run  
```
  python  addDevice-DUO.py  
```
  
2.4. Run  
```
  python  addFolder-UNO.py  
```
  
2.5. Run  
```
  ./buildTwinFolders.sh  
```

  
**[PACK THE TWIN FOLDERS]**  
3.0. Run
```
  ./compressTwinFolders.sh  
```
The resulting files will be inside the "build/" folder...  
  
3.1.  
REMEMBER,  
both twin-UNO and twin-DUO have the syncthing binary file that can run  
on you current platform, the one that you are using now...  
IF YOU WANT TO RUN ANY OF THE TWINS ON DIFFERENT PLATFORMS, THEN,  
you need to download Syncthing Binary Pack for the platform   
that you want to run, from Syncthing website...  
For example, if you want to run one side on Raspberry and other on PC x86,  
you need to download both binaries versions and copy the syncthing file  
  
=== On PC x86 ===  
You need to have the file "syncthing" specific to run on PC x86 inside  
the twin-XXX folder...  
  
=== On RaspberryPI ===  
You need to have the file "syncthing" specific to run on RaspberryPI  
inside the twin-YYY folder...  
  
  
**[RUN THE TWINS]**  
4.0.  
Move the twin-XXX folders to the place where you want to run,  
extract then and run:  
  
```
  ./runUNO.sh		#to run the UNO side  
  ./runDUO.sh		#to run the DUO side  
```

4.1.  
On the UNO side, the shared folder is:  
twin-UNO/TwinFolder  
  
On the DUO side, the share folder is:  
USERHOMEFOLDER/TwinFolder  
(/home/user/TwinFolder)  
  
**[REBUILD/RESTART BUILDING PROCESS]**  
X.0.  
To repeat the building process:  
```
  ./cleanTwinConfigs.sh  
  ./cleanBuild.sh  
```
  
