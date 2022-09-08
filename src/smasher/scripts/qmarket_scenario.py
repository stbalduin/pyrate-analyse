import os
import midas.api as mia


def main():
    scenario_path = os.path.abspath(
        os.path.join(
            __file__, "..", "..", "scenarios", "qmarket_mv.yml"
        )
    )

    mia.run("qmarket_mv", {}, scenario_path)


if __name__ == "__main__":
    main()
