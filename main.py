'''
Author: Muhammad Ahmed
Location: Living in 5D
Hobby: Writing code for people in 3D
'''
def Sq_STUDENTID(M, N):
  '''
  Generate N many random points on a square where
  Each side should have N/4 points randomly locatd on that side
  One corner of the square is at the origin, i.e. (0,0)
  where as the opposite corner from the origin is at M = [x,y]
  return D as a numpy array where D is 2xN
  '''
  import numpy as np
  D = np.zeros((2,N))
  origin = [0,0]
  #calculating the centre using the origin and the M coordinate
  x_c = (0 + M[0])/2
  y_c = (0 + M[1])/2
  #Moving origin to the x_c and y_c and calculating the new points already know with respect to the new shifted origin , i calculated just for my
  # understanding they are not used in computing x_3, y_3 and x_4 , y_4
  origin_new = np.array([ 0-x_c, 0-y_c ])
  M_new = np.array([M[0]-x_c , M[1]-y_c ])
  #rotating the origin and M by 90 degrees to find the other two corners of the square and moving it back to the original origin we had at the start
  [x_3,y_3] = np.array([y_c-0+x_c,0-x_c+y_c])
  [x_4,y_4] = np.array([y_c-M[1]+x_c,M[0]-x_c+y_c])

  # so basically side 1 is from 0,0 to x_3,y_3 , first i generate random numbers of the size specified by N
  garbage = np.random.rand(int(N/4))
  x_line_1 = x_3*garbage           #y=0 const
  y_line_1 = y_3*garbage
  points_1= np.vstack((x_line_1,y_line_1))

  # I realied that using the same random numbers does not produce the result so for plotting each line i am regenerated the numbers
  garbage = np.random.rand(int(N/4))

  # this line is from x_3,y_3 to M[0],M[1]
  y_line_2 =  y_3 + garbage * (M[1]-y_3) #x=x_3 const
  x_line_2 =  x_3 + garbage * (M[0]-x_3)
  points_2= np.vstack((x_line_2,y_line_2))

  garbage = np.random.rand(int(N/4))
  #this line is from (M[0],M[1]) to (x_4,y_4)
  x_line_3 = M[0] - (garbage * (M[0]-x_4))
  y_line_3 = M[1] - (garbage * (M[1]-y_4))
  points_3= np.vstack((x_line_3,y_line_3))

  garbage = np.random.rand(int(N/4))
  #this line is from (x_4,y_4) to (0,0)
  y_line_4 = garbage * (y_4)
  x_line_4 = garbage * (x_4)
  points_4= np.vstack((x_line_4,y_line_4))

  D = np.hstack((points_1,points_2,points_3,points_4))
  return D
