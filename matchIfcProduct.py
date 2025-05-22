from sentence_transformers import util
import re

class IfcProductMatches:
    def __init__(self, ifcProductName, filtereddatabase, llm):
        self.matchingdict = self.matchIfcProduct(ifcProductName, filtereddatabase, llm)
        self.maxSimMatch = list(self.matchingdict.keys())[0]
        self.maxSimScore = list(self.matchingdict.values())[0]

    def matchIfcProduct(self, ifcProductName, filtereddatabase, llm):
        matchingdict = {}

        # encode the IfcProductName using the respective LLM
        encodingTermIfcProduct = llm.encode(ifcProductName)

        # iterate over all filtered datasets and encode them, calculate the cosine similarity of each term with the IfcProduct
        for dataset in filtereddatabase:
            encodingTermDataset = llm.encode(dataset)
            termCosSim = float(util.cos_sim(encodingTermIfcProduct, encodingTermDataset))

            # calculate cosine similarity of tokenized datasets and tokenized IfcProduct
            tokenCosSim = []
            for token_ifcProduct in re.split(r"[ :\-_]", ifcProductName):
                for token_dataset in re.split(r"[ :\-_]", dataset):
                    tokenCosSimtemp = float(util.cos_sim(llm.encode(token_ifcProduct), llm.encode(token_dataset)))
                    tokenCosSim.append(tokenCosSimtemp)

            # select the maximum cosine similarity of whole expression/ term or tokenized and save in dictionary
            if max(tokenCosSim) < termCosSim:
                matchingdict[dataset] = termCosSim
            else:
                matchingdict[dataset] = max(tokenCosSim)

        # sort the Matching Dictionary according to its highest cosine similarity
        matchingdict = dict(sorted(matchingdict.items(), key=lambda kv: kv[1], reverse=True))
        return matchingdict
