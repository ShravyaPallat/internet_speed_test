import speedtest

# Initialize the Speedtest object
test = speedtest.Speedtest()

# Notify the user that the server list is being loaded
print("Loading server list...")
# Retrieve the list of available servers
test.get_servers()

# Notify the user that the best server is being selected
print("Choosing best server...")
# Select the best server based on ping response
best = test.get_best_server()
# Print the details of the chosen server
print(f"Found: {best['host']} located in {best['country']}")

# Notify the user that the download speed test is starting
print("Performing download test...")
# Perform the download speed test and store the result in bytes per second
download_result = test.download()

# Notify the user that the upload speed test is starting
print("Performing upload test...")
# Perform the upload speed test and store the result in bytes per second
upload_result = test.upload()

# Retrieve the ping result in milliseconds
ping_result = test.results.ping

# Convert the download speed from bytes per second to megabits per second (Mbps)
# and print the result
print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbps")

# Convert the upload speed from bytes per second to megabits per second (Mbps)
# and print the result
print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbps")

# Print the ping result in milliseconds (ms)
print(f"Ping: {ping_result:.2f} ms")
