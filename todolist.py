Dolist{
Donetask=[]
Ongoingtask=[] 
}
Place=Input(“enter ur takes for today separated by a comma: “).split (“ , “)
For job in Place :
Print (job)
Do=Input(“did u finish + {Place}already ? “).captaliz
If Do==“Yes”:
 Donetask.append (Do)
 Print(“Nice Job “) 
else :
 Ongoingtask.append (Do)
 Print (“ok! try to not put it off“)
Print (“———“)

Thelist=Input (“do u want to see ur today progress?(yes, no) “).lower
if Thelist==“yes”
 Print (Dolist)
else :
 Print (“ok! “)