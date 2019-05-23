# pythoncards
pythoncards is a very small and simple library that can be used to create and manipulate playing card deck objects.

## Quick Start
pythoncards is composed of one file containing a class named Deck that can create, you guessed it, card deck objects.
To get started you're gonna have to do some importing. Here are a few different ways to import the library for use, pick whichever you prefer.

```python
import pythoncards  # Imports the whole pythoncards library which only contains 1 file containing 1 class.
newDeck = pythoncards.Deck('name of deck')
```

```python
from pythoncards import Deck  # Only imports the Deck class from the library.
newDeck = Deck('name of deck')
```

### Methods and Attributes

The "Deck" class has a few attributes and methods that are similar to an actual deck of playing cards.

`deck = Deck('example', 2, True)  # This object variable will be used for example purposes`

 Attributes | Purpose | Code
 --- | :---: | :---:
Name | Name of the deck | `deck.name  # => 'example'`
Contents | List of card objects in the deck | `deck.content  # => [Card(), Card()...]`
Discard Pile | Deck object containing discarded cards | `deck.discard  # => Deck('"example"_discard', 0)`

```python
newDeck = pythoncards.Deck('name of deck')

newDeck.name  # Gets the name of the deck object.
newDeck.deck  # Gets the contents of the deck object in a list.
```
