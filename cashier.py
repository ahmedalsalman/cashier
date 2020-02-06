def main():
	listOfItems = []
	dict = {"name":"", "price":"", "quantity":""}
	total = 0
	while dict["name"] != "done":
		dict = {"name":"", "price":"", "quantity":""}
		dict["name"] = input('Item (enter "done" when finished): ')
		if dict["name"] == "done":
			break
		dict["price"] = float(input("Price: "))
		dict["quantity"] = int(input("Quantity: "))
		total += (float(dict["price"]) * dict["quantity"])
		listOfItems.append(dict)

	print("""-------------------
receipt
-------------------""")
	for item in listOfItems:
		print(f'{item["quantity"]} {item["name"]} {float(item["price"]) * int(item["quantity"])}JD')

	print("-------------------")
	print(f"Total Price: {total}JD")



if __name__ == '__main__':
	main()
