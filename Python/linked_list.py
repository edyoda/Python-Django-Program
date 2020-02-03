#!/usr/bin/env python
# coding: utf-8
Hello all. Here we will see how to create linked list in python. We will implement CRUD(create, read, update, delete) operations also
# In[9]:


# create a node class so we can create node for each and every element
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# Create a linked list class so that we create a class
class LinkedList:
    def __init__(self):
        self.head=None

# insert at beginning of list
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

#insert at a particular location
    def insertAfter(self, prev_node, new_data):
        if prev_node is None: 
            print ("The given previous node must inLinkedList.")
            return
        new_node = Node(new_data)  
        new_node.next = prev_node.next
        prev_node.next = new_node 

# insert at end of list
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=new_node

# update element
    def update(self, data, update_by):
        temp = self.head
        while(temp):
            if temp.data==data:
                temp.data=update_by
                return
            temp=temp.next
        return ("data doesn't not exist")

# remove an element
    def remove(self,remove_data):
        temp = self.head
        if (temp is not None):
            if (temp.data == remove_data):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == remove_data:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None

# will our list
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

            
            
l = LinkedList()
l.head=Node(1)
second=Node(2)
third=Node(3)
fourth=Node(4)
fifth=Node(8)
l.head.next=second
second.next=third
third.next=fourth
fourth.next=fifth
l.printList()


# In[14]:


l.insertAtBeginning(5)
l.printList()


# In[15]:


l.insertAfter(third,7)
l.printList()


# In[ ]:




