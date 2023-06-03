from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

'''
    Here is defined the knowledge base for the puzzle.
    The knowledge base is a conjunction of the possibilities for each character.
    The possibilities are defined by the following rules:
        - A Knight is a person who always tells the truth.
        - A Knave is a person who always lies.
        - A Knight and a Knave cannot be the same person.
    To represent the above rules, we use the following clauses:
        - Or(AKnight, AKnave): A can be a Knight or a Knave.
        - Biconditional(AKnight, Not(AKnave)): A is a Knight if and only if A is not a Knave.
        - Or(BKnight, BKnave): B can be a Knight or a Knave.
        - Biconditional(BKnight, Not(BKnave)): B is a Knight if and only if B is not a Knave.
        - Or(CKnight, CKnave): C can be a Knight or a Knave.
        - Biconditional(CKnight, Not(CKnave)): C is a Knight if and only if C is not a Knave.
'''
knowledgeBase = And(
    Or(AKnight, AKnave),
    Biconditional(AKnight, Not(AKnave)),
    Or(BKnight, BKnave),
    Biconditional(BKnight, Not(BKnave)),
    Or(CKnight, CKnave),
    Biconditional(CKnight, Not(CKnave)),
)

# Puzzle 0
# A says "I am both a knight and a knave."
'''
    To represent the above statement, we use the following clauses:
        - And(AKnight, AKnave): A is a Knight and a Knave.
    To apply the above clauses to the knowledge base, we use the following rules:
        - Biconditional(AKnight, And(AKnight, AKnave)): If A is a Knight, then A is a Knight and a Knave.
        
'''
knowledge0 = And(
    knowledgeBase,
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
'''
    To represent the above statements, we use the following clauses:
        - And(AKnave, BKnave): A and B are both Knaves.
    To apply the above clauses to the knowledge base, we use the following rules:
        - Biconditional(AKnight, And(AKnave, BKnave)): If A is a Knight, then A and B are both Knaves.
'''
knowledge1 = And(
    knowledgeBase,
    Biconditional(AKnight, And(AKnave, BKnave)),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
'''
    To represent the above statements, we use the following clauses:
        - Or(And(AKnight, BKnight), And(AKnave, BKnave)): A and B are the same kind.
        - Or(And(AKnight, BKnave), And(AKnave, BKnight)): A and B are of different kinds.
    To apply the above clauses to the knowledge base, we use the following rules:
        - Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))): If A is a Knight, then A and B are the same kind.
        - Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))): If B is a Knight, then A and B are of different kinds.
'''
knowledge2 = And(
    knowledgeBase,
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
'''
    To represent the above statements, we use the following clauses:
        - Or(AKnight, AKnave): A can be a Knight or a Knave.
        - AKnave: A is a Knave.
        - CKnave: C is a Knave.
        - AKnight: A is a Knight.
    To apply the above clauses to the knowledge base, we use the following rules:
        - Biconditional(AKnight, Or(AKnight, AKnave)): If A is a Knight, then A can be a Knight or a Knave.
        - Biconditional(BKnight, AKnave): If B is a Knight, then A is a Knave.
        - Biconditional(BKnight, CKnave): If B is a Knight, then C is a Knave.
        - Biconditional(CKnight, AKnight): If C is a Knight, then A is a Knight.
'''
knowledge3 = And(
    knowledgeBase,
    Biconditional(AKnight, Or(AKnight, AKnave)),
    Biconditional(BKnight, AKnave),
    Biconditional(BKnight, CKnave),
    Biconditional(CKnight, AKnight),
)

'''
    There are several ways to solve this problem.
    We can only say this because of the knowledge base, that defines that Not(AKnight) is the same as AKnave, by using Or(AKnight, AKnave) and Biconditional(AKnight, Not(AKnave)).
    We could instead of Biconditional use Implication twice, but the second time we would have to use the other Symbol in the first argument and negate the second argument.
    E.g.:
    
        - Biconditional(AKnight, Or(AKnight, AKnave)): If A is a Knight, then A can be a Knight or a Knave.

        - Implication(AKnight, Or(AKnight, AKnave)): If A is a Knight, then A can be either a Knight or a Knave.
        - Implication(AKnave, Not(Or(AKnight, AKnave))): If A is a Knave, then A cannot be both a Knight and a Knave.
    
    We could not use Biconditional nor Implication, and approach the problem with just And, Or and Not.
    E.g.:

        - Biconditional(AKnight, Or(AKnight, AKnave)): If A is a Knight, then A can be a Knight or a Knave.

        - Implication(AKnight, Or(AKnight, AKnave)): If A is a Knight, then A can be either a Knight or a Knave.
        - Implication(AKnave, Not(Or(AKnight, AKnave))): If A is a Knave, then A cannot be both a Knight and a Knave.

        - And(Implication(AKnight, Or(AKnight, AKnave)), Implication(AKnave, Not(Or(AKnight, AKnave)))): If A is a Knight, then A can be either a Knight or a Knave. If A is a Knave, then A cannot be both a Knight and a Knave.
    
    Bicondionals in this context are very powerful, because it allows to make more clauses, and it is easier to translate them to code.

    One thing to notice is that i allways use the Knight for the first argument in the Biconditional, this is because we know for sure that the Knight does not lie, and we can use that to our advantage.
    After all its a true statement, and for all the clauses we can make out of a Biconditional, it is crucial on the performance that we have a true statement.
    By usign biconditional, we also state that Not(AKnight), a Knave, implies the Negated sentence of a Knight.
'''
def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
