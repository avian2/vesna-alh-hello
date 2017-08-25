import vesna.alh
import serial
import logging

def main():
	logging.basicConfig(level=logging.INFO)

	f = serial.Serial("/dev/ttyUSB0", 115200, timeout=10)
	node = vesna.alh.ALHTerminal(f)

	print "Making GET request"
	resp = node.get("hello", "arg1=value1")
	print "Response:", resp

	print "Making POST request"
	resp = node.post("hello", "example post data", "arg2=value2")
	print "Response:", resp

if __name__ == "__main__":
	main()
