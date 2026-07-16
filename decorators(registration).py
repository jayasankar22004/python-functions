def register_validator(func):
    uns=[]
    def inner(ur,age,psd):
        nonlocal uns
        if us not in uns:
            sp = ['@','*','!','#','$','%','&','_','-','=','+','/']
            if len(psd) >= 8:
                up = list(filter(lambda x: x.isupper(), psd))
                sc = list(filter(lambda x: x in sp, psd))
                dg = list(filter(lambda x: x.isdigit(), psd))

                print(up, sc, dg, sep='\n')

                if up and sc and dg:
                    print("Strong Password")
                    if age > 18:
                        
                         func(us,psd,age)
                else:
                    print("Weak Password")
            else:
                print("password must contain 8 characters")
            return inner

        return inner
@register_validator
def register(ur,age,psd):
    print("registration success")
print()
