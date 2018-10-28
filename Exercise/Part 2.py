inventory_quantity = {'HP': 20,
                  'DELL': 50,
                  'MACBOOK': 12,
                  'ASUS': 30}

print('Yêu cầu 5:')
print(inventory_quantity)


print('Yêu cầu 6:')
print(' Number of Macbook in Inventory: {}'.format(inventory_quantity['MACBOOK']))


inventory_quantity['TOSHIBA'] = 10
print('Yêu cầu 7:')
print(inventory_quantity)


inventory_price = {'HP': 600,
                   'DELL': 650,
                   'MACBOOK': 12000,
                   'ASUS': 400,
                   'ACER': 350,
                   'TOSHIBA': 600,
                   'FUJITSU': 900,
                   'ALIENWARE': 1000}
print('Yêu cầu 8')
print(inventory_price)



order = {'brand': 'ASUS',
         'quantity': 5}
order_quantity = min(inventory_quantity[order['brand']], order['quantity'])
order_total_value = inventory_price[order['brand']] * order_quantity
print('Yêu cầu 9:')
print("Order : {0} {1}. Total order's value: {2} $".format(order_quantity, order['brand'],order_total_value))
