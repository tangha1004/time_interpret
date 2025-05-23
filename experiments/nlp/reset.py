import os
import shutil


def main():
    with open("results.csv", "w") as fp:
        fp.write(
            "Dataset,Model,Explainer,LogOdds,Comprehensiveness,Sufficiency\n"
        )

    if os.path.exists("lightning_logs"):
        shutil.rmtree("lightning_logs")


if __name__ == "__main__":
    main()
