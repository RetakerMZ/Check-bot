import threading
import time
import random
import logging
from typing import List

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

class Server:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.current_connections = 0
        self.lock = threading.Lock()

    def handle_request(self, request_id: int):
        with self.lock:
            self.current_connections += 1
            load_percentage = (self.current_connections / self.capacity) * 100

            # Log traffic flow
            logging.info(f"Request {request_id} routed to {self.name}. Connections: {self.current_connections}/{self.capacity} ({load_percentage:.1f}%)")

            # Alert if approaching 100% CPU load
            if load_percentage >= 80.0:
                logging.warning(f"ALERT: {self.name} is approaching capacity! Current load: {load_percentage:.1f}%")

        # Simulate processing time
        processing_time = random.uniform(0.1, 0.5)
        time.sleep(processing_time)

        with self.lock:
            self.current_connections -= 1
            logging.info(f"Request {request_id} completed on {self.name}. Connections: {self.current_connections}/{self.capacity}")

class LoadBalancer:
    def __init__(self, servers: List[Server]):
        self.servers = servers
        self.lock = threading.Lock()

    def get_server(self) -> Server:
        with self.lock:
            # Implement 'Least Connections' algorithm
            best_server = None
            min_connections = float('inf')

            for server in self.servers:
                with server.lock:
                    if server.current_connections < min_connections:
                        min_connections = server.current_connections
                        best_server = server

            return best_server

def generate_requests(load_balancer: LoadBalancer, total_requests: int):
    threads = []

    def request_task(req_id: int):
        server = load_balancer.get_server()
        if server:
            # Check if server is at capacity before routing?
            # The prompt says 'alert if approaching 100%', let's allow it to hit 100% to show alerts.
            server.handle_request(req_id)
        else:
            logging.error(f"Request {req_id} dropped - no available servers.")

    for i in range(total_requests):
        t = threading.Thread(target=request_task, args=(i+1,))
        threads.append(t)
        t.start()
        # Adding a small delay to simulate arrival rate
        time.sleep(random.uniform(0.01, 0.05))

    for t in threads:
        t.join()

if __name__ == '__main__':
    # Define 3 backend servers with a capacity limit (e.g., 5 concurrent requests)
    server_capacity = 5
    servers = [
        Server("Server-1", capacity=server_capacity),
        Server("Server-2", capacity=server_capacity),
        Server("Server-3", capacity=server_capacity)
    ]

    lb = LoadBalancer(servers)

    logging.info("Starting Load Balancer Simulation...")
    generate_requests(lb, 50)
    logging.info("Simulation completed.")
