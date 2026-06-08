print("DDoS Simulation and Mitigation Tool")
print()

max_requests = 10
request_count = 0

for i in range(1, 51):
    request_count = request_count + 1
    print("Request received:", request_count)

    if request_count > max_requests:
        print("System overload detected")
        print("Mitigation applied: Rate limiting activated")
        break

print()
print("Simulation finished")
print("In real systems, firewalls, load balancers, and rate limiting are used to prevent DDoS attacks")