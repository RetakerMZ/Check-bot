# Load Balancer Simulation

This is a Python script that simulates a Load Balancer distributing HTTP traffic across 3 backend servers using a 'Least Connections' algorithm.

## Features

- **Server Capacity Limit:** Each simulated server has a maximum capacity (concurrent connections).
- **Concurrent Traffic Simulation:** Spawns 50 concurrent requests with varying, random processing times using Python threads.
- **Least Connections Algorithm:** The Load Balancer routes incoming requests dynamically to the server with the fewest active connections.
- **Logging & Alerting:** The script logs the traffic flow in real-time. If any server approaches its maximum capacity (>= 80% load), it logs a warning alert.

## Prerequisites

- Python 3.x (Built-in standard libraries are used, so no additional dependencies are required).

## Usage

To run the simulation, simply execute the script via your terminal:

```bash
python3 load_balancer.py
```

### Sample Output

```
...
2026-10-08 05:16:29,220 [INFO] Request 32 routed to Server-3. Connections: 4/5 (80.0%)
2026-10-08 05:16:29,221 [WARNING] ALERT: Server-3 is approaching capacity! Current load: 80.0%
2026-10-08 05:16:29,242 [INFO] Request 20 completed on Server-3. Connections: 3/5
2026-10-08 05:16:29,256 [INFO] Request 33 routed to Server-3. Connections: 4/5 (80.0%)
2026-10-08 05:16:29,256 [WARNING] ALERT: Server-3 is approaching capacity! Current load: 80.0%
2026-10-08 05:16:29,301 [INFO] Request 34 routed to Server-1. Connections: 5/5 (100.0%)
2026-10-08 05:16:29,301 [WARNING] ALERT: Server-1 is approaching capacity! Current load: 100.0%
...
```

Watch as the Load Balancer distributes the load and emits warnings when the server loads spike.
