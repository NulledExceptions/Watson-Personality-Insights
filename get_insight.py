import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights


def analyze(handle):
    twitter_consumer_key = 'Ysy2YH2mecimBoj7BaUai7fcp'
    twitter_consumer_secret = 'XU6EMvXHROKxEJeF1l1kY0H8rxNeZlmV27TyK2WGMroj0DQirF'
    twitter_access_token = '816385551007944704-BtKafq5QB3DWieUI3r8NixEmjXpC5rJ'
    twitter_access_secret = 'CWTMvSPg1hVrPmFXXwsF2JlgdReoopXZCTOidDOeVqH8I'

    twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret,
                              access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)

    statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

    text = ""

    for status in statuses:
        if (status.lang == 'en'):
            text += status.text.encode('utf-8')

    pi_username = '78bc8f32-0a51-48f4-b33c-fa94f6ff81bb'
    pi_password = 'Sy1Oqw5Foe2r'

    personality_insights = PersonalityInsights(username=pi_username, password=pi_password)

    pi_result = personality_insights.profile(text)


    return pi_result


def flatten(orig):
    data = {}
    for c in orig['tree']['children']:
        if 'children' in c:
            for c2 in c['children']:
                if 'children' in c2:
                    for c3 in c2['children']:
                        if 'children' in c3:
                            for c4 in c3['children']:
                                if (c4['category'] == 'personality'):
                                    data[c4['id']] = c4['percentage']
                                    if 'children' not in c3:
                                        if (c3['category'] == 'personality'):
                                            data[c3['id']] = c3['percentage']
    return data


def compare(dict1, dict2):
    compared_data = {}
    for keys in dict1:
        if dict1[keys] != dict2[keys]:
            compared_data[keys] = abs(dict1[keys] - dict2[keys])


    return compared_data


user_handle="@Fanta_GB"
celebrity_handle="@shaq"

user_result=analyze(user_handle)
#celebrity_result=analyze(celebrity_handle)


user=flatten(user_result)
#celebrity=flatten(celebrity_result)
#compared_results=compare(user,celebrity)


#print user_result
#json=json.dumps(user_result, indent=4, sort_keys=False)


with open(user_handle+'.json', 'w') as outfile:
    json.dump(user_result, outfile)
