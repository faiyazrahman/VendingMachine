import decimal
#input1 = item selection
#input2 = user amount input
#input3 = if insufficient funds - C or R

item1 = {
 "item1": "Sea Salt Chips",
 "price1": 2.50,
 "value1": "2.50",
 "code1": "A01"
}

item1_name = item1.get("item1")
item1_price = item1.get("price1")
item1_code = item1.get("code1")
item1_value1 = item1.get("value1")


#####################################
item2 = {
 "item2": "Dairy Milk Chocolate",
 "price2": 3.40,
 "value2": "3.40",
 "code2": "A02"
}

item2_name = item2.get("item2")
item2_price = item2.get("price2")
item2_code = item2.get("code2")
item2_value2 = item2.get("value2")
######################################
item3 = {
 "item3": "Cola Classic",
 "price3": 4.60,
 "value3": "4.60",
 "code3": "A03"
}

item3_name = item3.get("item3")
item3_price = item3.get("price3")
item3_code = item3.get("code3")
item3_value3 = item3.get("value3")
###################################
item4 = {
 "item4": "Grape Drink",
 "price4": 4.20,
 "value4": "4.20",
 "code4": "B01"
}

item4_name = item4.get("item4")
item4_price = item4.get("price4")
item4_code = item4.get("code4")
item4_value4 = item4.get("value4")
###################################
item5 = {
 "item5": "Cadbury - BOOST",
 "price5": 3.40,
 "value5": "3.40",
 "code5": "B03"
}

item5_name = item5.get("item5")
item5_price = item5.get("price5")
item5_code = item5.get("code5")
item5_value5 = item5.get("value5")
###################################
item6 = {
 "item6": "Gummy Bears",
 "price6": 5.60,
 "value6": "5.60",
 "code6": "C01"
}

item6_name = item6.get("item6")
item6_price = item6.get("price6")
item6_code = item6.get("code6")
item6_value6 = item6.get("value6")
#################################



print("########################################################################")
print("--------------------- S-N-A-C-K --- M-A-C-H-I-N-E ----------------------")
print("########################################################################")
print("------------------------- Please select an item ------------------------")
print("########################################################################")
print()
print("########################################################################")
print("----------------------------------- MENU -------------------------------")
print("########################################################################")
print("------------------------------------------------------------------------")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("{0:<10}{1:>30}{2:>22}".format("ITEM", "PRICE", "Item Code"))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("------------------------------------------------------------------------")
print("{0:^10}{1:>22}{2:>0}{3:>19}".format(item1_name, " $" , item1_value1, item1_code))
print("------------------------------------------------------------------------")
print("{0:^10}{1:>16}{2:>0}{3:>19}".format(item2_name, " $" , item2_value2, item2_code))
print("------------------------------------------------------------------------")
print("{0:^10}{1:>24}{2:>0}{3:>19}".format(item3_name, " $" , item3_value3, item3_code))
print("------------------------------------------------------------------------")
print("{0:^10}{1:>25}{2:>0}{3:>19}".format(item4_name, " $" , item4_value4, item4_code))
print("------------------------------------------------------------------------")
print("{0:^10}{1:>21}{2:>0}{3:>19}".format(item5_name, " $" , item5_value5, item5_code))
print("------------------------------------------------------------------------")
print("{0:^10}{1:>25}{2:>0}{3:>19}".format(item6_name, "  $" , item6_value6, item6_code))
print("------------------------------------------------------------------------")
print("########################################################################")
print()
print()


def select_item():

	main_input1 = input("Enter item code: ").upper()


	if (main_input1 == "A01"):
		selection = 1
		#selected_item()

	elif (main_input1 == "A02"):
		selection = 2
		#selected_item()

	elif (main_input1 == "A03"):
		selection = 3
		#selected_item()


	elif (main_input1 == "B01"):
		selection = 4
		#selected_item()


	elif (main_input1 == "B03"):
		selection = 5
		#selected_item()
	

	elif (main_input1 == "C01"):
		selection = 6
		#selected_item()

	else:
		print("ERROR - invalid code")
		select_item()


	input1 = main_input1
	if(input1 == "A01"):
		print("{0:^10}{1:>15}".format("Item selected: ", item1_name))
		print()
		print("{0:^10}{1:<0}{2:<0}".format("Please pay: ", "$", item1_value1))
		#price_check()

	elif(input1 == "A02"):
		print("{0:^10}{1:>15}".format("Item selected: ", item2_name))
		print()
		print("{0:^10}{1:<0}{2:<0}".format("Please pay: ", "$", item2_value2))
		#price_check()

	elif(input1 == "A03"):
		print("{0:^10}{1:>15}".format("Item selected: ", item3_name))
		print()
		print("{0:^10}{1:<0}{2:<0}".format("Please pay: ", "$", item3_value3))
		#price_check()

	elif(input1 == "B01"):
		print("{0:^10}{1:>15}".format("Item selected: ", item4_name))
		print()
		print("{0:^10}{1:<0}{2:<0}".format("Please pay: ", "$", item4_value4))
		#price_check()

	elif(input1 == "B03"):
		print("{0:^10}{1:>15}".format("Item selected: ", item5_name))
		print()
		print("{0:^10}{1:<0}{2:<0}".format("Please pay: ", "$", item5_value5))
		#price_check()

	elif(input1 == "C01"):
		print("{0:^10}{1:>15}".format("Item selected: ", item6_name))
		print()
		print("{0:^10}{1:<0}{2:<0}".format("Please pay: ", "$", item6_value6))
		#price_check()

	else:
		print("Please enter valid Code")


	print("--------------------------------------------")


	input2 = round(float(input("$")),2)
	print()
	print("--------------------------------------------")

	if(input2 == item1_price) and (selection == 1):
		print("Thank you!")

	elif(input2 == item2_price) and (selection == 2):
		print("Thank you!")

	elif(input2 == item3_price) and (selection == 3):
		print("Thank you!")

	elif(input2 == item4_price) and (selection == 4):
		print("Thank you!")

	elif(input2 == item5_price) and (selection == 5):
		print("Thank you!")

	elif(input2 == item6_price) and (selection == 6):
		print("Thank you!")

	elif(input2 > item1_price) and (selection == 1):
		print("{0:^10}{1:<11}0".format("Please take your change: $", round((input2 - item1_price), 3)))
		print()
		print("Thank you!")
		print("--------------------------------------------")

	elif(input2 > item2_price) and (selection == 2):
		print("{0:^10}{1:<11}".format("Please take your change: $", input2 - item2_price))
		print()
		print("Thank you!")
		print("--------------------------------------------")

	elif(input2 > item3_price) and (selection == 3):
		print("{0:^10}{1:<11}".format("Please take your change: $", input2 - item3_price))
		print()
		print("Thank you!")
		print("--------------------------------------------")

	elif(input2 > item4_price) and (selection == 4):
		print("{0:^10}{1:<11}".format("Please take your change: $", input2 - item4_price))
		print()
		print("Thank you!")
		print("--------------------------------------------")

	elif(input2 > item5_price) and (selection == 5):
		print("{0:^10}{1:<11}".format("Please take your change: $", input2 - item5_price))
		print()
		print("Thank you!")
		print("--------------------------------------------")

	elif(input2 > item6_price) and (selection == 6):
		print("{0:^10}{1:<11}".format("Please take your change: $", input2 - item6_price))
		print()
		print("Thank you!")
		print("--------------------------------------------")

	else: 
		print("----- Insufficent funds -----")
		print()
		print("Press C to continue or R for refund")
		print("--------------------------------------------")
		input3 = input()
		if(input3 == "R"):
			print()
			print("--------------------------------------------")
			print("{0:^10}{1:<11}".format("Refunded: $", input2))
			print()
			print("Thank you!")
			print("--------------------------------------------")

		elif(input3 != "C"):
			print("Invalid option")


select_item()
print()
