import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def protrusion(path):
  roughness = max(np.abs(path[:,0]))
  return roughness

def get_angle(points):
  # points is an array of ordered coordinates which constitute the longest path
  angles = []
  for i in range(len(points) -2):
    v_1 = np.array(points[i]) - np.array(points[i+1])
    v_2 = np.array(points[i+2]) - np.array(points[i+1])

    costheta = np.dot(v_1,v_2) / (np.linalg.norm(v_1,2)*np.linalg.norm(v_2,2))
    angles.append(np.arccos(costheta))
  return(angles)
