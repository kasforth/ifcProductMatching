from matchIfcProduct import IfcProductMatches

# set the name of the IfcProduct (here the IfcMaterial concrete)
# and the dataset list for matching (filtered from any database)
ifcProductName = "concrete"
filtereddatabase = ["cement", "brick", "rigid insulation"]

# set the name of the chosen LLM
llm_name = "bert-base-uncased"

# calculate the cosine similarities and return sorted dictionary with the most similar match and its scores
ifcProductMatches = IfcProductMatches(ifcProductName, filtereddatabase, llm_name)
matchDict = ifcProductMatches.matchingdict
maxSimMatch = ifcProductMatches.maxSimMatch
maxSimScore = ifcProductMatches.maxSimScore
print(maxSimMatch, maxSimScore)
