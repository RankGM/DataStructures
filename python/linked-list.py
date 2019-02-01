'''
	Todo:
		- def sort
		- Include exceptions
'''

class node:
	def __init__ (self, data=None):
		self.key = data
		self.next = None

class linkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	# O(1)
	def insertAtEnd(self, data):
		aux = node(data)
		
		# if first node
		if not self.head:
			self.head = aux
			self.tail = aux
			return

		# finds and inserts to tail
		crawler = self.tail
		crawler.next = aux
		self.tail = aux

	# O(1)
	def insertAtBeginning(self, data):
		aux = node(data)
		
		# if inserting the first element, update tail
		if not self.head:
			self.tail = aux
		aux.next = self.head
		self.head = aux


	# O(n)
	def insertAfter(self, target, data):
		aux = node(data)

		# If list is empty, return error
		if not self.head:
			print(f"List is empty, Cannot insert {data} Consider using insertAtEnd")
			return

		#Finds the target node
		crawler = self.head
		while crawler:
			if crawler.key == target:
				aux.next = crawler.next
				
				# If inserting as lasta element, update tail
				if not crawler.next:   
					self.tail = aux
				crawler.next = aux
				return

			crawler = crawler.next

		print(f"Target {target} not found in list. Cannot insert {data}")

	# O(n)
	def remove(self, data):

		# case: list empty
		if not self.head:
			print(f"List is empty, cannot remove {data}")
			return
		
		# case: remove first node
		crawler = self.head
		if crawler.key == data:
			self.head = crawler.next
			return

		# case: second to last
		while crawler: 
			if crawler.key == data:
				break
			previous = crawler
			crawler = crawler.next

		# case: loop ended by reaching None
		if not crawler:
			print(f"Cannot remove {data}. Value not found in list")
			return
		
		# case: loop ended because found value (break statement)
		previous.next = crawler.next



	# O(n)
	def printList(self):
		crawler = self.head
		
		if not crawler:
			print("List is empty. Cannot print")
			return

		# To print the arrows correctly
		if crawler:
			print(crawler.key, end=' ')
			crawler = crawler.next
		
		while crawler:
			print('->', end=' ')
			print(crawler.key, end=' ')
			crawler = crawler.next
		print()


# TESTER PROGRAM

list1 = linkedList()
list1.insertAtEnd(10)
list1.insertAtEnd(30)
list1.insertAtBeginning(0)
list1.insertAfter(10, 20)
print("List 1: ", end='')
list1.printList()


list2 = linkedList()
for i in range(1,10):
	list2.insertAtBeginning(i)
print("List 2: ", end='')
list2.printList()

list2.remove(5)
print("List 2: ", end='')
list2.printList()

list2.remove(90)
print("List 2: ", end='')
list2.printList()
