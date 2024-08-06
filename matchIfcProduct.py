from sentence_transformers import SentenceTransformer, util

class IfcProductMatches:
    def __init__(self, ifcProductName, filtereddatabase, llm_name):
        self.matchingdict = self.matchIfcProduct(ifcProductName, filtereddatabase, llm_name)
        self.maxSimMatch = self.matchingdict[0]

    def matchIfcProduct(self, ifcProductName, filtereddatabase, llm_name):
        matchingdict = {}
        llm = SentenceTransformer(llm_name)

        #encode the IfcProductName using the respective LLM
        encodingIfc = llm.encode(ifcProductName)

        #iterate over all filtered datasets, calculate the cosine similarity of each with the IfcProduct and save the result in a Matching Dictionary
        for dataset in filtereddatabase:
            encodingDataset = llm.encode(dataset)
            cosinesimilarity = float(util.cos_sim(encodingIfc, encodingDataset))
            matchingdict[dataset] = cosinesimilarity

        #sort the Matching Dictionary according to its highest Cosine similarity
        matchingdict = dict(sorted(matchingdict.items(), key=lambda kv: kv[1], reverse=True))
        return matchingdict