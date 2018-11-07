import facebook

token = "EAAasGZCoDZAoABAEj2ZC3b0ZANpU8OQIBXVll1vieVf7uRdZADSiiWNe8cny42WuZA7JCxNbsn7sJh4FzvtQ1zPrCCsFLCNncFzVRLZAhCU4iNZCNk2HZBaAXRt2M76NsTSaydzpFLs1TkZBffTMthKNrUG178EwN0ANn76vp14SAuxwZDZD"
graph = facebook.GraphAPI(token)
args = {'fields' : ['first_name','last_name','friends'] }
friends = graph.get_object("me/friends",**args)
print(friends)