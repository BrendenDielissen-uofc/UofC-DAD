import time, iio

ctx = iio.LocalContext()
ctrl = ctx.find_device('lps331ap')

channel_names = ['pressure', 'timestamp', 'temp']
for id in channel_names:
    chan = ctrl.find_channel(id)
    value = chan.attrs['raw'].value if 'raw' in chan.attrs.keys() else None
    print(chan.attrs)
    print("{0}: {1}".format( chan.id, value))
