'''
Author: Sofia Gutierrez
Lab #3: The purpose of this lab is to impelement different functions to perform on a Linked List
'''

import matplotlib.pyplot as plt
import numpy as np
import random

class ListNode:
    # Constructor
    def __init__(self, data,next=None):
        self.data = data
        self.next = next

class List:
    # Constructor
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = tail
    
    def Print(self):
        t = self.head
        while t != None:
            print(t.data,end = ' ')
            t = t.next
        print()
    
    def Append(self,x):
        if self.head is None:
            self.head = ListNode(x)
            self.tail = self.head
        else:
            self.tail.next = ListNode(x)
            self.tail = self.tail.next
    
    def AppendList(self,python_list):
        for d in python_list:
            self.Append(d)
    
    def Extend(self,python_list):
        for d in python_list:
            self.append(d)
    
    def _rectangle(self,x0,y0,dx,dy):
        # Returns the coordinates of the corners of a rectangle
        # with bottom-left corner (x0,y0), dx width and dy height
        x = [x0,x0+dx,x0+dx,x0,x0]
        y = [y0,y0,y0+dy,y0+dy,y0]
        return x,y
    
    def draw(self,figure_name=' '):
        # Assumes the list contains no loops
        fig, ax = plt.subplots()
        x, y = self._rectangle(0,0,20,20)
        ax.plot(x,y,linewidth=1,color='k')
        ax.plot([0,20],[10,10],linewidth=1,color='k')
        ax.text(-2,15, 'head', size=10,ha="right", va="center")
        ax.text(-2,5, 'tail', size=10,ha="right", va="center")
        t = self.head
        x0 = 40
        while t !=None:
            x, y = self._rectangle(x0,0,30,20)
            ax.plot(x,y,linewidth=1,color='k')
            ax.plot([x0+15,x0+15],[0,20],linewidth=1,color='k')
            ax.text(x0+7,10, str(t.data), size=10,ha="center", va="center")
            if t.next == None:
                ax.text(x0+22,10, '/', size=15,ha="center", va="center")
            else:
                ax.plot([x0+22,x0+40],[10,10],linewidth=1,color='k')
                ax.plot([x0+37,x0+40,x0+37],[7,10,13],linewidth=1,color='k')
            t = t.next
            x0 = x0+40
        if self.head == None:
            ax.text(12,15, '/', size=10,ha="center", va="center")
        else:
            ax.plot([10,40],[15,15],linewidth=1,color='k')
            ax.plot([37,40,37],[12,15,18],linewidth=1,color='k')

        if self.tail == None:
            ax.text(12,5, '/', size=10,ha="center", va="center")
        else:
            xt = 40
            t = self.head
            while t!= self.tail:
                t = t.next
                xt+=40
            ax.plot([10,10,xt+15,xt+15],[5,-10,-10,0],linewidth=1,color='k')
            ax.plot([xt+12,xt+15,xt+18],[-3,0,-3],linewidth=1,color='k')

        ax.set_title(figure_name)
        ax.set_aspect(1.0)
        ax.axis('off')
        fig.set_size_inches(1.2*(x0+200)/fig.get_dpi(),100/fig.get_dpi())
        plt.show()
    
    def Insert(self,i,x):
        new_node = ListNode(x)
        if self.head != None:
            if i == 0:
                new_node.next = self.head 
                self.head = new_node
            else:
                t, counter = self.head, 1
                while counter != i and t.next != None:
                    counter += 1
                    t = t.next
                new_node.next = t.next
                t.next = new_node
        else:
            self.head = new_node
    
    def Remove(self,x):
        if self.head == None:
            raise ValueError("Value not found")
        if self.head.data == x:
            self.head = self.head.next
        else:
            t  = self.head
            while t.data != x and t.next != None:
                prev = t
                t = t.next
            if t.data == x:
                if t.next != None:
                    prev.next = t.next
                else:
                    prev.next = None
            else:
                raise ValueError("Value not found")
    
    def Pop(self,i):
        t, counter = self.head, 0
        while t != None:
            if counter == i:
                self.Remove(t.data)
                return t.data
            counter += 1
            t = t.next
        self.Remove(self.tail)
    
    def Clear(self):
        self.head = None
        self.tail = None
    
    def Index(self,x,start,end):
        if self.head == None:
            return
        t, counter = self.head, 0
        while t != None:
            if counter >= start and t.data == x:
                if counter <= end:
                    return counter
            counter += 1
            t = t.next
        print("Value not found")
    
    def Count(self,x):
        if self.head == None:
            return 0
        t, counter = self.head, 0
        while t != None:
            if t.data == x:
                counter += 1
            t = t.next
        return counter
    
    def Insert_for_sort(self,i):
        if self.head == None:
            self.head = ListNode(i)
            self.tail = ListNode(i)
        else:
            new_node = ListNode(i)
            if new_node.data < self.head.data:
                temp = self.head
                self.head = new_node
                self.head.next = temp
            else:
                t = self.head
                while t.data < new_node.data and t.next != None:
                    t = t.next
                if t.data < new_node.data and t.next == None:
                    t.next = new_node
                    self.tail = new_node
                if t.data < new_node.data:
                    t.next = new_node
                    new_node.next = t.next.next
    
    def Sort(self):
        if self.head == None:
            return
        t, data_list = self.head, []
        while t != None:
            data_list.append(t.data)
            t = t.next
        sorted_list = List()
        for i in data_list:
            sorted_list.Insert_for_sort(i)
        return sorted_list
    
    def Sort2(self):
        if self.head == None:
            return
        t = self.head
        while t.next != None:
            if t.data > t.next.data:
                t.data, t.next.data = t.next.data, t.data
            t = t.next
        return
    
    def Reverse(self):
        if self.head == None or self.head.next == None:
            return
        else:    
            t, prev = self.head, None
            while t != None: 
                next = t.next
                t.next = prev 
                prev = t 
                t = next
            self.head = prev
    
    def Copy(self):
        if self.head == None:
            return
        L2 = List()
        t = self.head
        while t != None:
            L2.Append(t.data)
            t = t.next
        return L2

if __name__ == "__main__":
    # It won't execute when this file is imported
    '''
    plt.close('all')
    L1 = List()
    L1.draw('Empty list')
    L1.extend(list(np.random.permutation(10)))
    L1.draw('Unsorted list')
    L1 = List()
    L1.extend(list(np.arange(10)))
    L1.draw('Sorted list')
    L1.tail = L1.head.next.next
    L1.draw('Bad list!')
    L1.tail = None
    L1.draw('Another bad list!')
    '''
    
    i = random.sample(range(0, 10), 5)
    L1 = List()
    L1.AppendList(i)
    
    print("Insert function:")
    L1.Print()
    L1.Insert(0,1000)
    L1.Print()
    
    print("Remove function:")
    L1.Print()
    L1.Remove(1000)
    L1.Print()
    
    print("Pop function:")
    L1.Print()
    print(L1.Pop(1))
    L1.Print()
    
    print("Clear function:")
    L1.Print()
    L1.Clear()
    L1.Print()
    
    print("Count function:")
    print(L1.Count(1000))
    
    print("Copy function:")
    L1.Print()
    L2 = L1.Copy()
    L2.Print()
    
    print("Reverse function:")
    L1.Reverse()
    L1.Print()
    
    print("Sort function:")
    L1.Print()
    sorted_list = L1.Sort()
    sorted_list.Print()
    
    print("Sort2 function")
    L1.Print()
    L1.Sort2()
    L1.Print()
    
    print("Index function:")
    L1.Print()
    print(L1.Index(8,0,4))