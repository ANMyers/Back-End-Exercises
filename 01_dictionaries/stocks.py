stockDict = { 'GM': 'General Motors', 'CAT':'Caterpillar', 'EK':"Eastman Kodak", 'GE':"General Electric" }

purchases = [ ( 'GE', 100, '10-sep-2001', 48 ), ( 'CAT', 100, '1-apr-1999', 24 ), ( 'GE', 200, '1-jul-1998', 56 ) ]

overall_transactions = dict() # Store the total transactions with each company

def history_report():

	""" Creates a report of transactions

	Method Argument
	----------------
	n/a
	"""

	for each in purchases:
		tick_of_company = each[0]
		number_of_shares = each[1]
		date_of_purchase = each[2]
		price_of_shares = each[3]

		name_of_company = each[0]

		"""for k, v in stockDict.items():
									if tick_of_company is k:
										name_of_company = v"""

		name_of_company = stockDict[tick_of_company]

		total_cost = number_of_shares * price_of_shares

		# print("I purchased {0} stock for ${1}".format(name_of_company, total_cost))

		if each[0] in overall_transactions: # If the tick exists add to the total
			overall_transactions[each[0]] += total_cost
		else:								# If the tick doesn't exist create it
			overall_transactions[each[0]] = total_cost

	for ticker, total in overall_transactions.items():
		print("----------{}---------".format(ticker))
		print("Total Price of {} is ${}".format(ticker, total))
		print("\n\n")

history_report()






