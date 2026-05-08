Dolist = {
    "Donetask": [],
    "Ongoingtask": []
}

Place = input("Enter your tasks for today separated by a comma: ").split(",")

for job in Place:
    print(job)

    Do = input(f"Did you finish {job} already? ").capitalize()

    if Do == "Yes":
        Dolist["Donetask"].append(job)
        print("Nice Job")

    else:
        Dolist["Ongoingtask"].append(job)
        print("Ok! Try not to put it off")

print("--------")

Thelist = input("Do you want to see your today progress? (yes/no): ").lower()

if Thelist == "yes":
    print(Dolist)

else:
    print("Ok!")