# Security Guidelines

## Overview
This project is designed to simulate cybersecurity scenarios for research and educational purposes. Proper security practices are essential to protect the environment from misuse or unintended vulnerabilities.

## Best Practices
1. **Secure Configuration**
   - Use strong passwords for all system accounts.
   - Restrict container access to trusted users only.
   - Ensure Snort configuration files are read-only.

2. **Network Segmentation**
   - Isolate the environment from production networks when running simulations.
   - Use private networks in Docker containers.

3. **Data Privacy**
   - Avoid using sensitive or real user data in simulations.
   - Clear logs regularly to prevent data leakage.

4. **Updates**
   - Regularly update Snort rules and signatures.
   - Keep all dependencie
