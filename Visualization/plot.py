import plotly.plotly as py
import plotly.graph_objs as go

import igraph
from igraph import *

def plot(tree_dict):
  """

  :param tree_dict: dictionary like spanning_tree.SPANNING_INFO
  :return:
  """
  nr_vertices = len(tree_dict)

  v_label = map(str, range(nr_vertices))
  G = Graph.Tree(nr_vertices, 2)  # 2 stands for children number
  # lay = G.layout('lgl')
  lay = G.layout('sugiyama')


  position = {k: lay[k] for k in range(nr_vertices)}
  Y = [lay[k][1] for k in range(nr_vertices)]
  M = max(Y)

  es = EdgeSeq(G)  # sequence of edges
  E = [e.tuple for e in G.es]  # list of edges

  L = len(position)
  Xn = [position[k][0] for k in range(L)]
  Yn = [2 * M - position[k][1] for k in range(L)]

  labels = v_label

  # print pp.pprint(Xe)
  # print pp.pprint(Ye)
  for i in xrange(len(Xn)):
    print (i, Xn[i], Yn[i])

  ## Create Plotly Traces
  # lines = go.Scatter(x=Xe,
  #                    y=Ye,
  #                    mode='lines',
  #                    line=dict(color='rgb(210,210,210)', width=1),
  #                    hoverinfo='none'
  #                    )
  dots = go.Scatter(x=Xn,
                    y=Yn,
                    mode='markers',
                    name='',
                    marker=dict(symbol='dot',
                                size=18,
                                color='#6175c1',  # '#DB4551',
                                line=dict(color='rgb(50,50,50)', width=1)
                                ),
                    text=labels,
                    hoverinfo='text',
                    opacity=0.8
                    )

  ## Create Text Inside the Circle via Annotations
  # def make_annotations(pos, text, font_size=10, font_color='rgb(250,250,250)'):
  #   L = len(pos)
  #   if len(text) != L:
  #     raise ValueError('The lists pos and text must have the same len')
  #   annotations = go.Annotations()
  #   for k in range(L):
  #     annotations.append(
  #       go.Annotation(
  #         text=labels[k],  # or replace labels with a different list for the text within the circle
  #         x=pos[k][0], y=2 * M - position[k][1],
  #         xref='x1', yref='y1',
  #         font=dict(color=font_color, size=font_size),
  #         showarrow=False)
  #     )
  #   return annotations

  ## Add Axis Specifications and Create the Layout
  axis = dict(showline=False,  # hide axis line, grid, ticklabels and  title
              zeroline=False,
              showgrid=False,
              showticklabels=False,
              )

  layout = dict(title='Tree with Reingold-Tilford Layout',
                # annotations=make_annotations(position, v_label),
                font=dict(size=12),
                showlegend=False,
                xaxis=go.XAxis(axis),
                yaxis=go.YAxis(axis),
                margin=dict(l=40, r=40, b=85, t=100),
                hovermode='closest',
                plot_bgcolor='rgb(248,248,248)'
                )

  ## Plot!
  # data = go.Data([lines, dots])
  data = go.Data([dots])
  fig = dict(data=data, layout=layout)
  # fig['layout'].update(annotations=make_annotations(position, v_label))
  py.iplot(fig, filename='Tree-Reingold-Tilf_1')

if __name__ == '__main__':
  d = {}
  for i in xrange(25):
    d[i] = i
  plot(d)