class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y

        return out

    def backward(self, dout):
        dx = dout * self.y # xとyをひっくり返す
        dy = dout * self.x

        return dx, dy



apple = 100
apple_num = 2
tax = 1.1

# layer
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

# 林檎の金額 x 個数
apple_price = mul_apple_layer.forward(apple, apple_num)

# 上記の合計 x 税金
price = mul_tax_layer.forward(apple_price, tax)

# backward

dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)



##################################################

class AddLayer:
    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y
        return out

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy

apple = 100
apple_num = 2
orange = 150
orange_num = 3
tax = 1.1

mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_fruits_layer = AddLayer()
mul_tax_layer = MulLayer()

# no.1
apple_price = mul_apple_layer.forward(apple, apple_num)
orange_price = mul_orange_layer.forward(orange, orange_num)
print(apple_price, orange_price, "#1")

# no.2
# 林檎とオレンジの合計
fruits_price = add_fruits_layer.forward(apple_price, orange_price)
print(fruits_price, "#2")

# no.3
# 税込金額
total_price = mul_tax_layer.forward(fruits_price, tax)
print(total_price, "#3")

##############################
# backward 

print("--backward--")

dtotal = 1

#1
dfruits, dtax = mul_tax_layer.backward(dtotal)

print(dfruits, dtax)

#2
dapple_price, dorange_price = add_fruits_layer.backward(dfruits)
print(dapple_price, dorange_price)


dapple, dapple_num = mul_apple_layer.backward(dapple_price)
dorange, dorange_num = mul_orange_layer.backward(dorange_price)

print(dapple, dapple_num, "apple")
print(dorange, dorange_num, "orange")












