from worker import Worker
from manager import Manager


ceo = Manager("John", 30000)

head_sales = Manager("Robert", 20000)
sales_executive1 = Worker("Richard", 10000)
sales_executive2 = Worker("Rob", 10000)

head_sales.add(sales_executive1)
head_sales.add(sales_executive2)

head_marketing = Manager("Michel", 20000)
marketing_executive1 = Worker("Michel", 10000)
marketing_executive2 = Worker("Linda", 10000)

head_marketing.add(marketing_executive1)
head_marketing.add(marketing_executive2)

ceo.add(head_sales)
ceo.add(head_marketing)

print(ceo.display(2))