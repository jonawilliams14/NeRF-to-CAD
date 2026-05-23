import sys

from coffee_nerf_cad.cli import main

if __name__ == "__main__":
    sys.argv.insert(1, "example")
    main()
