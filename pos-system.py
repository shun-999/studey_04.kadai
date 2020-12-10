### 商品クラス
import pandas as pd
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price


### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_order_name=[]
        self.item_order_price=[]
        self.item_master=item_master
    
    def add_item_order(self,item_code):
        #self.item_order_list.append(item_code)
        for i in self.item_master:
            if item_code == i.item_code:
                self.item_order_list.append(item_code)
                self.item_order_name.append(i.item_name)
                self.item_order_price.append(i.price)

       
    def view_item_list(self):
        for item,name,price  in zip(self.item_order_list, self.item_order_name, self.item_order_price):
            print("商品コード:{},商品名:{},価格:{}".format(item,name,price))
  
def master_recog(file):
    item_master=[]
    df = pd.read_csv(file)
    for item,name,price in zip(list(df["商品コード"]),list(df["商品名"]),list(df["価格"])):
        item_master.append(Item(str(item),name,price))
    return item_master



### メイン処理
def main():
    # マスタ登録
    item_master = master_recog("./master.csv")
    #item_master = []
    #item_master.append(Item("001","りんご",100))
    #item_master.append(Item("002","なし",120))
    #item_master.append(Item("003","みかん",150))


    # オーダー登録
    order = Order(item_master)
    #order.add_item_order("001")
    #order.add_item_order("002")
    #order.add_item_order("003")
    order.add_item_order(input("商品コードを入力してください >>"))
    
    # オーダー表示
    order.view_item_list()
    


    
if __name__ == "__main__":
    main()