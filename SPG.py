import sympy

def factorize(n):
    """Канонічний розклад числа на прості множники."""
    return sympy.factorint(n)

def build_tables(A, n, factors):
    """Побудова таблиць залишків для алгоритму."""
    tables = {}
    for prime, power in factors.items():
        temp = []
        for j in range(prime):
            r_p_i = pow(A, n * j // prime, n + 1)
            temp.append(r_p_i)
        tables[prime] = temp
    return tables

def compute_remainder(n, prime, A, B, power, residues):
    """Обчислення залишку для одного простого множника."""
    x = residues.index(pow(B, n // prime, n + 1))
    result = x
    for i in range(1, power):
        alpha_pow = pow(A, result, n + 1)
        m = B * pow(alpha_pow, -1, n + 1)
        reduced = pow(m, n // prime**(i + 1), n + 1)
        next_residue = residues.index(reduced)
        result += next_residue * prime**i
    return result, prime**power

def chinese_remainder_theorem(congruences):
    """Розв'язання системи конгруенцій за китайською теоремою залишків."""
    M = 1
    for _, modulus in congruences:
        M *= modulus
    solution = 0
    for residue, modulus in congruences:
        M_i = M // modulus
        solution += residue * M_i * pow(M_i, -1, modulus)
        solution %= M
    return solution

def sph_algorithm(A, B, n):
    """Алгоритм Сільвера-Поліга-Геллмана."""
    factors = factorize(n)
    tables = build_tables(A, n, factors)

    congruences = []
    for prime in factors:
        remainder, modulus = compute_remainder(n, prime, A, B, factors[prime], tables[prime])
        congruences.append((remainder, modulus))

    return chinese_remainder_theorem(congruences)

alpha = int(input("Генератор групи: "))
beta = int(input("Елемент групи: "))
group_order = int(input("Порядок групи: "))

print("\nАлгоритм Сільвера-Поліга-Геллмана:")
x = sph_algorithm(alpha, beta, group_order)
print("x =", x)
