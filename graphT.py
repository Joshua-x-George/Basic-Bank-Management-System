def main():
    listg = []
    scale = int(input("Enter the y scale for the graph: "))
    nos = int(input("Enter the number of points to be plotted: "))
    for i in range(1,nos+1):
        listg.append(float(input("Enter a number for x-point "+ str(i)+ ": ")))
    plotgraph(listg,scaley=scale)

def plotgraph(lst,scaley=1):
    
    #to generate points in list of tuples ie ()
    points=[ (i+1,lst[i]) for i in range(len(lst))]
    
    maxunitX = len(points)+1
    negativeValues = True if min(lst) < 0 else False
    scalex = 1#pass need to implement scalex later; scale x is set to 1 for now
    
    #previous & xpoint for the point plotting functionality
    previous = 0
    xpoint = 0
    
    maxunitY = int(max(lst))+ 2 * scaley
    minunitY = int(min(lst))-scaley
    
    #to correct the y axis number to scale
    if minunitY%scaley != 0:
        minunitY -= minunitY%scaley
    
    #pass changeable to your ide config
    tabspace = 8
    
    print("   ↑")
    #to correct for y axis when 0 is present in points
    if not negativeValues:
        minunitY = minunitY+scaley if minunitY+scaley == 0 else minunitY

    for i in reversed(range(scaley if negativeValues else minunitY+scaley,maxunitY,scaley)):
        print(f"{i:03}│",end ='')
        for inde in range(len(points)):
            if points[inde][1] == i or points[inde][1] >= i-scaley/2 and points[inde][1] < i or points[inde][1] < i + scaley/2 and points[inde][1] > i:
                previous = xpoint
                xpoint = points[inde][0]
                
                for x in range(1,xpoint+1-previous):
                    print('\t',end = '')
                print("*",end = '')
        xpoint = 0
        print()
        for j in range(int(tabspace/4)):
            print('   │')
            
    #prints the -ve part of the graph
    if negativeValues:
        print('  0├',end = '')
        for i in reversed(range(1,maxunitX+1)):
            print('─'*tabspace,end = '')
        print('>\n','   │    '*scalex,sep='',end = '')
        for i in range(scalex,maxunitX+1,scalex):
            print(f"{i:02}",end = '\t'*scalex)
        print("\n   │")
        for i in range(-1*scaley,minunitY-scaley,-1*scaley):
            print(f"{i:03}│",end ='')
            for inde in range(len(points)):
                if points[inde][1] == i or points[inde][1] <= i+scaley/2 and points[inde][1] > i or points[inde][1] > i - scaley/2 and points[inde][1] < i:
                    previous = xpoint
                    xpoint = points[inde][0]
                    for x in range(1,xpoint+1-previous):
                        print("\t",end = '')
                    print("*",end = '')
            xpoint = 0
            print()
            for j in range(int(tabspace/4)):
                print('   │')
        print("   ↓")
    else:  
        print('  0└',end = '')
        for i in reversed(range(1,maxunitX+1)):
            print('─'*tabspace,end = '')
        print('>\n','\t'*scalex,sep='',end = '')
        
        for i in range(scalex,maxunitX+1,scalex):
            print(f"{i:02}",end = '\t'*scalex)
        print()
