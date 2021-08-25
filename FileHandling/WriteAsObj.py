try:
    f=open("text.txt",'w',encoding="utf-8")

    f.write("With Object method ")
except:
    print("operation failed!!!")
finally:
     f=open("text.txt",'w',encoding="utf-8")
     f.close()