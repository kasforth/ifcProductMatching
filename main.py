from matchIfcProduct import IfcProductMatches

ifcProduct = "brick"
filtereddatabase = ["concrete", "masonary"]
llm_name = "google-bert/bert-base-uncased"

ifcProductMatches = IfcProductMatches(ifcProduct, filtereddatabase, llm_name)
maxSimMatch = ifcProductMatches.maxSimMatch
matchDict = ifcProductMatches.matchingdict
print(maxSimMatch)
