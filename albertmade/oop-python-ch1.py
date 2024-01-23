"""
created by albertmade (24.1.22)

절차적으로 구현된 Higher or Lower

"""

import random

# 카드 상수 모음
SUIT_TUPLE = {"Spades", "Hearts", "Clubs", "Diamonds"}
RANKS_TUPLE = (
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
)
NCARDS = 8


def getCard(deckListIn):
    """입력받은 카드 덱에서 임의로 한장의 카드를 선택해 반환
    args:
        deckListIn(): TBD
    """
    thisCard = deckListIn.pop()
    return thisCard


def shuffle(deckListIn):
    """입력받은 카드 덱을 복사한 후 복사본을 무작위로 뒤섞어 반환
    args:
        deckListIn() : TBD
    """
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut


# 메인 코드 (아직 if __init__ == 그거 안쓰는 듯)

print("대충 게임 설명")
startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANKS_TUPLE):
        cardDict = {"rank": rank, "suit": suit, "value": thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict["rank"]
    currentCardValue = currentCardDict["value"]
    currentCardSuit = currentCardDict["suit"]
    print("뭐 그 ", currentCardRank, currentCardSuit)

# 계속 작성
