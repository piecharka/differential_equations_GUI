import tkinter as tk
import differential_equations_methods as diff_methods
import math

def makeform(root, fields):
  entries = {}
  for field in fields:
    row = tk.Frame(root)
    lab = tk.Label(row, width=22, text=field+": ", anchor='w')
    ent = tk.Entry(row)
    if field == 'Equation':
      ent.insert(0, "1+(z-y)*(z-y)")
    elif field == 'Actual value equation':
      ent.insert(0, "z+1/(1-z)")
    elif field == 'First endpoint':
      ent.insert(0, "2")
    elif field == 'Second endpoint':
      ent.insert(0, "5")
    elif field == 'Number of steps':
      ent.insert(0, "20")
    elif field == 'Initial value':
      ent.insert(0, "1")
    else: 
      ent.insert(0, "0")
    row.pack(side=tk.TOP, 
      fill=tk.X, 
      padx=5, 
      pady=5)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT, 
      expand=tk.YES, 
      fill=tk.X)
    entries[field] = ent
  return entries


def actual_value(z, input_code):
  code_with_values = input_code.replace('z', str(z))
  return eval(code_with_values)


def g(z, y, input_code):
  code_with_values = input_code.replace('z', str(z)).replace('y', str(y))
  return eval(code_with_values)


def submit(entries):
  equation_code = entries['Equation'].get()
  actual_value_code = entries['Actual value equation'].get()

  a_endpoint = float(entries['First endpoint'].get())
  b_endpoint = float(entries['Second endpoint'].get())
  N = int(entries['Number of steps'].get())
  initial_value = float(entries['Initial value'].get())

  x,y = diff_methods.euler(g, a_endpoint, b_endpoint, N, initial_value, equation_code)

  x_mid, y_mid = diff_methods.midpoint(g, a_endpoint, b_endpoint, N, initial_value, equation_code)

  actual = [actual_value(val, actual_value_code) for val in x]
  #diff_methods.display(x, y, actual)
  print(x,x_mid)
  print(y, y_mid)
  diff_methods.display_multiple_plots([x, x_mid], [y, y_mid], actual)


if __name__ == '__main__':
  root = tk.Tk()
  root.title('App')

  fields = ('Equation', "Actual value equation", 'First endpoint', 'Second endpoint', 'Number of steps', 'Initial value')
  entries = makeform(root, fields)
  button = tk.Button(root, text="Submit", width=10, height=2, command=(lambda e=entries: submit(e)))
  button.pack()
  root.mainloop()
