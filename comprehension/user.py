usernames=["admin","charan","root","guest","developer"]
result={ i:"valid" if len(i)>=5 else "invalid" for i in usernames}
print(result)