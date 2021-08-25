try:
        f=open("text.txt",'r',encoding="utf-8")
        for line in f:
            print(line,end='')
except:
        print("Operation Failed!!!!")
    
finally:
        f.close()