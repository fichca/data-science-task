from task_4.my_linked_list import MyLinkedList

my_list = MyLinkedList()
my_list.unshift(111)
my_list.push(222)
my_list.push(333)
my_list.push(444)
my_list.unshift(555)
my_list.push(666)
my_list.pop()
my_list.shift()
my_list.shift()

# expected: 222 333 444
print(my_list)
