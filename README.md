This is threat monitoring solution.

1. install pyshark .
You can use : pip install pyshark 

2.Interface Selection: Ensure you replace 'your_network_interface' in start_network_capture() with the actual name of your network interface. 
You can find the interface name by running pyshark.tshark.tshark.get_tshark_interfaces().

3.Running threat_hash.py to capture live packets requires administrative privileges.

4. Run the test_hash.py with administrative privileges.
