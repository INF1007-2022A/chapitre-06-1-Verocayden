#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = []
        values_nb = []
        values_str = []
        while len(values) < 10:
            values.append(input("Veillez entrer une valeur: "))

        for element in values: # Separer valeurs numeriques VS alpha.
            if element.isdigit():
                values_nb.append(float(element))
            elif type(element) == str:
                values_str.append(element)

        sorted(values_nb)
        sorted(values_str)

        print(values_nb)
        print(values_str)
    return values_nb, values_str


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        mot1 = input("Entrez un mot: ").split()
        mot2 = input("Entrez un autre mot: ").split()
        if sorted(mot1) == sorted(mot2):
            print("Ce sont des anagrammes")
            return True
        return False


def contains_doubles(liste) -> bool:
    # Transform list into set (without doubles) and the lengths.
    if len(set(liste)) == len(liste): # No doubles
        return False
    else: # Contains doubles
        return True

"""
OTHER SOLUTION
compare = []
    for item in list:
        if item in compare:
            return True
        compare.append(item)

    return False
"""


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    dict_best = {}
    for student in student_grades:
        total = 0
        for grade in student_grades[student]:
            total += grade
        average = total / len(student_grades[student])
        student_grades[student] = round(average)
    best_grade = max(student_grades.values())
    for student in student_grades:
        if student_grades[student] == best_grade:
            dict_best = {student: best_grade}
    return dict_best


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    phrase = input("Entrez une phrase: ")
    histogramme = {}
    new_histogramme = {}
    for letter in phrase:
        if letter.isalpha():
            if letter not in histogramme:
                histogramme[letter] = 1
            elif letter in histogramme:
                histogramme[letter] += 1
    for letter in histogramme:
        if histogramme[letter] >= 5:
            new_histogramme[letter] = histogramme[letter]
    sorted(new_histogramme.values())
    print(new_histogramme)
    return new_histogramme


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name = input("Écrivez le nom de la recette : ").upper()
    ingredients = (input("Écrivez les ingrédients (séparés par un espace): ").upper()).split()
    dict = {name: ingredients}
    print(dict)
    return dict


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom = (input("Écrivez le nom de la recette à afficher: ")).upper()
    if nom in ingredients:
        print(nom, ingredients[nom])


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    # order()

    print(f"On vérifie les anagrammes...")
    # anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
