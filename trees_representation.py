class elem:
	def __init__ (self , value ):
		self.p = None
		self.key = value
		self.left = None
		self.right = None

	def ShowLeaves ( self ):
		if self == None :
			return
		if self.left == None :
			self.Show ()
		else:
			y=self.left
			while y != None :
				y.ShowLeaves()
				y=y.right

	#the method Show displays the four members of an element on the same line. Test this method (and the constructor) with a single object of the class elem.
	# Make sure to put the following function inside the class elem
	def Show ( self ):
		keyparent = " None "
		if self.p != None:
			keyparent = self.p.key
		keyleft = " None "
		if self.left != None:
			keyleft = self.left.key
		keyright = " None "
		if self.right != None:
			keyright = self.right.key
		print ("In this node , key = " + str( self.key)\
		+ "\t parent = " + str(keyparent)\
		+ "\t left-child = " + str( keyleft )\
		+ "\t right-sibling = " + str(keyright ))

	def Show2(self):
		string = " key : "+str(self.key)+" parents : "+str(self.p)+" left-child :"+str(self.left)+" right-child :"+str(self.right)
		print(string)
	
	#the method AddRightChild takes an element x as a parameter, and adds it as the rightmost child of the current element.
	def AddRightChild (self , x):
		if self.left == None:
			self.left = x
		else:
			rightmost = self.left
			while rightmost.right != None:
				rightmost = rightmost.right
			rightmost.right = x
		x.p = self

	#method ShowDescendants displays all the descendants of the current node in the tree. The method Show is used as a subroutine.
	def ShowDescendants ( self ):
		x = self
		x. Show ()
		y = x.left
		while y!= None :
			y.ShowDescendants ()
			y = y.right
	# Make sure to put the following function inside the class elem
		

# It can be tested by invoking
e1=elem(88)
e1.Show()

class tree: 
	def __init__ (self , x=None ):
		self.root = x
	# Make sure to put the following function inside the class tree
	def ShowLeaves( self ):
		print (" Leaves of the tree :")
		if self.root == None :
			print(" Empty tree ")
		else:
			self.root.ShowLeaves()


# The given tree is built as follows :
T = tree(elem (6))
T.root.AddRightChild ( elem (7))
T.root.AddRightChild ( elem (5))
T.root.AddRightChild ( elem (1))
# The tree is displayed as follows :
T.root.Show()
T.root.left.Show()
T.root.left.right.Show()
T.root.left.right.right.Show()
print("===================================================")
print("==============display the descendants==============")
print("===================================================")
# The tree is displayed as follows :
T.root.ShowDescendants()
# These function can be tested by invoking
print("===================================================")
print("================display tree leaves================")
print("===================================================")
T.ShowLeaves()