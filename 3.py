'''
Project: AVL Tree
Author: Sakhno Danylo
Version: 1.0
Release: 14.12.2025
'''

class Node:
   id = None
   root = None
   parent = None
   leftChild = None
   rightChild = None

   # Constructor    
   def __init__(self, id):
      self.id = id
      self.root = self

   # Balance Factor function     
   def getBF(self):
      leftBF = self.getHeightLeft()
      rightBF = self.getHeightRight()
      return (leftBF - rightBF)

   # Returns a node by ID
   def getNode(self, id):
      result = None
      if (self.id == id):
         return (self)
      if (self.leftChild != None):
         if (self.leftChild.id == id):
            return self.leftChild
         else:
            result = self.leftChild.getNode(id)
            if (result != None):
               return (result)
      if (self.rightChild != None):
         if (self.rightChild.id == id):
            return self.rightChild
         else:
            result = self.rightChild.getNode(id)
            if (result != None):
               return (result)

   # Append a child node to the left of current one
   def addLeft(self, node):
      if (self.leftChild == None):
         if (node != None):
            self.leftChild = node
            self.leftChild.parent = self
            self.leftChild.root = self.root
      return node

   # Append a child node to the right of current one
   def addRight(self, node):
      if (self.rightChild == None):
         if (node != None):         
            self.rightChild = node
            self.rightChild.parent = self
            self.rightChild.root = self.root
      return node

   # Append a node to the whole tree keeping the balance
   def add(self, parent, node):
      leftBF = parent.getHeightLeft()
      rightBF = parent.getHeightRight()
      if (leftBF > rightBF):
         if (parent.rightChild != None):
            parent.add(parent.rightChild, node)  
         else:
            parent.addRight(node)
      else:
         if (parent.leftChild != None):
            parent.add(parent.leftChild, node)  
         else:
            parent.addLeft(node)

   # Print hierarchy
   def showTree(self, node):
      result = str(node.id) + '|'
      if (node.leftChild != None):
         result = result + str(node.leftChild.id) + '|'
      else:
         result = result + ' |'
      if (node.rightChild != None):
         result = result + str(node.rightChild.id)
      print(result)
      if (node.leftChild != None):
         node.leftChild.showTree(node.leftChild)
      else:
         result = result + ' |'
      if (node.rightChild != None):
         node.rightChild.showTree(node.rightChild)

   # Calculate the left child branch
   def getHeightLeft(self):
      ll = 0
      lr = 0
      result = 0
      if (self.leftChild != None):
         ll = self.leftChild.getHeightLeft()
         lr = self.leftChild.getHeightRight()
         result = 1
      if (ll > lr) :
         result = result + ll
      else:
         result = result + lr
      return result
      
   # Calculate the right child branch
   def getHeightRight(self):
      ll = 0
      lr = 0
      result = 0
      if (self.rightChild != None):
         ll = self.rightChild.getHeightLeft()
         lr = self.rightChild.getHeightRight()
         result = 1
      if (ll > lr) :
         result = result + ll
      else:
         result = result + lr
      return result

   # Update root reference trough the tree if it was changed
   def updateRoot(self, root):
      self.root = root
      if (self.leftChild != None):
         self.leftChild.updateRoot(root)
      if (self.rightChild != None):
         self.rightChild.updateRoot(root) 

   # Rotate to the right 
   def rotateRight(self):
      old_parent = self.parent
      self.parent = None
      substitute = self.leftChild
      self.leftChild = None
      if old_parent != None:
         if (old_parent.leftChild == self):
            old_parent.leftChild = None
            old_parent.addLeft(substitute)
         else:
            old_parent.rightChild = None
            old_parent.addRight(substitute)
      else:
         substitute.parent = None
      if (substitute.leftChild != None):
         bfl = substitute.leftChild.getBF()
      else:
         bfl = 0
      if (substitute.rightChild != None):
         bfr = substitute.rightChild.getBF()
      else:
         bfr = 0
      if (bfl < bfr):
         tempchild = substitute.rightChild
         substitute.rightChild = None 
      else:
         tempchild = substitute.leftChild            
         substitute.leftChild = None
      substitute.addLeft(self)
      substitute.add(substitute, tempchild)
      if (old_parent == None):
         substitute.updateRoot(substitute)

   # Rotatte to the left
   def rotateLeft(self):
      old_parent = self.parent
      self.parent = None
      substitute = self.rightChild
      self.rightChild = None
      if old_parent != None:
         if (old_parent.rightChild == self):
            old_parent.rightChild = None
            old_parent.addRight(substitute)
         else:
            old_parent.leftChild = None
            old_parent.addLeft(substitute)
      else:
         substitute.parent = None
      if (substitute.leftChild != None):
         bfl = substitute.leftChild.getBF()
      else:
         bfl = 0
      if (substitute.rightChild != None):
         bfr = substitute.rightChild.getBF()
      else:
         bfr = 0
      if (bfl < bfr):
         tempchild = substitute.rightChild
         substitute.rightChild = None 
      else:
         tempchild = substitute.leftChild            
         substitute.leftChild = None
      substitute.addLeft(self)
      substitute.add(substitute, tempchild)
      if (old_parent == None):
         substitute.updateRoot(substitute)

   # Rebuild the tree to get the balance
   def balance(self, node):
      bf = node.getBF()
      if (bf == 0) or (abs(bf) == 1) :
         return
      else:
         if (bf < 0):
            node.rotateLeft()
         else:
            node.rotateRight()
      if node.leftChild != None:
         node.balance(node.leftChild)
      if node.rightChild != None:
         node.balance(node.rightChild)    

   # Remove a node from the tree
   def remove(self):
      parent = self.parent
      if (parent != None):
         if (parent.leftChild == self):
            parent.leftChild = None
         if (parent.rightChild == self):
            parent.rightChild = None
         parent.balance(parent.root)
         del self

   # Insert a node to the current node if it has available place
   def insert(self, node):
      if (self.leftChild == None):
         self.addLeft(node)
      if (node.parent == None):
         if (self.rightChild == None):
            self.addRight(node)
      if (node.parent == None):
         raise Exception('No available place')
      else:
         self.balance(self.root)        
   


node_1 = Node(1)
node_2 = Node(2)
node_1.addLeft(node_2)
node_3 = Node(3)
node_1.addRight(node_3)
node_4 = Node(4)
node_3.addLeft(node_4)
node_5 = Node(5)
node_3.addRight(node_5)
node_6 = Node(6)
node_4.addLeft(node_6)
node_1.showTree(node_1.root)
print('BF=', node_1.root.getBF())
node_1.balance(node_1)
node_1.showTree(node_1.root)
print('BF=', node_1.root.getBF())
node_2.remove()
node_1.showTree(node_1.root)
print('BF=', node_1.root.getBF())
print('Left height=', node_1.root.getHeightLeft())
print('Right height=', node_1.root.getHeightRight())
node_7 = Node(7)
node_1.insert(node_7)
node_1.showTree(node_1.root)



