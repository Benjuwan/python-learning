class A:
    pass

class B(A):
    pass

class C(A):
    pass

print(issubclass(C, A))
print(issubclass(C, B))
