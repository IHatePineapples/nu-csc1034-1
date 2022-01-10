from . import panda

import argparse


def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument('--no_rotate', help="Suppress Rotation",
                        action="store_true")

    parser.add_argument('--scale', metavar='scale', type=float,
                        default=1, help='Scale the panda')

    parser.add_argument('--scene_scale', metavar='scene_scale',
                        type=float, default=1,
                        help='Scale the scene of the panda')

    parser.add_argument('--music', help="Add relaxing music",
                        action="store_true")

    parser.add_argument('--no_sound', help="Suppress sound",
                        action="store_true")


    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()
