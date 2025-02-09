alert tcp any any -> any 80 (msg:"Potential HTTP Traffic"; sid:1000001; rev:1;)
alert icmp any any -> any any (msg:"ICMP Echo Request Detected"; sid:1000002; rev:1;)
