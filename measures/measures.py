import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

## Some path measures for the 1+1D model. 

def protrusion(path):
  # the 1+1D maximum absolute x distance in the path. Coords defined: [x, t]
  roughness = max(np.abs(path[:,0]))
  return roughness

def get_angle(points):
  # Gets the array of subsequent angles between nodes in the path. 
  # points is an array of ordered coordinates which constitute the longest path
  angles = []
  for i in range(len(points) -2):
    v_1 = np.array(points[i]) - np.array(points[i+1])
    v_2 = np.array(points[i+2]) - np.array(points[i+1])

    costheta = np.dot(v_1,v_2) / (np.linalg.norm(v_1,2)*np.linalg.norm(v_2,2))
    angles.append(np.arccos(costheta))
  return(angles)

def area(path):
  # Area deviation from the path and the geodesic.
  #path is a list of node co-ords [(x_i,t_i)] of length whatever
  area = 0

  for i in range(len(path)-1):
    #consecutive nodes on same side of geodesic AND start/end nodes
    if path[i][0]*path[i+1][0] >= 0:
      area += 0.5 * abs(path[i][0] + path[i+1][0]) * abs(path[i][1] - path[i+1][1])
    #consecutive nodes on opposite sides of geodesic
    else:
      t_int = path[i][1] - path[i][0]* ((path[i+1][1] - path[i][1]) / (path[i+1][0] - path[i][0]))
      area += 0.5 * abs(path[i][0]) * abs(t_int - path[i][1])
      area += 0.5 * abs(path[i+1][0]) * abs(path[i+1][1] - t_int)
  return area

