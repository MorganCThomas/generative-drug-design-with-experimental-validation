import os
import sys
import pandas as pd


def main(csv):
    df = pd.read_csv(csv, index_col='Index')
    if os.path.basename(csv) == 'distribution_based.csv':
        for i, row in df.iterrows():
            print(
                f"""
### {i}. {row['Title']}

**Publication Date**: {row['Publication Date']}, {row['Year']} - [Paper Link]({row['Paper Link']})

**Target**: {row['Target']} - **Design Task**: {row['Design Task']}

**Model**: {row['Model']} (Input: {row['Input']}, Output: {row['Output']})

**Hit Rate**: {row['Hit Rate']}

**Outcome**: {row['Outcome']} - **Most Potent Design**: {row['Most Potent Design']}

**Notes**: {row['Notes']}

------------------------------------------------------------------------------------------------------------
            """
        )
    elif os.path.basename(csv) == 'goal_directed.csv':
        for i, row in df.iterrows():
            print(
                f"""
### {i}. {row['Title']}

**Publication Date**: {row['Publication Date']}, {row['Year']} - [Paper Link]({row['Paper Link']})

**Target**: {row['Target']} - **Design Task**: {row['Design Task']}

**Model**: {row['Model']} (Input: {row['Input']}, Output: {row['Output']})

**Optimization Algorithm Class**: {row['Optimization Algorithm Class']}

**Hit Rate**: {row['Hit Rate']}

**Outcome**: {row['Outcome']} - **Most Potent Design**: {row['Most Potent Design']}

**Notes**: {row['Notes']}

------------------------------------------------------------------------------------------------------------

            """
            )
    else:
        print("Unknown CSV")
        

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(
            f"Usage: python {sys.argv[0]} <csv file> \n"
        )
    else:
        main(sys.argv[1])
