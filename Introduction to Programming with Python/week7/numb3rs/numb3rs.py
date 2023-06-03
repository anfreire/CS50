import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
	ip_modified = ip.strip()
	try:
		numbers = re.search(r"^(\d+).(\d+).(\d+).(\d+)$", ip_modified)
		if numbers:
			nmb1 = int(numbers.group(1))
			nmb2 = int(numbers.group(2))
			nmb3 = int(numbers.group(3))
			nmb4 = int(numbers.group(4))
		if ( nmb1 >= 0 and nmb1 <= 255 and
			nmb2 >= 0 and nmb2 <= 255 and
			nmb3 >= 0 and nmb3 <= 255 and
			nmb4 >= 0 and nmb4 <= 255):
			return True
		else:
			return False
	except (TypeError, re.error, UnboundLocalError) as error:
		return False



if __name__ == "__main__":
    main()
