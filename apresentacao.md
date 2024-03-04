---
author: Bruno Jardim
---

# Workshop de Python
## Semana da Ciência e Inovação (SCI)



---

# Quick Recap
## Operadores básicos


```python
1 + 2 = 3

1 + 2.0 = 3.0

"hello " + "world" = "hello world"
```


---


# Quick Recap
## Loops
### For-loop

```python
for i in range(10):
  print(i)
  
for i in ["a","b","c"]:
  print(i)
  
```
### While-loop

```python
while(i < 10):
    print(i)
    i += 1
  
```

---

# Quick Recap
## Funções

```python
def fib(n):
  return fib(n - 1) + fib(n - 2)
  
```

---

# Desafio 1

Criar uma função que imprima o seguinte padrão.

```txt
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
    #
```

# Desafio 2 

Generalizar a função para uma árvore de tamanho N


---

# Conceitos
## Recursividade
Utilização de uma função como definição dela própria.


```python
def fib(n):
  return fib(n - 1) + fib(n - 2)
  
```

---

# Conceitos
## Recursividade
Utilização de uma função como definição dela própria.


```python
def fib(n):
  return fib(n - 1) + fib(n - 2)
  
```

### Cuidados

- Caso base/terminação.
- Caso geral converge para o caso base.


---

# Conceitos
## Recursividade
Utilização de uma função como definição dela própria.


```python
def fib(n):
  # Falta caso base
  return fib(n - 1) + fib(n - 2) # Falta garantir que converge para o caso base  
```

### Cuidados

- Caso base/terminação.
- Caso geral converge para o caso base.

---

# Conceitos
## Recursividade
Utilização de uma função como definição dela própria.

```python
def fib(n):
  assert(n >= 0)
  
  if n == 0 or n == 1:
    return 1
   
  return fib(n - 1) + fib(n - 2)
```
Seria a implementação correta desta função.


---

# Conceitos
## Operações com FP

Devido à memória de uma computador ser limitada existem certos números que não são possiveis representar sem erros de arredondamento.
Isto deve-se à representação binária que os números têm que tomar.

Um dos exemplos mais simples seria 

0.1 = 0.00011001100110011...(representação binária de 0.1)

---

# Conceitos
## Operações com FP

Devido à memória de uma computador ser limitada existem certos números que não são possiveis representar sem erros de arredondamento.
Isto deve-se à representação binária que os números têm que tomar.

Um dos exemplos mais simples seria 

0.1 = 0.00011001100110011...(representação binária de 0.1)

### Exemplos

```python
>>> 0.1 + 0.2 == 0.3
False

>>> 0.1 + 0.2
0.30000000000000004

>>> import math
>>> pi = 3.1415926535897932384626433832795
>>> math.tan(pi/2.0)
1.633123935319537e+16
  
```

---

# Conceitos
## Complexidade (Temporal)
É o que descreve a quantidade de tempo que um computador gasta num determinado algoritmo.

- O(1)  
- O(log(n))  
- O(n)
- O(n log(n))
- O(n^2)
- O(2^n)
- O(n!)

### Exemplo

```python
def fib(n):
  assert(n >= 0)
  
  if n == 0 or n == 1:
    return 1
   
  return fib(n - 1) + fib(n - 2)
```

Tem complexidade ≃ O(2^n)

---

# Conceitos
## Complexidade (Temporal)

```python
def fib(n):
  assert(n >= 0)
  
  if n == 0 or n == 1:
    return 1
   
  return fib(n - 1) + fib(n - 2)
```
### Qual é a solução para esta complexidade elevada?

---

# Conceitos
## Complexidade (Temporal)

```python
def fib(n):
  assert(n >= 0)
  
  if n == 0 or n == 1:
    return 1
   
  return fib(n - 1) + fib(n - 2)
```
### Qual é a solução para esta complexidade elevada?

Utilizar um estratégia que não faça tantos cálculos desnecessários

```python
def fib(n):
  a = 1
  b = 0
  for i in range(n):
    a, b = a+b, a
  return a
```
Tem complexidade ≃ O(n)

---

# Exemplos práticos
- Lokta-Volterra
- Teoria de Números
- Relação temperatura-pressão em gases

---

# Workshop de Python
## Semana da Ciência e Inovação (SCI)
