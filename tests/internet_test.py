import speedtest

print("Initializing speedtest...")
s = speedtest.Speedtest()
print('speedtest initialized...')
server = s.get_best_server()
print('Using server: ', server)

for i in range(10):
    download = s.download(threads=1)
    print('Download speed: ', download)
    upload = s.upload(threads=1)
    print('Upload speed: ', upload)
