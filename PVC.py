#package imports
import time 
import ast
import datetime
import os

#predefines colors used in the program
green = ('\033[01;32m')
red = (u'\033[01;31m')
yellow = (u"\u001b[38;5;226m")
purple = (u"\u001b[38;5;135m")

#io open operations
currentDT = datetime.datetime.now()
timenow = currentDT.strftime("%I_%M_%S %p")
filename = "PVC Code Fixes "+str(timenow)+".txt"
fileoutput = "output.txt"
filenamev2 = "Code Converted By PVC "+str(timenow)+".py"
codefix = open(filename,"w+")
fileinput = ""
add = 0

class PVC():
  #outputs the pvc logo
  def logo():
    print(purple+"""

'||''|. '||'  '| ' ..|'''.|
 ||   || '|.  .' .|'     ' 
 ||...|'  ||  |  ||        
 ||        |||   '|.      .
.||.        |     ''|....'
""")

    print(purple + """Welcome To Python Version Converter
A Python 2.x To Python 3.x Converter By Placing
""")

  def loadfile(file):
    reask = True
    while reask:
      fileinput = input(yellow+"\nFile to convert: ")
      try:
        fh = open(fileinput, 'r')
        reask = False
      except FileNotFoundError:
        os.system("clear")
        PVC.logo()
        print(red+"Invalid file, please enter a valid file.")
        continue
    os.system("clear")
    PVC.logo()
    print(green+"Valid file, continuing...\n")
    return(fileinput)



#tests if the code works in py3 
  def py3test(fileoutput):
    try:
        return ast.parse(fileoutput)
    except SyntaxError as exc:
      codefix.write("Issues:"+"\n"+str(exc))
      codefix.close()


  def autofixadd(fileoutput, add, solution):
    linenum = 0
    writefile = open(fileoutput,"r")
    for line in writefile:
      linenum += 1
      if line.count("import") > 0:
        add = linenum
        break

    solutions = PVC.solutions(solution)
    lines = open(fileoutput, 'r').readlines()
    newline = lines[add] + solutions
    lines[add] = newline
    out = open(filenamev2, 'w')
    out.writelines(lines)
    out.close()

#code fixes
  def solutions(fix):
    if fix == "exit":
      return("""
  Solution 1:
    Use sys.exit()
  Solution 2:
    If print and exit are on the same line move exit down to the next line.""")

    if fix == "add_exit":
      return("""import sys\n""")

    elif fix == "execfile":
      return("""
  Solution 1:
    from io import open

    def compile_file(filename):
      with open(filename, encoding='yourencoding') as f:
        return compile(f.read(), filename, 'exec')
    
    exec(compile_file(filename))""")
  
    elif fix == "reload":
      return("""
  Solution:
    Add the follow import statement to your code:
      from importlib import reload""")
    
    elif fix == "add_reload":
      return("""import importlib\n""")

    elif fix == "reduce":
      return("""
  Solution:
    Add the follow import statement to your code:
      from functools import reduce""")
    
    elif fix == "add_reduce":
      return("""import functools\n""")

    elif fix == "intern":
      return("""
  Solution:
    Add the follow import statement to your code:
      from sys import intern""")
    
    elif fix == "add_intern":
      return("""import sys\n""")

    elif fix == "generate_tokens":
      return("""
  Solution:
    Add the follow import statement to your code:
      from tokenize import tokenize""")

    elif fix == "add_tokenize":
      return("""from tokenize import tokenize\n""")

