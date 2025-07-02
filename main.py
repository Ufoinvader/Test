nouvelle_campagne = {
"responsable_de_campagne": "Jeanne d'Arc",
"nom_de_campagne": "Campagne nous aimons les chiens",
"date_de_début": "01/01/2020",
"influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}

taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2

taux_de_conversion = dict()
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2

infos_labradoodle = {
    "poids": "13 à 16 kg",
    "origine": "États-Unis"
}

infos_labradoodle['nom_scientifique'] = "Canis lupus familiaris"

print(infos_labradoodle)

print("poids" in infos_labradoodle)

print("race" in infos_labradoodle)


nom_contact = "Jackson"
contact_infos = {"nom": "Jackson", "prenom": "Michael", "telephone": "123-456-7890", "email": "j.michael@email.com"}
print(contact_infos["email"])
contact_infos["email"] = "jackson.michael@email.com"
print(contact_infos["email"])
contacts = []
contacts.append(contact_infos)
print(contacts)
print(len(contacts))