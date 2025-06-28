# The AICHALLENGE Gym environment

This is the repository of the AIChallenge Gym environment.

## Quickstart

```bash
git clone https://github.com/toki-1441/aichallenge_gym.git
cd aichallenge_gym
pip install -e .
```

Then you can run a quick waypoint follow example by:
```bash
cd examples
python3 waypoint_follow.py
```
## Known issues
- Library support issues on Windows. You must use Python 3.8 as of 10-2021
- On MacOS Big Sur and above, when rendering is turned on, you might encounter the error:
```
ImportError: Can't find framework /System/Library/Frameworks/OpenGL.framework.
```
You can fix the error by installing a newer version of pyglet:
```bash
$ pip3 install pyglet==1.5.20
```
And you might see an error similar to
```
f110-gym 0.2.1 requires pyglet<1.5, but you have pyglet 1.5.20 which is incompatible.
```
which could be ignored. The environment should still work without error.

## thanks
[F1tenth gym](https://github.com/f1tenth/f1tenth_gym.git)
