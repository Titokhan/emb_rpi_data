import serial

ser=serial.Serial('/dev/ttyACM0', 115200)
s=[0]

fn=open("emb_data.csv","w+")
while True:
	read_serial=ser.readline()
	s[0]=str(ser.readline())
	print s[0]
	fn.write(s[0])
	print read_serial
	fn.write(read_serial)
fn.close()
