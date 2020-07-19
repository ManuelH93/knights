from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Version 1 - no output

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

knowledge1 = And(
    And(Or(AKnave, AKnight), Not(And(AKnave, AKnight))),
    And(Or(BKnave, BKnight), Not(And(BKnave, BKnight))),
    Or(
        Biconditional(AKnight, And(AKnight, BKnight)),
        Biconditional(AKnave, And(AKnave, BKnight))
    ),    
    Or(
        Biconditional(BKnight, And(AKnave, BKnight)),
        Biconditional(BKnave, And(AKnave, BKnave))
    )
)

# Version 2 - no output

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    And(Or(AKnave, AKnight), Not(And(AKnave, AKnight))),
    And(Or(BKnave, BKnight), Not(And(BKnave, BKnight))),
    Or(
        Biconditional(AKnight, And(AKnight, BKnight)),
        And(
            Implication(AKnave, Not(And(AKnight, BKnight))),
            Biconditional(AKnave, And(AKnave, AKnight))
        )
    ),    
    Or(
        Biconditional(BKnight, And(AKnave, BKnight)),
        And(
            Implication(BKnave, Not(And(AKnave, BKnight))),
            Biconditional(BKnave, And(AKnave, BKnave))
        )
    )
)

# Version 3 - A is a Knave

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge3 = And(
    And(Or(AKnave, AKnight), Not(And(AKnave, AKnight))),
    And(Or(BKnave, BKnight), Not(And(BKnave, BKnight))),
    Or(
        Biconditional(AKnight, And(AKnight, BKnight)),
        And(
            Biconditional(AKnave, Not(And(AKnight, BKnight))),
            Biconditional(AKnave, And(AKnave, BKnight))
        )
    ),    
    Or(
        Biconditional(BKnight, And(AKnave, BKnight)),
        And(
            Biconditional(BKnave, Not(And(AKnave, BKnight))),
            Biconditional(BKnave, And(AKnave, BKnave))
        )
    )
)

# Version 4 - no output

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge4 = And(
    And(Or(AKnave, AKnight), Not(And(AKnave, AKnight))),
    And(Or(BKnave, BKnight), Not(And(BKnave, BKnight))),
    Or(
        Biconditional(AKnight, BKnight),
        Biconditional(AKnave, BKnight)
    ),    
    Or(
        Biconditional(BKnight, AKnave),
        Biconditional(BKnave, AKnave)
    )
)


# Version 5

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge5 = And(
    And(Or(AKnave, AKnight), Not(And(AKnave, AKnight))),
    And(Or(BKnave, BKnight), Not(And(BKnave, BKnight))),
    Or(
        And(
            Biconditional(AKnight, BKnight),
            Not(BKnave)
        ),
        Biconditional(AKnave, BKnight)
    ),   
    Or(
        And(
            Biconditional(BKnight, AKnave),
            Not(AKnight)
        ),
        Biconditional(BKnave, AKnave)
    )
)


print(model_check(knowledge3, AKnave))


