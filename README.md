# Asteroids

A small take on the classic arcade game *Asteroids*, written in Python with [pygame](https://www.pygame.org/). You fly a triangular ship, shoot the asteroids drifting in from the edges of the screen, and avoid getting hit.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- pygame 2.6.1 (installed for you below)

## Getting started

With uv:

```bash
uv sync          # create .venv and install pygame
uv run main.py   # start the game
```

With pip:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pygame==2.6.1
python main.py
```

## Controls

| Key     | Action         |
|---------|----------------|
| `W`     | Thrust forward |
| `S`     | Move backward  |
| `A`     | Rotate left    |
| `D`     | Rotate right   |
| `Space` | Shoot          |

Close the window to quit.

## Gameplay

- An asteroid spawns at a random screen edge every 0.8 seconds and comes in at a random speed and angle.
- Asteroids come in three sizes. When you shoot a large or medium asteroid, it breaks into two smaller, faster pieces. When you shoot a small one, it's destroyed.
- After each shot you have to wait 0.3 seconds before you can fire again.
- If an asteroid touches your ship, the game ends.

## Project structure

| File               | Purpose |
|--------------------|---------|
| `main.py`          | Entry point: sets up pygame and the sprite groups, runs the game loop, and checks for collisions |
| `circleshape.py`   | `CircleShape` base class (position, velocity, radius, circle collision) |
| `player.py`        | `Player` ship: drawing, movement, rotation, shooting |
| `shot.py`          | `Shot` projectile |
| `asteroid.py`      | `Asteroid` and its splitting logic |
| `asteroidfield.py` | `AsteroidField`, which spawns asteroids off-screen |
| `constants.py`     | Tunable values: screen size, speeds, radii, spawn rate, cooldown |
| `logger.py`        | Writes JSONL logs of game state and events for debugging |

## Tweaking the game

You can change all of the gameplay numbers in [`constants.py`](constants.py). For example:

- `PLAYER_SPEED`, `PLAYER_TURN_SPEED`: how fast the ship moves and turns
- `PLAYER_SHOOT_SPEED`, `PLAYER_SHOOT_COOLDOWN_SECONDS`: how fast shots travel and how often you can fire
- `ASTEROID_SPAWN_RATE_SECONDS`, `ASTEROID_KINDS`, `ASTEROID_MIN_RADIUS`: how often asteroids spawn and what sizes they come in

## Logs

While the game runs, `logger.py` writes two files to the working directory:

- `game_state.jsonl`: a snapshot of the sprites about once per second, covering the first ~16 seconds of play
- `game_events.jsonl`: events such as `asteroid_shot`, `asteroid_split`, and `player_hit`

Both files are overwritten each time you start the game.
