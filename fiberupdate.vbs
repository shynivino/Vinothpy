nooftimes=InputBox("Enter No of Rows to be Updated:")
flagset=1	
Delay=175																					
do
	if nooftimes > 0 then																																																																																																																																																																																																																																																																																																														
		if flagset > 1 then
			WScript.Sleep Delay
			WScript.Sleep Delay			
			set oShell = CreateObject("Wscript.Shell")			
			bResult = oShell.AppActivate("Find Fiber Term Panel")
			WScript.Sleep Delay
			if bResult = True Then
				oShell.SendKeys "{DOWN}"
				WScript.Sleep Delay
				WScript.Sleep Delay
				WScript.Sleep Delay
				
			end if
		end if	
		set oShell = CreateObject("Wscript.Shell")
		Do
		  bResult = oShell.AppActivate("Find Fiber Term Panel")
		  If bResult = True Then
			 oShell.SendKeys "%E" 'Alt+E
			 WScript.Sleep Delay
			 oShell.SendKeys "E" 'E
			 WScript.Sleep Delay
			 WScript.Sleep Delay
			 Exit Do
		  End If
		  WScript.Sleep Delay
		Loop

		Do
			bResult = oShell.AppActivate("Fiber Term Panel Modification")
			If bResult = True Then

				 '---------- Move to the Equipment Constructed Status field
				 oShell.SendKeys "{TAB}" 'Tab keystroke
				 WScript.Sleep Delay
				 oShell.SendKeys "{TAB}" 'Tab keystroke
				 WScript.Sleep Delay
				 oShell.SendKeys "{TAB}" 'Tab keystroke
				 WScript.Sleep Delay
				 oShell.SendKeys "{TAB}" 'Tab keystroke
				 WScript.Sleep Delay
				 oShell.SendKeys "{TAB}" 'Tab keystroke
				 WScript.Sleep Delay
				 oShell.SendKeys "{TAB}" 'Tab keystroke
				 WScript.Sleep Delay
				 oShell.SendKeys "{TAB}" 'Tab keystroke
				 WScript.Sleep Delay

				 '---------- Select the first entry in the pop down (Constructed)
				 oShell.SendKeys "C" ' Send "C" keystroke
				 WScript.Sleep Delay

				 '---------- Move to the Plant Owner field
				 oShell.SendKeys "{TAB}" 'Tab keystroke
				 WScript.Sleep Delay
				 oShell.SendKeys "{TAB}" 'Tab keystroke
				 WScript.Sleep Delay

				 '---------- Type NBN
				 oShell.SendKeys "NB" ' Send "NB" keystroke
				 WScript.Sleep Delay

				 '---------- Move to the Dialog box where object status is
				 oShell.SendKeys "{TAB}" 'Tab keystroke
				 WScript.Sleep Delay
				 oShell.SendKeys "{TAB}" 'Tab keystroke
				 WScript.Sleep Delay
				 oShell.SendKeys "{TAB}" 'Tab keystroke
				 WScript.Sleep Delay
				 oShell.SendKeys "{TAB}" 'Tab keystroke
				 WScript.Sleep Delay
				 oShell.SendKeys "{TAB}" 'Tab keystroke
				 WScript.Sleep Delay
				 WScript.Sleep Delay
				 '---------- Move to the Object status field
				 oShell.SendKeys "O" 'Send "O" keystroke to move to Object status field
				 WScript.Sleep Delay
				 WScript.Sleep Delay
				 oShell.SendKeys "{ENTER}" 'Send "ENTER" keystroke edit the field
				 WScript.Sleep Delay
				 WScript.Sleep Delay
				 oShell.SendKeys "C" 'Send "C" keystroke to select CONSTRUCTED
				 WScript.Sleep Delay
				 WScript.Sleep Delay

				 '---------- Move to the Apply Button
				 oShell.SendKeys "%A" 'Alt+A to Apply changes
				 WScript.Sleep Delay
				 WScript.Sleep Delay
				 WScript.Sleep Delay
				 oShell.SendKeys "%C" 'Alt+C to Close window
				 WScript.Sleep Delay
				 WScript.Sleep Delay
				 Exit Do
			End If
		Loop

		WScript.Sleep Delay
		WScript.Sleep Delay
		WScript.Sleep Delay
		WScript.Sleep Delay
	else
		exit do		  
	end if
	nooftimes = nooftimes - 1
	flagset = flagset + 1
loop
WScript.Sleep Delay
WScript.Sleep Delay
WScript.Sleep Delay

Do
  bResult = oShell.AppActivate("Find Fiber Term Panel")
  WScript.Sleep Delay
  WScript.Sleep Delay
  If bResult = True Then
     oShell.SendKeys "%Q" 'Alt+Q to refresh query
     Exit Do
  End If
  WScript.Sleep Delay
Loop
WScript.Sleep Delay
WScript.Sleep Delay
WScript.Echo "Completed" 
