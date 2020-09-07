##the function createHashTable(m) returns an m-slot hash table, where each slot contains None
def createHashTable(m):
	return [None]*m

##the function h(k, m) returns the slot index where the integer k should reside
##in an m-slot hash table, with the reminder method.
def h(k,m):
	return k%m

##the function search(T, k, m) returns the slot index where the integer k
##resides in the m-slot hash table T, and None if it not present. Use linear probing to handle collisions, and make
##sure that your function runs properly even when T has no empty slots.
def search(T,k,m): 
	index=k%m 
	explored=0 #set to m when all the slots have been explored
	while explored < m and T[index] != None and T[index]!=k:
		explored+=1
		index+=1
		index=index%m
	if(T[index]==k):
		return index
	return None

#define element and LIST classes with all the necessary methods for singly linked
#lists. Each singly linked list should have an attribute name. 
class element:
	def __init__(self,k):
		self.key=k
		self.next=None

	def Show(self):
		keynext="None"
		if self.next !=None:
			keynext =self.next.key
		print("Element with key " \
		+str(self.key)+" points to "+str(keynext))

class LIST:
	def __init__(self):
		self.head = None
		self.name= ""

	def Show(self):
		print("Displaying list"+str(self.name))
		x= self.head
		while x!=None:
			x.Show()
			x=x.next

	def insert(self,x): ##adds element x as the new head of the list
		if isinstance(x,element)==False:
			print("Warning: attempt to insert an invalid element to a list")
			return
		x.next=self.head
		self.head=x

	def search(self, k):##returns x if we find x.key == k in the list, otherwise None
		if self == None or self.head==None:
			return None
		x=self.head
		while x!=None:
			if x.key == k:
				return x
			x=x.next
		return None

	def delete(self,x):
		if x == None or isinstance(x,element)==False:
			print("Warning: attempt to remove an invalid element from the list")
			return
		p=None #predecessor of y
		y=self.head #y browses the list, searching for x
		while y!=x and y!=None:
			p=y
			y=y.next
		if y==self.head:
			self.head=self.head.next
			return
		p.next=y.next


##the function createHashTableChaining(m) returns an array of m empty chained lists, 
##whose names are Slot 0, . . . , Slot m-1, where m-1 should be replaced by its numerical value.
def creatHashTableChaining(m):
	TC=[]
	for i in range(m):
		li=LIST()
		li.name="Slot "+str(i)+":"
		TC.append(li)
	return TC

##the function displayHashTableChaining(T, m) displays all the items in
##the m-slot hash table T where chaining is used.
def displayHashTableChaining(TC,m):
	print("Displaying the items in the hash table with chaining.")
	for i in range(m):
		TC[i].Show()

##the Python function append(T, k, m) adds the integer value k to the m-slot hash
##table T where chaining is used.

####### First , we must write the method insert ( x ) of the class LIST
def append(T,k,m):
	index=h(k,m)
	T[index].insert(element(k))



##the function searchChaining(T, k, m) that returns the element whose key is k
##if it is in the m-slot hash table T using chaining, and None otherwise.

######### First , we must write the method search ( k ) of the class LIST
def searchChaining(T,k,m):
	index=h(k,m)
	return T[index].search(k)





##the function deleteChaining(T, k, m) removes the element whose key is the integer
## k from the m-slot hash table T using chaining. The case where no such element is 
##present in the table should be reported to the user
def deleteChaining(T,k,m):
	x=searchChaining(T,k,m)
	if x!=None:
		T[h(k,m)].delete(x)


##Example of main 
HT=creatHashTableChaining(5)
append(HT,4,5)
append(HT,65,5)
displayHashTableChaining(HT,5)

