products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

# 7-9簡寫p = [name, price]
#7-10簡寫products.append([name, price])

for p in products:
	print(p[0], '的價格是', p[1])