#print(json.dumps(user_result, indent=4, sort_keys=False))
#print json['tree']
'''
for b in user_result['tree']['children']:
    print(b)
    #print b['children']
    for c in b['children']:
        #print c['children']
        for d in c['children']:
            #print d
            for e in d['children']:
                print e['name'] ,  e['percentage']
#for a in user_result['tree']['children']['children']:
    #print a
'''
'''
#print the keys:
for key in dic.iterkeys():
    print key
#print the values:
for value in dic.itervalues():
    print value
#print key and values
for key, value in dic.iteritems():
    print key, value
for b in user_result['tree']['children'] :
    #print(b)
    for trait in b:
        print trait
for key, value in user_result.iteritems():
    for a in user_result['tree']:
        for b in user_result['tree']['children'] :
            print b
for key, value
    print key
 warnings []
 tree {u'children': [{u'children': [{u'category': u'personality', u'percentage': 0.004385838407164611, u'children': [{u'category': u'personality', u'name': u'Openness', u'sampling_error': 0.0599949159, u'id': u'Openness', u'percentage': 0.8235281487828072, u'children': [{u'category': u'personality', u'percentage': 0.8035173430613427, u'id': u'Adventurousness', u'sampling_error': 0.0507683425, u'name': u'Adventurousness'}, {u'category': u'personality', u'percentage': 0.2718543865828507, u'id': u'Artistic interests', u'sampling_error': 0.1038704008, u'name': u'Artistic interests'}, {u'category': u'personality', u'percentage': 0.09473743625884407, u'id': u'Emotionality', u'sampling_error': 0.0475353859, u'name': u'Emotionality'}, {u'category': u'personality', u'percentage': 0.8626062198217859, u'id': u'Imagination', u'sampling_error': 0.06389646, u'name': u'Imagination'}, {u'category': u'personality', u'percentage': 0.9551019706175319, u'id': u'Intellect', u'sampling_error': 0.055758658, u'name': u'Intellect'}, {u'category': u'personality', u'percentage': 0.7673675517309637, u'id': u'Liberalism', u'sampling_error': 0.0833118639, u'name': u'Authority-challenging'}]}, {u'category': u'personality', u'name': u'Conscientiousness', u'sampling_error': 0.0757080248, u'id': u'Conscientiousness', u'percentage': 0.14333294241134875, u'children': [{u'category': u'personality', u'percentage': 0.6444366662374036, u'id': u'Achievement striving', u'sampling_error': 0.0983090136, u'name': u'Achievement striving'}, {u'category': u'personality', u'percentage': 0.3783425436604306, u'id': u'Cautiousness', u'sampling_error': 0.09149712630000001, u'name': u'Cautiousness'}, {u'category': u'personality', u'percentage': 0.24987859192943734, u'id': u'Dutifulness', u'sampling_error': 0.060043287699999996, u'name': u'Dutifulness'}, {u'category': u'personality', u'percentage': 0.4773451185441701, u'id': u'Orderliness', u'sampling_error': 0.069870773, u'name': u'Orderliness'}, {u'category': u'personality', u'percentage': 0.42072610964251733, u'id': u'Self-discipline', u'sampling_error': 0.046969884499999996, u'name': u'Self-discipline'}, {u'category': u'personality', u'percentage': 0.9222906385511389, u'id': u'Self-efficacy', u'sampling_error': 0.092088718, u'name': u'Self-efficacy'}]}, {u'category': u'personality', u'name': u'Extraversion', u'sampling_error': 0.056464097799999995, u'id': u'Extraversion', u'percentage': 0.42250424604587405, u'children': [{u'category': u'personality', u'percentage': 0.6830081402482564, u'id': u'Activity level', u'sampling_error': 0.0775239185, u'name': u'Activity level'}, {u'category': u'personality', u'percentage': 0.7618899935153339, u'id': u'Assertiveness', u'sampling_error': 0.0828944437, u'name': u'Assertiveness'}, {u'category': u'personality', u'percentage': 0.06781858464682894, u'id': u'Cheerfulness', u'sampling_error': 0.1045189718, u'name': u'Cheerfulness'}, {u'category': u'personality', u'percentage': 0.5879725172655705, u'id': u'Excitement-seeking', u'sampling_error': 0.08038827479999999, u'name': u'Excitement-seeking'}, {u'category': u'personality', u'percentage': 0.19181662064647964, u'id': u'Friendliness', u'sampling_error': 0.0748785557, u'name': u'Outgoing'}, {u'category': u'personality', u'percentage': 0.08328201386255152, u'id': u'Gregariousness', u'sampling_error': 0.0575809506, u'name': u'Gregariousness'}]}, {u'category': u'personality', u'name': u'Agreeableness', u'sampling_error': 0.09636118880000001, u'id': u'Agreeableness', u'percentage': 0.004385838407164611, u'children': [{u'category': u'personality', u'percentage': 0.1663474571725852, u'id': u'Altruism', u'sampling_error': 0.0702330067, u'name': u'Altruism'}, {u'category': u'personality', u'percentage': 0.13512155385299657, u'id': u'Cooperation', u'sampling_error': 0.07934973740000001, u'name': u'Cooperation'}, {u'category': u'personality', u'percentage': 0.05815487321408708, u'id': u'Modesty', u'sampling_error': 0.0556717646, u'name': u'Modesty'}, {u'category': u'personality', u'percentage': 0.11720116905729666, u'id': u'Morality', u'sampling_error': 0.0625894515, u'name': u'Uncompromising'}, {u'category': u'personality', u'percentage': 0.3207260700705391, u'id': u'Sympathy', u'sampling_error': 0.0970925806, u'name': u'Sympathy'}, {u'category': u'personality', u'percentage': 0.47806590347386163, u'id': u'Trust', u'sampling_error': 0.0553576464, u'name': u'Trust'}]}, {u'category': u'personality', u'name': u'Emotional range', u'sampling_error': 0.090314624, u'id': u'Neuroticism', u'percentage': 0.667735929981205, u'children': [{u'category': u'personality', u'percentage': 0.7774067071004327, u'id': u'Anger', u'sampling_error': 0.0936568238, u'name': u'Fiery'}, {u'category': u'personality', u'percentage': 0.3886185204935827, u'id': u'Anxiety', u'sampling_error': 0.0547874561, u'name': u'Prone to worry'}, {u'category': u'personality', u'percentage': 0.7194334816969192, u'id': u'Depression', u'sampling_error': 0.0583330975, u'name': u'Melancholy'}, {u'category': u'personality', u'percentage': 0.17749794149692444, u'id': u'Immoderation', u'sampling_error': 0.0524962982, u'name': u'Immoderation'}, {u'category': u'personality', u'percentage': 0.7703591896194476, u'id': u'Self-consciousness', u'sampling_error': 0.056242027199999996, u'name': u'Self-consciousness'}, {u'category': u'personality', u'percentage': 0.3260736934797625, u'id': u'Vulnerability', u'sampling_error': 0.085098268, u'name': u'Susceptible to stress'}]}], u'id': u'Agreeableness_parent', u'name': u'Agreeableness'}], u'id': u'personality', u'name': u'Big 5'}, {u'children': [{u'category': u'needs', u'percentage': 0.010960800518491187, u'children': [{u'category': u'needs', u'percentage': 0.5830056155894936, u'id': u'Challenge', u'sampling_error': 0.0829107407, u'name': u'Challenge'}, {u'category': u'needs', u'percentage': 0.010960800518491187, u'id': u'Closeness', u'sampling_error': 0.0819215822, u'name': u'Closeness'}, {u'category': u'needs', u'percentage': 0.6411549905007771, u'id': u'Curiosity', u'sampling_error': 0.11854519570000001, u'name': u'Curiosity'}, {u'category': u'needs', u'percentage': 0.41354862428599376, u'id': u'Excitement', u'sampling_error': 0.1075390888, u'name': u'Excitement'}, {u'category': u'needs', u'percentage': 0.14583986827584094, u'id': u'Harmony', u'sampling_error': 0.1077322874, u'name': u'Harmony'}, {u'category': u'needs', u'percentage': 0.4294370715231829, u'id': u'Ideal', u'sampling_error': 0.0973316528, u'name': u'Ideal'}, {u'category': u'needs', u'percentage': 0.5040944353155962, u'id': u'Liberty', u'sampling_error': 0.1437423158, u'name': u'Liberty'}, {u'category': u'needs', u'percentage': 0.07592357514233677, u'id': u'Love', u'sampling_error': 0.0988457966, u'name': u'Love'}, {u'category': u'needs', u'percentage': 0.8838878891397461, u'id': u'Practicality', u'sampling_error': 0.08549209719999999, u'name': u'Practicality'}, {u'category': u'needs', u'percentage': 0.2866535707818255, u'id': u'Self-expression', u'sampling_error': 0.0802637708, u'name': u'Self-expression'}, {u'category': u'needs', u'percentage': 0.21523624827253313, u'id': u'Stability', u'sampling_error': 0.10463181290000001, u'name': u'Stability'}, {u'category': u'needs', u'percentage': 0.4881421773591044, u'id': u'Structure', u'sampling_error': 0.07845525719999999, u'name': u'Structure'}], u'id': u'Closeness_parent', u'name': u'Closeness'}], u'id': u'needs', u'name': u'Needs'}, {u'children': [{u'category': u'values', u'percentage': 0.08702916521938431, u'children': [{u'category': u'values', u'percentage': 0.08702916521938431, u'id': u'Conservation', u'sampling_error': 0.0670804621, u'name': u'Conservation'}, {u'category': u'values', u'percentage': 0.31604185182307143, u'id': u'Openness to change', u'sampling_error': 0.0639597739, u'name': u'Openness to change'}, {u'category': u'values', u'percentage': 0.2067499506703584, u'id': u'Hedonism', u'sampling_error': 0.13607386159999998, u'name': u'Hedonism'}, {u'category': u'values', u'percentage': 0.692194280203325, u'id': u'Self-enhancement', u'sampling_error': 0.1017942103, u'name': u'Self-enhancement'}, {u'category': u'values', u'percentage': 0.18137151033986848, u'id': u'Self-transcendence', u'sampling_error': 0.0794188389, u'name': u'Self-transcendence'}], u'id': u'Conservation_parent', u'name': u'Conservation'}], u'id': u'values', u'name': u'Values'}], u'id': u'r', u'name': u'root'}
 word_count 801
 processed_lang en
 source *UNKNOWN*
sid *UNKNOWN*orted_result = sorted(compared_results.items(), key=operator.itemgetter(1))
for keys, value in sorted_result[:5]:
    print keys,
    print(user[keys]),
    print ('->'),
    print (celebrity[keys]),
    print ('->'),
    print (compared_results[keys])
'''
