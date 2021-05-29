#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json


# In[2]:


#df = pd.read_csv("data\extracted_data.csv",header=None)
df_wai = pd.read_csv("data\weighted_average_index.csv")
indices = df_wai.to_dict()
indices['NA'] = {0:0}


# In[3]:


class WeightedAverageBasedDiagnosticEngine:
    
    ENGINE_NAME = 'Weighted-Average'
    
    def get_weighted_average(self,data):
        result = {}
        diagnosis = {}
        person_data = [json.loads(idx.replace("'", '"')) for idx in data]
        diag_conf_ind = 0
        c = 0
        for col in person_data[0]:
            try:
                sentiment = col['traits']['wit$sentiment'][0]['value']
                c = c+1
            except KeyError:
                sentiment = 'NA'
            diag_conf_ind = diag_conf_ind + indices[sentiment][0]
        if c != 0:
            diag_conf_ind = diag_conf_ind/c
        if (diag_conf_ind < 0):
            diagnosis['condition'] = 'true'
            diagnosis['ailment'] = 'depression'
            diagnosis['confidence'] = abs(diag_conf_ind)
            result['diagnosis'] = diagnosis
        else:
            diagnosis['condition'] = 'false'
            diagnosis['confidence'] = diag_conf_ind
            result['diagnosis'] = diagnosis
        return result


# In[4]:


'''text = ['[{ "text": "I have self doubt and look for human validation and feel confidentless", "intents": [ { "id": "328072262060613", "name": "derive_self_concept", "confidence": 0.9978 } ], "entities": { "concern:concern": [ { "id": "298701508600404", "name": "concern", "role": "concern", "start": 7, "end": 70, "body": "self doubt and look for human validation and feel confidentless", "confidence": 0.6675, "entities": [], "suggested": true, "value": "self doubt and look for human validation and feel confidentless", "type": "value" } ], "relation:relation": [ { "id": "399088171152908", "name": "relation", "role": "relation", "start": 0, "end": 1, "body": "I", "confidence": 0.9704, "entities": [], "value": "self", "type": "value" } ] }, "traits": {} },{"text":"Very anxious and hopeless.","intents":[{"id":"328072262060613","name":"derive_self_concept","confidence":0.7745}],"entities":{"self_description:handling_criticism":[{"id":"223931532538253","name":"self_description","role":"handling_criticism","start":5,"end":12,"body":"anxious","confidence":1,"entities":[],"value":"anxious","type":"value"},{"id":"223931532538253","name":"self_description","role":"handling_criticism","start":17,"end":25,"body":"hopeless","confidence":1,"entities":[],"value":"hopeless","type":"value"}]},"traits":{"wit$sentiment":[{"id":"5ac2b50a-44e4-466e-9d49-bad6bd40092c","value":"negative","confidence":0.6568}]}},{"text":"Not thriving. Mentally exhausted and lacking motivation. It definitely does get hard to keep pushing when everything in a sense is virtual and ambiguous.","intents":[{"id":"328072262060613","name":"derive_self_concept","confidence":0.9785}],"entities":{"concern:concern":[{"id":"298701508600404","name":"concern","role":"concern","start":0,"end":55,"body":"Not thriving. Mentally exhausted and lacking motivation","confidence":0.9258,"entities":[],"suggested":true,"value":"Not thriving. Mentally exhausted and lacking motivation","type":"value"}]},"traits":{"wit$sentiment":[{"id":"5ac2b50a-44e4-466e-9d49-bad6bd40092c","value":"negative","confidence":0.6318}]}},{"text":"Some days i do feel trouble falling asleep","intents":[{"id":"524483275590042","name":"derive_concern","confidence":0.9414}],"entities":{"concern:concern":[{"id":"298701508600404","name":"concern","role":"concern","start":12,"end":42,"body":"do feel trouble falling asleep","confidence":0.5053,"entities":[],"suggested":true,"value":"do feel trouble falling asleep","type":"value"}],"relation:relation":[{"id":"399088171152908","name":"relation","role":"relation","start":10,"end":11,"body":"i","confidence":0.9208,"entities":[],"value":"self","type":"value"}]},"traits":{"wit$sentiment":[{"id":"5ac2b50a-44e4-466e-9d49-bad6bd40092c","value":"negative","confidence":0.6363}]}},{"text":"overeating often","intents":[{"id":"524483275590042","name":"derive_concern","confidence":0.5971}],"entities":{"concern:positive_events":[{"id":"221512379783687","name":"concern","role":"positive_events","start":0,"end":10,"body":"overeating","confidence":1,"entities":[],"value":"overeating","type":"value"}]},"traits":{"wit$sentiment":[{"id":"5ac2b50a-44e4-466e-9d49-bad6bd40092c","value":"negative","confidence":0.6367}]}},{"text":"Not much motivation to do anything. It feels like a rut. nothing feels feasible most days.","intents":[{"id":"524483275590042","name":"derive_concern","confidence":0.7039}],"entities":{"concern:concern":[{"id":"298701508600404","name":"concern","role":"concern","start":0,"end":19,"body":"Not much motivation","confidence":0.9087,"entities":[],"suggested":true,"value":"Not much motivation","type":"value"}]},"traits":{}},{"text":"Physical health is average. I try to workout regularly. Atleast 15 min a day and at least 6 days a week.","intents":[{"id":"524483275590042","name":"derive_concern","confidence":0.5409}],"entities":{"relation:relation":[{"id":"399088171152908","name":"relation","role":"relation","start":28,"end":29,"body":"I","confidence":1,"entities":[],"value":"self","type":"value"}]},"traits":{"wit$sentiment":[{"id":"5ac2b50a-44e4-466e-9d49-bad6bd40092c","value":"neutral","confidence":0.6177}]}},{"text":"Yes. This has been one of my most prevalent problems lately. I just try isolating myself or breakdown into tears. Blaming one self is also a coping mechanism.","intents":[{"id":"328072262060613","name":"derive_self_concept","confidence":0.8384}],"entities":{"concern:concern":[{"id":"298701508600404","name":"concern","role":"concern","start":29,"end":59,"body":"most prevalent problems lately","confidence":0.6554,"entities":[],"suggested":true,"value":"most prevalent problems lately","type":"value"}],"relation:relation":[{"id":"399088171152908","name":"relation","role":"relation","start":26,"end":28,"body":"my","confidence":0.9498,"entities":[],"value":"self","type":"value"},{"id":"399088171152908","name":"relation","role":"relation","start":61,"end":62,"body":"I","confidence":1,"entities":[],"value":"self","type":"value"},{"id":"399088171152908","name":"relation","role":"relation","start":82,"end":88,"body":"myself","confidence":1,"entities":[],"value":"self","type":"value"},{"id":"399088171152908","name":"relation","role":"relation","start":126,"end":130,"body":"self","confidence":1,"entities":[],"value":"self","type":"value"}]},"traits":{"wit$sentiment":[{"id":"5ac2b50a-44e4-466e-9d49-bad6bd40092c","value":"negative","confidence":0.7011}]}}]']

WeightedAverageBasedDiagnosticEngine.get_weighted_average(text)'''

