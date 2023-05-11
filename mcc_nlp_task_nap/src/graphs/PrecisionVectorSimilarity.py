from typing import List

from src.graphs.Precision import Precision
from src.tools.Tools import Tools


class PrecisionVectorSimilarity(Precision):

    def estimate_input(self, t: str, subset: List[str]) -> dict:
        emb = self.data_set.import_emb()[t]
        sum_frequency = Tools.suma_palablas(subset, emb)
        btc = emb.most_similar([sum_frequency], topn=20)
        result = Tools.convert_to_dict(btc)

        for w in subset:
            if w in result:
                result.pop(w)
        # result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        return result
