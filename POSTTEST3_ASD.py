import pwinput
import os
import time

class Drakor_ID:
    JudulDrakor = ''
    GenreDrakor = ''

pilih = 0
DataDrakor = []

def login():
    print('''\n
    ==================================================
    |                  L O G I N                     |
    ==================================================''')
    uname = str.lower(input("Masukkan username : "))
    username = uname.capitalize()
    if username == "Sunny" :
        pin = int(pwinput.pwinput("Masukkan PIN : "))
        if pin == 123 :
            time.sleep(1)
            os.system('cls')
            menu()
        else:
            print("Silahkan masukkan PIN yang sesuai!")
            time.sleep(1)
            os.system('cls')
            login()
    else:
        print("Silahkan masukkan username yang sesuai!")
        time.sleep(1)
        os.system('cls')
        login()

def menu():
    pilih = str(input('''
    =================================
    |            Welcome            |
    |           DRAKOR.ID           |
    =================================
    |>>>>> Silahkan pilih opsi <<<<<|
    |                               |
    |   1. Drakor Favorit           |
    |   2. Drakor On Going          |
    |   3. Variety Show             |
    |   4. History Tontonan         |
    |   5. Log Out                  |
    =================================
Silahkan pilih opsi (1/2/3/4): '''))
    if pilih == '1':
        time.sleep(1)
        os.system('cls')
        drakor_fav()
    elif pilih == '2':
        time.sleep(1)
        os.system('cls')
        drakor_OnGoing()
    elif pilih == '3':
        time.sleep(1)
        os.system('cls')
        variety_show
    elif pilih == '4':
        time.sleep(1)
        os.system('cls')
        history()
    elif pilih == '5':
        time.sleep(1)
        os.system('cls')
        LogOut()
    else:
        print("Masukkan pilihan opsi yang benar")
        time.sleep(1)
        os.system('cls')
        menu()

def drakor_fav():
    class Node:
      # constructor for Node class
        def __init__(self, data):
            self.data = data
            self.ref = None

    class LinkedList():
      # constructor for LinkedList class
        def __init__(self):
            self.head = None
        
        def print_linkedlist(self):
            if self.head is None:
                print("The linked list is empty.")
            
            else:
                n = self.head
                while n is not None:
                    print(n.data, end=" ---> ")
                    n = n.ref

        def add_beginning(self, data):
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        
        def add_end(self, data):
            new_node = Node(data)
            if self.head is None:
                print("Linked list is empty. Initiating the linked list with given data")
                self.head = new_node
            else:
                n = self.head
                while n.ref is not None:
                    n = n.ref
                n.ref = new_node

    if __name__ == "__main__":
        l1 = LinkedList()

        l1.add_beginning("Welcome To Waikiki")
        l1.add_beginning("The Penthouse")
        l1.add_end("The Glory")
        l1.add_end("My Name")
        l1.print_linkedlist()

login()