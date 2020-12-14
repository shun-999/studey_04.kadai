### 商品クラス
import pandas as pd
import datetime

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
        self.item_number = []
        self.item_master=item_master
    
    def add_item_order(self,item_code, item_number):
        #self.item_order_list.append(item_code)
        for i in self.item_master:
            if item_code == i.item_code:
                self.item_order_list.append(item_code)
                self.item_order_name.append(i.item_name)
                self.item_order_price.append(i.price)
                self.item_number.append(item_number)

    def payment(self, payment):
        self.deposit = payment

       
    def view_item_list(self):
        sum_price = 0
        sum_num = 0
        for item,name,price,num  in zip(self.item_order_list, self.item_order_name, self.item_order_price, self.item_number):
            print("商品コード:{},商品名:{},価格:{}".format(item,name,price))
            print("注文：{},{}個".format(name,num))
            self.txt_out("商品コード:{},商品名:{},価格:{}".format(item,name,price))
            self.txt_out("注文：{},{}個".format(name,num))
            sum_price += price*num
            sum_num += num
        print("合計金額:{},合計個数:{}".format(sum_price,sum_num))
        print("お預かり金:{},お釣り:{}".format(int(self.deposit),int(self.deposit)-sum_price))
        self.txt_out("合計金額:{},合計個数:{}".format(sum_price,sum_num))
        self.txt_out("お預かり金:{},お釣り:{}".format(int(self.deposit),int(self.deposit)-sum_price))
    
    def txt_out(self, content):
        dt_now = datetime.datetime.today()
        dt_time = dt_now.strftime("%Y.%m.%d_%H.%M.%S")
        text_name = "./{}.txt".format(dt_time)
        with open(text_name, mode="a", encoding="utf-8")as f:
            f.write(content + "\n")


  
def master_recog(file):
    item_master=[]
    df = pd.read_csv(file)
    for item,name,price in zip(list(df["商品コード"]),list(df["商品名"]),list(df["価格"])):
        item_master.append(Item(str(item),name,price))
    return item_master

def order_buy():
    item_list = []
    sum_number = []
    while True:
        x = input("商品コードを入力してください>>")
        y = input("個数を入力してください>>")
        if x == "":
            break
        else:
            item_list.append(x)
            sum_number.append(y)
    return item_list, sum_number


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
    item_list, sum_number= order_buy()
    for item_code,item_number in zip(item_list,sum_number):
        order.add_item_order(item_code, int(item_number))
    
    pay_out = input("お金を入れてください>>")
    order.payment(pay_out)

    # オーダー表示
    order.view_item_list()

    
if __name__ == "__main__":
    main()