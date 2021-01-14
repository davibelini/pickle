program BARK:       // main part of the file.

  <DOG> dog as DOG. dog::bark: "arf-arf". // instantiate DOG to dog variable and use the subpiece bark with argument 'arg'.

end program BARK.

piece DOG:

  subpiece bark receives <str> arg:
    out: arg.
  end piece bark.

end piece DOG.