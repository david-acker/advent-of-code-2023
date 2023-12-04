from typing import List, Tuple

from utils import is_letter
    

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()


    def _get_character_index(self, character: str) -> int:
        return ord(character) - ord('a')
    

    def insert(self, value: str) -> None:
        current_node = self.root

        for character in value:
            character_index = self._get_character_index(character)

            next_node = current_node.children[character_index]
            if next_node is None:
                next_node = TrieNode()
                current_node.children[character_index] = next_node
            
            current_node = next_node

        current_node.is_end_of_word = True
        current_node.word = value


    def search_prefix(self, value: str, offset = 0) -> Tuple[bool, str | None]:
        current_node = self.root

        for index, character in enumerate(value):
            if index < offset:
                continue

            if (not is_letter(character)):
                return (False, None)

            character_index = self._get_character_index(character)

            next_node = current_node.children[character_index]
            if next_node is None:
                return (False, None)
            
            current_node = next_node

            # Return immediately once we find a word
            if current_node.is_end_of_word:
                break

        return (current_node.is_end_of_word, current_node.word)
    

class TrieNode:
    is_end_of_word = False
    word: str | None = None


    def __init__(self) -> None:
        self.children: List[TrieNode | None]= [None for _ in range(26)]
