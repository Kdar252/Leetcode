class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        card_count = Counter(hand)
        
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)
        
        while min_heap:
            first_card = min_heap[0]
            
            for card in range(first_card, first_card + groupSize):
                if card_count[card] == 0:
                    return False
                card_count[card] -= 1
                
                if card_count[card] == 0:
                    if card != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        
        return True