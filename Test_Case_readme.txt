Threat monitoring solution are usually build in order to continously monitor process dedicated to network or for endpoints.

The Test cases have been written in considertaion of the Blackbox and whitebox  testing.
----------------------------------------------------------------------------------------
Test Case 1: Test script running as admin:-
Verify is the threat monitor is run using the highest privledges in order to avoid any authention breach from a impersonificated user.
--------------------------------------------------
Test Case 2: Test  to handle new process entry:-
Verifing the correct capture of process executions after simulating process execution and check if it is captured.
--------------------------------------------------
Test Case 3: Test to handle duplicate processes after 60 seconds:-
Ensure the caching mechanism stores hashes for 60 seconds
Check that hashes are stored and verified for 60 seconds
--------------------------------------------------
Test Case 4: Test to handle duplicate processes within 60 seconds:-
Ensuring the caching mechanism stores hashes within 60 seconds for each process 
Confirm redundant data is discarded after 60 seconds
Ensure duplicate processes within 60 seconds are counted but not stored again.
--------------------------------------------------
Test Case 5: Test the overall reliability and accuracy
Simulate multiple processes and network traffic to validate accuracy and reliability.
--------------------------------------------------
Test Case 6: Test to handle the long path of the executable.
Ensuring that long path of the process executable are being processed and accepted by the monitoring solution.
--------------------------------------------------
Test Case 7: Test to handle that the solution is cross -platform but runs on Windows for now.
--------------------------------------------------
Test Case 8 : Test to handle when the path executable has soft links created.
--------------------------------------------------
Test Case 9 : Test to handle when the path executable has hard links created.
--------------------------------------------------
