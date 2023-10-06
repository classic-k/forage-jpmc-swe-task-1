import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for i in range(len(quotes)):

        p =( quotes[i]['top_ask']['price'] + quotes[i]['top_bid']['price']) / 2 
       
        self.assertEqual(getDataPoint(quotes[i]), (quotes[i]['stock'], quotes[i]['top_bid']['price'], quotes[i]['top_ask']['price'], p))
  
    """ ------------ Add the assertion below ------------ """

 
  def test_getRatio_realPrice(self):
    prices = [
      [112.1,109.5],  [204.5,221.0]
    ]
    
    

    for i in range(len(prices)):
        price = prices[i]
        r = price[0] / price[1]
       
        self.assertEqual(getRatio(price[0], price[1]), r)

  def test_getRatio_priceBZero(self):
    price= [
     204.5,0
    ]
    
    self.assertEqual(getRatio(price[0], price[1]), None)

  def test_getRatio_priceAZero(self):
    price= [0, 12.3]
    
    
    self.assertEqual(getRatio(price[0], price[1]), None)
  
    """ ------------ Add the assertion below ------------ """



if __name__ == '__main__':
    unittest.main()
