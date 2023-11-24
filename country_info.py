from dash import dash,html,dcc,Input,Output
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px


data = px.data.gapminder()

print(data)

app = dash.Dash()


app.layout = html.Div([
    
    
    html.Br(),
    
    html.H1('Global Countries Economic Date Dashboard',style={'textAlign':'center'}),
    
    
    html.Div([
        html.H3("Select Country"),
        
        dcc.Dropdown(id='country-filture',options=[country for country in data['country'].unique()],value='India',style={'width':250}),
        html.Br(),

        ]),
    dcc.Tabs(            
                children=[dcc.Tab(label='Population Summary',value=1),
                          dcc.Tab(label='GDP Per Capita Summary',value=2),
                          dcc.Tab(label='Life Expectancy Summary',value=3)],
                
                id = 'tab-selected',value=1),
                     
    html.Div([
        
        dcc.Graph(id='chart-1')
        
    ])


])

@app.callback(Output('chart-1','figure'),
              [Input('tab-selected','value'),Input('country-filture','value')])

def chart_generator(tab,country):
    
    filtured_data = data[data['country']==country]
    
    if tab == 1:
                
        return {'data':[go.Line(x=filtured_data['year'],y=filtured_data['pop'])],
                'layout':go.Layout(title=f'Population Summary Chart : {country}',height=600)}

    elif tab == 2:
               
        return {'data':[go.Line(x=filtured_data['year'],y=filtured_data['gdpPercap'])],
                'layout':go.Layout(title=f'GDP Per Capita Summary Chart : {country}',height=600)}

    else:
        
        return {'data':[go.Line(x=filtured_data['year'],y=filtured_data['lifeExp'])],
                'layout':go.Layout(title=f'Life Expectancy Summary Chart : {country}',height=600)}
        




if __name__ == '__main__':
    app.run_server()