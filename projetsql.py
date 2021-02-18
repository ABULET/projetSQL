def requete(question):
    requetes = {"En quelle année est sortie le film The Godfather ?":["SELECT startYear","FROM titles_basics","WHEN titles_basics.primaryTitle","LIKE 'The Godfather'","AND title_basics.tconst = 1;"],
                "En quelle année est sortie le premier film Superman ?":["SELECT startYear","FROM titles_basics","WHEN titles_basics.primaryTitle","LIKE 'Superman'","AND title_basics.tconst = 1;"],
                "Quel est le titre original du film 'Les dents de la mer' ?":["SELECT originalTitle","FROM title_basics","WHEN title_basics.primaryTitle","LIKE 'Les dents de la mer';"],
                "Quel est le métier d’Olivier Nakache ?":["SELECT primaryProfession","FROM name_basics","WHEN name_basics.primaryName","LIKE 'Olivier Nakache';"],
                "Quels sont les films d’Olivier Nakache ?":["SELECT primaryTitle","FROM title_basics","WHEN title_basics.tconst = title_principal.tconst","AND title_principal.characters","LIKE 'Olivier Nakache';"],
                "Quel est le film ayant recueilli le plus de votes ?":["SELECT primaryTitle","FROM title_basics","WHEN title_basics.tconst = title_ratings.tconst","AND title_rating.numVotes = max(title_ratings.nimVotes);"],
                "Qui a écrit le scénario du film Taxi sorti en 1998 ?":["SELECT writers","FROM title_writers","WHEN title_writers.tconst = title_basics.tconst","AND title_basics.primaryTitle","LIKE 'Taxi","AND title_basics.startYear = 1998;"]}
    for i in range(len(requetes[question])):
        print(requetes[question][i])



requete("Qui a écrit le scénario du film Taxi sorti en 1998 ?")