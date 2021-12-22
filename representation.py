import dash
import dash_html_components as html
import dash_cytoscape as cyto
import pprint
app = dash.Dash(__name__)

G = dict()
# G['a'] = ['b','c']
# G['b'] = ['a','d','e']
# G['c'] = ['a','d']
# G['d'] = ['b','c','e']
# G['e'] = ['b','d','f','g']
# G['f'] = ['e','g']
# G['g'] = ['e','f','h']
# G['h'] = ['g']
G ={'b': [None], 'a': ['b'], 'd': ['b'], 'e': ['b'], 'c': ['a'], 'f': ['e'], 'g': ['e'], 'h': ['g']}

elements=[]

#Conversion des dictionnaires
def convertgraph(G):
    #Préparation des noeuds
    for key in G.keys():    
        elements.append({ 'data' : {'id': key, 'label': key.upper()}})

    #Préparation des liaisons
    for key, value in G.items():
        for i in value:            
            if value!=[None]:                
                elements.append({ 'data' : {'source': key, 'target': i}})
    return(elements)

pprint.pprint(convertgraph(G))

app.layout = html.Div([
    html.P("MPDSIR", id="wael"),
    cyto.Cytoscape(
        id='cytoscape',
        elements= convertgraph(G),
        layout={'name': 'breadthfirst'},
        style={'width': '500px', 'height': '500px'}
    )
])


app.run_server(debug=True)