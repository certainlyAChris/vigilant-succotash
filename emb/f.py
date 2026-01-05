with open(r"d.py") as f:
    s = compile(filename=r"d.py",source=f.read(),mode="exec")
exec(s)