students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

chosen_name = input("Entrez le nom de l’étudiant : ")
if chosen_name in students:
    print(f"Les notes de {chosen_name} sont :")
    for subject, grade in students[chosen_name].items():
        print(f"{subject} : {grade}")
    moyenne = int(sum(students[chosen_name].values()) / len(students[chosen_name]))
    print(f"La moyenne de {chosen_name} est : {moyenne}")
else:
    print(f"L'étudiant {chosen_name} n'existe pas dans la liste.")
