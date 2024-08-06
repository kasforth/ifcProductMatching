from sentence_transformers import SentenceTransformer, util

class IfcProductMatches:
    def __init__(self, ifcProductName, filtereddatabase, llm_name):
        self.matchingdict = self.matchIfcProduct(ifcProductName, filtereddatabase, llm_name)
        self.maxSimMatch = list(self.matchingdict.keys())[0]
        self.maxSimScore = list(self.matchingdict.values())[0]

    def matchIfcProduct(self, ifcProductName, filtereddatabase, llm_name):
        matchingdict = {}

        # load the LLM using SentenceTransfomers and encode the IfcProductName using the respective LLM
        llm = SentenceTransformer(llm_name)
        encodingIfc = llm.encode(ifcProductName)

        # iterate over all filtered datasets and encode them, calculate the cosine similarity of each with the IfcProduct
        # and save the result in a Matching Dictionary
        for dataset in filtereddatabase:
            encodingDataset = llm.encode(dataset)
            cosinesimilarity = float(util.cos_sim(encodingIfc, encodingDataset))
            matchingdict[dataset] = cosinesimilarity

        #sort the Matching Dictionary according to its highest Cosine similarity
        matchingdict = dict(sorted(matchingdict.items(), key=lambda kv: kv[1], reverse=True))
        return matchingdict