class Node:
    def __init__(self, saturs, pirms = None, pec=None):
        self.info = saturs
        self.prev = pirms
        self.next = pec

    def read(self):
        print(self.info)

class List:
    def __init__(self, pirmais_info):
        self.pirmais = Node(pirmais_info)
    
    def add(self, jaunais_info, indekss = -1):
        if indekss == -1:
            pedejais = self.pirmais
            while pedejais.next:
                pedejais = pedejais.next
            # pedejais.next = Node(jaunais_info, pirms = pedejais)
            pedejais.next = Node(jaunais_info)
            pedejais.next.prev = pedejais
            return pedejais.next
        
        if indekss == 0:
            self.pirmais = Node(jaunais_info, pec=self.pirmais)
            self.pirmais.next.prev = self.pirmais
            return self.pirmais
        
        ieprieksejais = self.pirmais
        for i in range(indekss-1):
            if ieprieksejais.next == None:
                self.add(jaunais_info)
                return
            ieprieksejais = ieprieksejais.next
           
        ieprieksejais.next = Node(jaunais_info, pec = ieprieksejais.next, pirms=ieprieksejais)
        jaunais = ieprieksejais.next
        if jaunais.next:
            jaunais.next.prev = jaunais
        return jaunais
        
    
    def read(self):
        esosais = self.pirmais
        while esosais:
            esosais.read()
            esosais = esosais.next
        return
    
    def len(self):
        garums = 0
        skaititajs = self.pirmais
        while skaititajs:
            garums += 1
            skaititajs = skaititajs.next
        return garums


    def get(self, index):
        if index == 0:
            return self.pirmais
        esosais = self.pirmais
        for i in range(index):
            esosais = esosais.next
        return esosais
    
    def put(self, ieliekama_node: Node, index):
        if ieliekama_node.prev and ieliekama_node.next:
            ieliekama_node.prev.next = ieliekama_node.next
            ieliekama_node.prev = None
            ieliekama_node.next = None

        if ieliekama_node.next:
            self.pirmais = ieliekama_node.next
            ieliekama_node.next = None
        
        if ieliekama_node.prev:
            ieliekama_node.prev.next = None
            ieliekama_node.prev = None

        turpinajums = None
        if index < self.len()-1:
            turpinajums = self.get(index+1)
        # turpinajums.read()
        if index == 0:
            self.pirmais = ieliekama_node
            self.pirmais.next = turpinajums
            self.pirmais.next.prev = self.pirmais
            self.pirmais.prev = None
            return
        
        ieprieksejais = self.pirmais
        for i in range(index-1):
            ieprieksejais=ieprieksejais.next
        
        # ieprieksejais.read()
        # ieliekama_node.read()
        ieprieksejais.next = ieliekama_node
        esosais = ieprieksejais.next
        # esosais.read()
        esosais.prev = ieprieksejais
        esosais.next = turpinajums
        if esosais.next:
            esosais.next.prev = esosais

        return esosais

        


    def switch(self, index1, index2):
        if index1>index2:
            self.switch(index2, index1)
            return
        
        kopija_pirmais = self.get(index1)
        kopija_otrais = self.get(index2)

        self.put(kopija_otrais, index1)
        self.add("tukss", index2)
        kopija_pirmais.prev = None
        kopija_pirmais.next = None

        self.put(kopija_pirmais, index2)

        return


print("Sākotnējais saraksts:")
saraksts = List("suns")
saraksts.add(24)
saraksts.add("hei, visi!")
saraksts.add("pirmais", 0)
saraksts.add("ceturtais", 3)
saraksts.add("beigas",5)
saraksts.read()
print("Nomainīts elements pie indeksa 3:")

saraksts.put(Node("tests"),3)
saraksts.read()
print("Apmainīti vietām elementi pie indeksa 5 un 0:")
saraksts.switch(5,0)
saraksts.read()
