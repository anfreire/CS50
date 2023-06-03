import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]

'''
    Probability of a gene mutation
'''
MUTATION = {
    False: 1 - PROBS["mutation"],
    True: PROBS["mutation"]
}


'''
    Probability of passing a gene to a child given the number of genes the parent has
'''
PASS_THE_GENE = {
    0: MUTATION[True],
    1: (0.5 * MUTATION[True]) + (0.5 * MUTATION[False]),
    2: MUTATION[False]
}

def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    def get_parents(person):
        '''
            Return the parents of a person if they exist
            Return None if they don't exist
        '''
        father = people[person]["father"]
        mother = people[person]["mother"]
        if father in people.keys() and mother in people.keys():
            return father, mother
        else:
            return None, None
        
    def get_gene(person):
        '''
            Return the number genes we assume a person has
        '''
        if person in two_genes:
            return 2
        elif person in one_gene:
            return 1
        else:
            return 0
        
    def get_trait(person):
        '''
            Return the trait we assume a person has
        '''
        if person in have_trait:
            return True
        else:
            return False
        
    def get_probability(person):
        '''
            Return the probability of a person having a certain number of genes and a certain trait
            If the person has no parents, return the unconditional probability of haveing the assumed number of genes and trait
            If the person has parents, return the conditional probability of having the assumed number of genes and trait given the number of genes the parents have
        '''
        person_gene = get_gene(person)
        person_trait = get_trait(person)
        father, mother = get_parents(person)
        if father == None and mother is None:
            return PROBS["gene"][person_gene] * PROBS["trait"][person_gene][person_trait]
        else:
            father_gene = get_gene(father)
            mother_gene = get_gene(mother)
            father_pass = PASS_THE_GENE[father_gene]
            mother_pass = PASS_THE_GENE[mother_gene]
            probability = 1
            if person_gene == 0:
                probability *= (1 - father_pass) * (1 - mother_pass)
            elif person_gene == 1:
                probability *= (father_pass * (1 - mother_pass)) + ((1 - father_pass) * mother_pass)
            else:
                probability *= father_pass * mother_pass
            probability *= PROBS["trait"][person_gene][person_trait]
            return probability
    probability = 1
    for person in people:
        '''
            Iterate over all people and gett the probability of a person having a certain number of genes and a certain trait
            Making the joint probability by multiplying all the probabilities
        '''
        probability *= get_probability(person)
    return probability
        

def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        '''
            Iterate over all people and update their probabilities by:
            Adding the joint probability to the probability of a person having a certain number of genes and a certain trait
        '''
        gene = 0
        if person in one_gene:
            gene = 1
        elif person in two_genes:
            gene = 2
        if person in have_trait:
            trait = True
        else:
            trait = False
        probabilities[person]["gene"][gene] += p
        probabilities[person]["trait"][trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities:
        '''
            Iterate over all people and normalize their probabilities by:
            Dividing the probability of a person having a certain number of genes and a certain trait by the sum of all probabilities of a person having a certain number of genes and a certain trait
        '''
        gene_sum = probabilities[person]["gene"][0] + probabilities[person]["gene"][1] + probabilities[person]["gene"][2]
        trait_sum = probabilities[person]["trait"][True] + probabilities[person]["trait"][False]
        for gene in probabilities[person]["gene"]:
            probabilities[person]["gene"][gene] /= gene_sum
        for trait in probabilities[person]["trait"]:
            probabilities[person]["trait"][trait] /= trait_sum




        


if __name__ == "__main__":
    main()
