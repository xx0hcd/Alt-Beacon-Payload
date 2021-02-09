# Alt-Beacon-Payload

Beacon payload using AV bypass method from https://github.com/fullmetalcache/CsharpMMNiceness and shellcode generated from https://github.com/RCStep/CSSG.

Clone this and save shellcode output file in the same directory (output filename is hard coded in the python script).

1. Load the awesome shellcode generator into your beacon console (https://github.com/RCStep/CSSG).
  - use the C# format with leading zeros 0x90,0x90.
  - save as 'tmpshell.txt' in the same directory.
  
2. Run the alt_beacon.py script.
  - Probably want to change the function/variables in the 'niceness_template.cs' file (assumed to be in the same directory). If you change '$$$LENGTH$$$' and '$$$NICENESS$$$' in the template file then you will also have to change where it is looking for that in the python script (lines 41,42 and 44).
  
3. Outputs final.cs.
  - compile it or something.
  - C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe /unsafe /platform:x64 /out:C:\Windows\Temp\final.exe C:\Windows\Temp\final.cs
  
4. Better automation/aggressor script?
  - ...
