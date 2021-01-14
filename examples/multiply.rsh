program MULTIPLY:
  
  <num> number1 as <num>in: "type a number > ".
  <num> number2 as <num>in: "type another number > ".
  MULTIPLY_FUNC: number1, number2.

end program MULTIPLY.
  
piece MULTIPLY_FUNC receives <num> n, <num> n2:

  <num> result as n * n2.
  out: result.
  exit: result.

end piece MULTIPLY_FUNC.