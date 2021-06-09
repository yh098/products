products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	products.append([name, price])
print(products)

# 7-9簡寫p = [name, price]
#7-10簡寫products.append([name, price])