def crackle_pop() -> None:
  for i in range(1, 100):
    to_print: str =""
    if i % 3 == 0:
      to_print+="Crackle"
    if i % 5 == 0:
      to_print+="Pop"
    if len(to_print) == 0:
      to_print = i
    print(to_print)

