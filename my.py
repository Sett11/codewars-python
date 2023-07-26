def get_product_id(s): 
    return s.split('-p-')[::-1][0].split('-')[0]

print(get_product_id('http://www.exampleshop.com/fancy-coffee-cup-p-90764-12052019.html'))
print(get_product_id('http://www.exampleshop.com/c-3-p-0-p-654-11112011.html'))