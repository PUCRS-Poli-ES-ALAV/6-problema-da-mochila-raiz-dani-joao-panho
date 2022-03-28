itr = 0

s1 = "Casablanca"
s2 = "Portentoso"

s3 = "Maven, a Yiddish word meaning accumulator of knowledge, began as an attempt to " + "simplify the build processes in the Jakarta Turbine project. There were several" + " projects, each with their own Ant build files, that were all slightly different." +"JARs were checked into CVS. We wanted a standard way to build the projects, a clear "+ "definition of what the project consisted of, an easy way to publish project information" +"and a way to share JARs across several projects. The result is a tool that can now be" +"used for building and managing any Java-based project. We hope that we have created " +"something that will make the day-to-day work of Java developers easier and generally help " +"with the comprehension of any Java-based project.";
s4 = "This post is not about deep learning. But it could be might as well. This is the power of " +"kernels. They are universally applicable in any machine learning algorithm. Why you might" +"ask? I am going to try to answer this question in this article." + "Go to the profile of Marin Vlastelica Pogančić" + "Marin Vlastelica Pogančić Jun";

def dist_pd(string1,string2):
    global itr
    
    size1 = len(string1)
    size2 = len(string2)
    
    matrix = [ [ 0 for i in range(size2 + 1) ] for j in range(size1 + 1) ]

    for i in range(1, size1+1):
        matrix[i][0] = matrix[i-1][0] + 1
        itr += 1

    for j in range(1, size2+1):
        matrix[0][j] = matrix[0][j-1] + 1
        itr += 1

    for i in range(1, size1+1): 
        for j in range(1, size2+1):
            itr += 1
            custoExtra = 1
            if string1[i - 1] == string2[j - 1] :
                custoExtra = 0
            matrix[i][j] = min(matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + custoExtra)

    return matrix

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in dist_pd(s3, s4)]))
print(f"iterations: {itr}")
# s1 e s2 = 120 iterations
# s3 e s4 = 228641 iterations