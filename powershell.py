import subprocess

def win32_perf_raw_data_tcpip_icmp():
    command = "Get-CimInstance -className Win32_PerfRawData_Tcpip_ICMP | ConvertTo-Json"
    ping_stats =  subprocess.run(["powershell", "-Command", command], capture_output= True, text=True)
    return ping_stats.stdout

def write_to_file(filename, output):
    with open(filename, 'w') as f:
        f.write(str(output))

output=  win32_perf_raw_data_tcpip_icmp()

write_to_file("ping_stats.txt", output)

