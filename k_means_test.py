from numpy import *
# K-means Algorithm

def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine)
        dataMat.append(fltLine)
    return dataMat

# compute Euclidean distance
def distEclud(vecA,vecB):
    return sqrt(sum(power(vecA-vecB,2)))

# create K centroids randomly (keep centroids in data boundary)

def randCent(dataSet,k):
    n = shape(dataSet)[1] # get the dimensions of the data
    centroids = mat(zeros(k,n)) # init a k*n matrix
    for j in range(n):
        minJ = min(dataSet[:,j]) # get the min of the row
        rangeJ = float(max(dataSet[:,j]) - minJ) #get the range of the row data
        centroids[:,j] = minJ + rangeJ*random.rand(k,1)
    return centroids

def kMeans(dataSet,k,distMeans = distEclud,createCent = randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))
    centroids = createCent(dataSet,k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf;minIndex = -1
            for j in range(k):
                distJI = distMeans(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI;minIndex = j
        if clusterAssment[i,0] != minIndex:clusterChanged = True
        clusterAssment[i,:] = minIndex,minDist**2
    print(centroids)
    for cent in range(k):
        ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
    return centroids,clusterAssment


