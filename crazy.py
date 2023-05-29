from pythonping import ping

def send_ing(ip_address, count):

    try:

        response = ping(ip_address, count=count)

        if response.success():

            print(f"Successfully sent {count} pings to {ip_address}")

        else:

            print(f"No response from {ip_address}")

    except Exception as e:

        print(f"Failed to send pings to {ip_address} ({str(e)})")

ip_address = '159.224.216.59'

send_ping(ip_address, count=2000)
