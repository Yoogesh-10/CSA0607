from graph_coloring import graph_coloring
# Same size (8 vertices), same k=4. Easy: sparse path. Harder: K5 plus isolated vertices
vertices=list(range(8))
easy_edges=[(i,i+1) for i in range(7)]
hard_edges=[(i,j) for i in range(5) for j in range(i+1,5)]
for label,edges in [("Graph A - Path P8",easy_edges),("Graph B - K5 + 3 isolated",hard_edges)]:
    print("\\n",label)
    ok,col,stats=graph_coloring(vertices,edges,4,order="input")
    print("Result:",ok,"Coloring:",col)
    print("Measured search:",stats)
print("\\nPrediction: Graph B has higher degree and more constraints, but Graph B is uncolourable.")
print("Interpretation: for these instances the input-order heuristic must exhaust the K5 search.")
