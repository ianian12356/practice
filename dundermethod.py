class product:
	def __int__(Self, name, price):
		self.name = name
		self.price = price

	 def __str__(self): # __str__ 為python內建method來決定print出來的東西要是甚麼
	 	# return self.name + ' $'+ str(self.price)
	 	return f'{self.name} ${self.price}'  # f 寫法為直接把雙括號裡的資訊直接是為全string，不用像上面那樣還要用str轉為字串才能相加

	 def __repr__(self): # __repr__為python內建method來決定詳細class的資訊要是甚麼 
	 	return f'<product({self.name},{self.price}>'

	 def __add__(sef, other): # 加法的dunder method
	 	if isinstance(other, str):  #isinstance為確認物件是否為我們指定的資料型態function
	 		return self.name += other
	 	if isinstance(other, product):
	 		return [self, other] 

	 def __mul__(self, other): # 乘法的dunder method
	 	res = []
	 	if isinstance(other, int):
	 		for _ in reange(other):
	 			return res.append(self)


p = product('珍珠奶茶', 60)
print(p) # 會讀取__str__ return出來的資訊
print(repr(p)) # 會讀取__repr__ return出來的資訊

