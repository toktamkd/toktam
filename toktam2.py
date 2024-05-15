class Node:
    def __init__(self, coefficient=0, power=0):
        self.coefficient = coefficient
        self.power = power
        self.next = None

def add_polynomials(poly1, poly2):
    dummy = Node()
    current = dummy

    while poly1 is not None and poly2 is not None:
        if poly1.power > poly2.power:
            current.next = Node(poly1.coefficient, poly1.power)
            poly1 = poly1.next
        elif poly1.power < poly2.power:
            current.next = Node(poly2.coefficient, poly2.power)
            poly2 = poly2.next
        else:
            coeff_sum = poly1.coefficient + poly2.coefficient
            if coeff_sum != 0:
                current.next = Node(coeff_sum, poly1.power)
            poly1 = poly1.next
            poly2 = poly2.next
        current = current.next

    current.next = poly1 if poly1 is not None else poly2

    return dummy.next

def multiply_polynomials(poly1, poly2):
    result = Node()
    while poly1 is not None:
        temp = poly2
        while temp is not None:
            coeff = poly1.coefficient * temp.coefficient
            power = poly1.power + temp.power
            result = add_polynomials(result, Node(coeff, power))
            temp = temp.next
        poly1 = poly1.next

    return result


poly1 = Node(4, 2)
poly1.next = Node(5, 1)
poly1.next.next = Node(6, 0)


poly2 = Node(2, 2)
poly2.next = Node(7, 1)
poly2.next.next = Node(3, 0)

print("\nadd two polynomials:")
result_sum = add_polynomials(poly1, poly2)
while result_sum is not None:
    print(f"{result_sum.coefficient}x^{result_sum.power}", end=" ")
    if result_sum.next is not None:
        print("+", end=" ")
    result_sum = result_sum.next

print("\nmultiply two polynomials:")
result_mul = multiply_polynomials(poly1, poly2)
while result_mul is not None:
    print(f"{result_mul.coefficient}x^{result_mul.power}", end=" ")
    if result_mul.next is not None:
        print("+", end=" ")
    result_mul = result_mul.next
