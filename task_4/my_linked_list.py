class MyLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.size = 0

    def push(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next = node
            node.previous = self.__tail
            self.__tail = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return
        else:
            self.__tail = self.__tail.previous
            self.__tail.next = None
            self.size -= 1

    def shift(self):
        if self.is_empty():
            return
        else:
            self.__head = self.__head.next
            self.__head.previous = None
            self.size -= 1

    def unshift(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            self.__tail = node
        else:
            self.__head.previous = node
            node.next = self.__head
            self.__head = node
        self.size += 1

    def is_empty(self) -> bool:
        return 0 == self.size

    def __str__(self) -> str:
        result: str = ""
        if self.is_empty():
            return result

        target: Node = self.__head
        while target is not None:
            result = result + str(target.element) + " "
            target = target.next

        return result


class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
        self.previous = None
