class A:
    pass

class B(A):
    pass

class C(A):
    pass

print(isinstance(C(), A))
print(isinstance(C(), B))
print(isinstance(C(), C))