#converts python2 code to working python3 code
  def convert():
    fixes = []
    lines = 0
    linenum = 0
    PVC.logo()
    file = PVC.loadfile(fileinput)
    openfile = open(file,"r")
    codefix = open(filename,"w+")
    writefile = open(fileoutput,"w+")
    time.sleep(1)
    print(yellow+"Loading Code...")
    time.sleep(2)
    for count in openfile:
      lines += 1
    openfile.close()
    print(str(lines), "Lines Of Code Loaded.")
    time.sleep(1)
    print("Converting...\n")
    time.sleep(1)
    openfile = open(file,"r")
    for line in openfile:
      linenum += 1

      if line.count("print") > 0:
        if(line.count("print_") > 0):
          pass
        if(line.count("_print") > 0):
          pass
        if(line.count("_print") > 0):
          pass
        elif(line.count("print ") > 0):
          line = line.replace("print (","print(")
          line = line.replace("print ","print(")
          line = line.replace('\n', '')
          line += ")"
          line += "\n"
          print(green+"Line "+str(linenum)+":"+" Added parenthesis to print statement")
      
      if line.count("return") > 0:
        line = line.replace("return ","return(")
        line = line.replace('\n', '')
        if line.strip() == "return":
          line +="\n"
        else:
          line += ")"
        print(green+"Line "+str(linenum)+":"+" Added parenthesis to return statement")

      if line.count("exec") > 0:
        line = line.replace("exec ","exec(")
        line = line.replace('\n', '')
        line += ")"
        print(green+"Line "+str(linenum)+":"+" Added parenthesis to exec function")

      if line.count("xrange") > 0:
        line = line.replace("xrange","range")
        print(green+"Line "+str(linenum)+":"+" Converted xrange to range")
        

      if line.count("except Exception,") > 0:
        line = line.replace("except Exception,","except Exception as")
        print(green+"Line "+str(linenum)+":"+" Converted except statement")
      
      if line.count("Error, ") > 0:
        if line.count("import") > 0:
          pass
        else:
          line = line.replace("Error, ","Error as ")
          print(green+"Line "+str(linenum)+":"+" Converted except statement")


      if line.count("raw_input") > 0:
        line = line.replace("raw_input","input")
        print(green+"Line "+str(linenum)+":"+" Converted input statement")
        

      if line.count("<>") > 0:
        line = line.replace("<>","!=")
        print(green+"Line "+str(linenum)+":"+" Converted does not equal operator")
        
      
      if line.count("generator.next") > 0:
        line = line.replace("generator.next","next")
        print(green+"Line "+str(linenum)+":"+" Converted next function")
        
        
      
      if line.count("raw_input") > 0:
        line = line.replace("raw_input","input")
        print(green+"Line "+str(linenum)+":"+" Converted input statement")
        

      
      if line.count("raise") + line.count("Error, ") > 1:
        line = line.replace("Error, ","Error(")
        print(green+"Line "+str(linenum)+":"+" Converted raise error statement")
        


      if line.count("iterkeys") > 0:
        line = line.replace("iterkeys","keys")
        print(greeen+"Line "+str(linenum)+":"+" Converted iterkeys function")
        
      
      if line.count("iteritems") > 0:
        line = line.replace("iteritems","items")
        print(green+"Line "+str(linenum)+":"+" Converted iteritems function")
                
      
      if line.count("itervalues") > 0:
        line = line.replace("itervalues","values")
        print(green+"Line "+str(linenum)+":"+" Converted itervalues function")
        
      
      if line.count("file(") > 0:
        line = line.replace("file(","open(")
        print(green+"Line "+str(linenum)+":"+" Converted open file function")
        

      if line.count("        ") > 0:
        line = line.replace("        ","        ")
        print(green+"Line "+str(linenum)+":"+" Converted all spaces to tabs")
        

      if line.count("sorted(") > 0:
        line = line.replace("sorted","repr(sorted")
        print(green+"Line "+str(linenum)+":"+" Converted all spaces to tabs")
        

      if line.count("StandardError") > 0:
        line = line.replace("StandardError","Exception")
        print(green+"Line "+str(linenum)+":"+" Converted StandardError exception")
        

      if line.count("cmp") > 0:
        line = line.replace("cmp","key")
        print(green+"Line "+str(linenum)+":"+" Converted cmp function")
        
      
      if line.count("array.array.read") > 0:
        line = line.replace("array.array.read","array.array.fromfile")
        print(green+"Line "+str(linenum)+":"+" Converted array.read() function")
        

      if line.count("array.array.write") > 0:
        line = line.replace("array.array.write","array.array.tofile")
        print(green+"Line "+str(linenum)+":"+" Converted array.write() function")
        
      
      if line.count("__builtin__") > 0:
        line = line.replace("__builtin__","builtins")
        print(green+"Line "+str(linenum)+":"+" Converted __builtin__ function")
        

      if line.count("_winreg") > 0:
        line = line.replace("_winreg","winreg")
        print(green+"Line "+str(linenum)+":"+" Converted winreg function")
        

      if line.count("ConfigParser") > 0:
        line = line.replace("ConfigParser","configparsec")
        print(green+"Line "+str(linenum)+":"+" Converted ConfigParser function")
        

      if line.count("copy_reg") > 0:
        line = line.replace("copy_reg","copyreg")
        print(green+"Line "+str(linenum)+":"+" Converted copy_reg function")
        
      
      if line.count("Queue") > 0:
        line = line.replace("Queue","queue")
        print(green+"Line "+str(linenum)+":"+" Converted Queue function")
        

      if line.count("SocketServer") > 0:
        line = line.replace("SocketServer","socketserver")
        print(green+"Line "+str(linenum)+":"+" Converted SocketServer function")
        

      if line.count("markupbase") > 0:
        line = line.replace("markupbase","_markupbase")
        print(green+"Line "+str(linenum)+":"+" Converted markupbase function")
        
      
      if line.count("SocketServer") > 0:
        line = line.replace("SocketServer","socketserver")
        print(green+"Line "+str(linenum)+":"+" Converted SocketServer function")


      if line.count("repr") > 0:
        line = line.replace("repr","reprlib")
        print(green+"Line "+str(linenum)+":"+" Converted repr function")
        

      if line.count("test.test_support") > 0:
        line = line.replace("test.test_support","test_support")
        print(green+"Line "+str(linenum)+":"+" Converted test.test_support function")
      

      if line.count("exit") > 0:
        if(line.count("{exit") > 0):
          pass
        elif(line.count(" exit()")):
          print(red+"Line "+str(linenum)+":"+" The builtin function exit() has been removed from python 3 and has been moved to the sys library, please see",filename, "for more info")
          fixes.append("add_exit")
        
      
      if line.count("execfile()") > 0:
        print(red+"Line "+str(linenum)+":"+" The execfile() function has been removed from python 3, please see",filename, "for more info")
        solution = PVC.solutions("exexfile")
        codefix.write("Line "+str(linenum)+":"+solution+"\n\n")
      


      if line.count("reload") > 0:
        line = line.replace("reload","importlib.reload")
        print(green+"Line "+str(linenum)+":"+" Converted reload() function")
        print(red+"Line "+str(linenum)+":"+" The builtin function reload() has been removed from python 3 and has been moved to the importlib library, please see",filename, "for more info")
        fixes.append("add_reload")
      

      if line.count("reduce") > 0:
        line = line.replace("reduce","functools.reduce")
        print(green+"Line "+str(linenum)+":"+" Converted reduce() function")
        print(red+"Line "+str(linenum)+":"+" The builtin function reduce() has been removed from python 3 and has been moved to the functools library, please see",filename, "for more info")
        fixes.append("add_reduce")


      if line.count("intern") > 0:
        line = line.replace("intern","sys.intern")
        print(green+"Line "+str(linenum)+":"+" Converted intern() function")
        print(red+"Line "+str(linenum)+":"+" The builtin function intern() has been removed from python 3 and has been moved to the sys library, please see",filename, "for more info")
        fixes.append("add_intern")

      if line.count("generate_tokens") > 0:
        line = line.replace("generate_tokens","tokenize")
        print(green+"Line "+str(linenum)+":"+" Converted generate_tokens() function")
        print(red+"Line "+str(linenum)+":"+" The builtin function generate_tokens() has been removed from python 3 and the tokenize() function has been added in its place, please see",filename, "for more info")
        fixes.append("add tokenize")

      writefile.write(line)

    writefile.close()

    print(yellow+"\nAdding automatic fixes...")
    for solution in fixes:
      print(solution)
      PVC.autofixadd(fileoutput, add, solution)
    print("Fixes added\n")
    time.sleep(1)
    print("Testing for errors in converted code...")
    time.sleep(1)
    test = PVC.py3test(open(fileoutput).read())
    if not test:
      os.rename(fileoutput,filenamev2)
      errormessage = "Syntax error found, please see,filename,for more info."
      print(errormessage)
      
    elif(os.stat(filename).st_size == 0):
      os.remove(filename)
      os.rename(fileoutput,filenamev2)
      errormessage = "No errors found your code is good to go!"
      print(errormessage)
    
    print("\nFinished.")


PVC.convert()