import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
	try:
		pattern = '\"https?\:\/\/w?w?w?\.?youtube\.com\/embed\/([\w\d]+)'
		link = re.findall(pattern , s)[0]
		return(f"https://youtu.be/{link}")
	except:
		return


if __name__ == "__main__":
    main()
