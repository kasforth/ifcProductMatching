from matchIfcProduct import IfcProductMatches
from sentence_transformers import SentenceTransformer

def main():
    # set the name of the IfcProduct (here the IfcMaterial concrete)
    # and the dataset list for matching (filtered from any database)
    ifcProductName = "concrete"
    filtereddatabase = ["cement", "brick", "rigid insulation"]

    # set the name of the chosen LLM and load the LLM using SentenceTransfomers
    llm_name = "bert-base-uncased"
    llm = SentenceTransformer(llm_name)

    # calculate the cosine similarities and return sorted dictionary with the most similar match and its scores
    ifcProductMatches = IfcProductMatches(ifcProductName, filtereddatabase, llm)
    matchDict = ifcProductMatches.matchingdict
    maxSimMatch = ifcProductMatches.maxSimMatch
    maxSimScore = ifcProductMatches.maxSimScore
    print(f"The most similar dataset of the IfcProduct {ifcProductName} is " + maxSimMatch)
    print(f"The cosine similarity score of the maximum similar match is " + str(maxSimScore))

if __name__ == '__main__':
    main()