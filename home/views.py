from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd
import numpy as np
import seaborn as sns

import plotly.express as px
from plotly.offline import plot
from plotly.graph_objs import Scatter

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')

def compound_interest(request):
  # x_data = [0,1,2,3]
  # y_data = [x**2 for x in x_data]
  # plot_div = plot([Scatter(x=x_data, y=y_data,
  #                       mode='lines', name='test',
  #                       opacity=0.8, marker_color='green')],
  #              output_type='div')

  P = 10000 # The Starting Principal
  r = 0.10 # The Annual Interest Rate to Compound On 10%
  n = 12 # The Number of Months in a Year
  t = 20 # The Number of Years to Compound
  M = 500 # Monthly Contribution Amount

  # Calculate the End of Year Balance for Each Year

  # Prepare a DataFrame to store the Year and Final Balance
  results = pd.DataFrame(columns = ['Year', 'Principal', 'Interest', 'Amount'])

  # Iterate through each year to find the ending balance
  # then append it to the results DataFrame
  Principal = P
  for i in range(1,t+1):
    Year = i
    Amount = P*np.power((1 + r / n), n * i)+(M)*(np.power((1+ r / n ), n * i)-1)/(r / n)
    Principal = Principal + M*12
    results = pd.concat([results, pd.DataFrame([{'Year': Year, 'Principal': Principal, 'Interest': Amount-Principal, 'Amount': Amount}])], ignore_index=True)
  #   results =  results.append({'Year': Year, 'Amount': Amount}, ignore_index = True)

  # Our Year's data type needs to be an integer not a float
  results['Year'] = results['Year'].astype('int')
  results['Principal'] = results['Principal'].astype('float64')
  print('results: {}'.format(results))

  # Plot it Out

  # fig = px.line(results, title='Compound Interest Plot ({:.2%} Return, {:,.2f} Principal, {:,.2f} Contribution)'.format(r, P, M))
  fig = px.bar(results, height=500, x='Year', y=["Principal", "Interest"], title='Compound Interest Plot ({:.2%} Return, {:,.2f} Principal, {:,.2f} Contribution)'.format(r, P, M))
  plot_div = plot(fig, output_type='div')
  return render(request, 'components/compound-interest.html', context={'plot_div': plot_div})

