import random
T="Hello, World!"
GENES=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,!."
def fitness(ind): return sum(a==b for a,b in zip(ind,T))
def create(): return "".join(random.choice(GENES) for _ in range(len(T)))
def evolve(pop=200):
    p=[create() for _ in range(pop)]
    for g in range(500):
        sc=sorted([(fitness(i),i) for i in p],reverse=True)
        if g%100==0: print(f"  Gen {g}: fit={sc[0][0]}")
        if sc[0][0]==len(T): print(f"  Solved gen {g}!"); return
        sv=[i for _,i in sc[:pop//10]]; p=[]
        while len(p)<pop:
            a,b=random.sample(sv,2); c=random.randint(0,len(a)-1)
            ch=a[:c]+b[c:]; ch="".join(random.choice(GENES) if random.random()<0.05 else x for x in ch)
            p.append(ch)
def main():
    random.seed(42); print("GENETIC ALGORITHM"); evolve()
if __name__=="__main__": main()
