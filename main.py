from matchIfcProduct import IfcProductMatches

ifcProduct = "concrete"
filtereddatabase = ["cement", "brick"]
llm_name = "google-bert/bert-base-uncased"

ifcProductMatches = IfcProductMatches(ifcProduct, filtereddatabase, llm_name)
maxSimMatch = ifcProductMatches.maxSimMatch
matchDict = ifcProductMatches.matchingdict
print(maxSimMatch)
