# snap7-read-and-write-PLC

For this project i used following softwares
- python 3.7 (64-bit)
- NetToPLCsim S7ov.1.2.4.0
- TIA portal 15.1
- PLCSIM 15.1


First of all you need to run nettoplc as Administrator. Then it ask to stop 's7oiehsx64' service.It is a 'SIMATIC S7DOS Help Service'. It is using Port 102. you have to stop that service.(When you run nettoplc as adminstrator, it can stop 's7oiehsx64' and get port 102 to nettoplc) 

For this project i used PLCSIM as plc. I made a programe  in TIA Portal 15.1 and download it to plc sim.(/images/ob.png)
I made a db(/images/db.png) for that project and i need to read db data and control it from python.

After PLCSIM running, connect it to localhost using nettoplc(/images/nettoplc.png).

In my python script, Read "door","bulb","count" and write data to "switch".
