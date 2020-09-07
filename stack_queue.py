
class stack :
    def __init__(self,n) :
        self.v = [0]*n
        self.length = n
        self.top = -1

    def show (self) :
        print("The array :", self.v)
        print("length :", self.length)
        print("top =", self.top)

    def empty(self) :
        if self.top == -1 :
            return True
        else : return False

    def push (self,x) :
        if self.top == -1 :
            self.top += 1
            self.v[self.top] = x
        else :
            self.top += 1
            if self.top >= self.length :
                self.v.append(x)
            else : self.v[self.top] = x

    def pop (self) :
        if self.empty() :
            print("error underflow")
        else :
            self.top -=1
            return self.v[self.top+1]

s = stack(4)
print("Ajout :")
s.push(6)
print("The array is :", s.v)
s.push(2)
print("The array is :", s.v)
s.push(1)
print("The array is :", s.v)
s.push(8)
print("The array is :", s.v)
s.push(9)
print("The array is :", s.v)

print()
print("Extraction :")
print("element extrait :",s.pop())
print("element extrait :",s.pop())
print("element extrait :",s.pop())
print("element extrait :",s.pop())
print("element extrait :",s.pop())
print("The array is :", s.v)
print()


class queue :
    def __init__ (self,n):
        self.v =[0]*n
        self.length = n
        self.top =0
        self.head = 0

    def show (self) :
        print("The array :", self.v)
        print("length :", self.length)
        print("top =", self.top)
        print("head =", self.head)

    def enqueue (self,x) :
        self.v[self.top]=x
        if self.length == self.top :
            self.top = 1
        else :
            self.top += 1

    def dequeue (self) :
        x = self.v[self.head]
        if self.head == self.length :
            self.head = 1
        else :
            self.head += 1
        return x

print("Ajout :")
q = queue(5)
q.show()
q.enqueue(8)
q.show()
q.enqueue(15)
q.show()
q.enqueue(-4)
q.show()
q.enqueue(9)
q.show()
q.enqueue(12)
q.show()
print()
print("Extraction :")
print("element :",q.dequeue())
print("element :",q.dequeue())
print("element :",q.dequeue())
print("element :",q.dequeue())
print()


def reverse (s) :
    q = queue(s.length)
    cpt = 0
    while cpt < s.length :
        elem = s.pop()
        q.enqueue(elem)
        print(elem)
        print(q.v)
        cpt+=1
    return q

s = stack(4)
s.push(6)
s.push(2)
s.push(1)
s.push(8)
s.show()
q = reverse(s)
q.show()
