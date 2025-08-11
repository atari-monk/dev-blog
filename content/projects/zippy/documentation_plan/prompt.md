## Template

C:\Atari-Monk-Art\dev-blog\content\templates\class-documentation.md

```md
# Class_name Documentation (High level overview)

## Functionality

- 

## Implementation

### Public methods

#### Constructor

- 

#### Method name

- 

### Private methods

- 
```

## Example of valid documentation

C:\Atari-Monk-Art\dev-blog\content\projects\zippy\documentation\input\keyboard-system.md

```md
# Keyboard System Documentation (High level overview)

## Functionality

- Stores and updates keys state.  
  Key is down or not.

## Implementation

### Public methods

#### Constructor

- Inits keys map.
- Stores event handler refs and binds them to this.
- Registers handlers to events.

#### IsKeyDown

- Takes key symbol, returns key state.

#### Destroy

- Removes handlers form events.

### Private methods

#### setupEventListeners

- Registers handlers to events.

#### handleKeyDown

- Sets key state down.

#### handleKeyUp

- Sets key state up.
```

## Code