import requests
from bs4 import BeautifulSoup
import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np



for c in range(1,91):
    with open("Chhattisgarh"+str(c)+".csv", 'r') as f:
        var = [];
        c_name = [];
        p_name = [];
        votes = [];
        var = csv.reader(f, delimiter=",");
        for i in var:
            if len(i) is not 0:
                c_name.append(i[0]);
                p_name.append(i[1]);
                votes.append(int(i[2]));

        fig = plt.figure()
        index = np.arange(len(c_name))
        plt.bar(c_name, votes,color=['black', 'red', 'green', 'blue', 'cyan']);
        plt.xlabel('Candidate_name');
        plt.ylabel('No of Votes');
        plt.xticks(index,c_name, fontsize=5, rotation=70)
        plt.title('Constituency- wise results')
        #plt.show()
        plt.savefig("Chhattisgarh"+str(c)+".png");
        plt.clf()



for c1 in range(1,231):
    with open("Madhya Pradesh"+str(c1)+".csv", 'r') as f:
        var = [];
        c_name = [];
        p_name = [];
        votes = [];
        var = csv.reader(f, delimiter=",");
        for i in var:
            if len(i) is not 0:
                c_name.append(i[0]);
                p_name.append(i[1]);
                votes.append(int(i[2]));

        fig = plt.figure()
        index = np.arange(len(c_name))
        plt.bar(c_name, votes,color=['black', 'red', 'green', 'blue', 'cyan']);
        plt.xlabel('Candidate_name');
        plt.ylabel('No of Votes');
        plt.xticks(index,c_name, fontsize=5, rotation=70)
        plt.title('Constituency- wise results')
        #plt.show()
        plt.savefig("Madhya Pradesh"+str(c1)+".png");
        plt.clf()

for c2 in range(1,41):
    with open("Mizoram"+str(c2)+".csv", 'r') as f:
        var = [];
        c_name = [];
        p_name = [];
        votes = [];
        var = csv.reader(f, delimiter=",");
        for i in var:
            if len(i) is not 0:
                c_name.append(i[0]);
                p_name.append(i[1]);
                votes.append(int(i[2]));

        fig = plt.figure()
        index = np.arange(len(c_name))
        plt.bar(c_name, votes,color=['black', 'red', 'green', 'blue', 'cyan']);
        plt.xlabel('Candidate_name');
        plt.ylabel('No of Votes');
        plt.xticks(index,c_name, fontsize=5, rotation=70)
        plt.title('Constituency- wise results')
        #plt.show()
        plt.savefig("Mizoram"+str(c2)+".png");
        plt.clf()


for c3 in range(1,201):
    with open("Rajasthan"+str(c3)+".csv", 'r') as f:
        var = [];
        c_name = [];
        p_name = [];
        votes = [];
        var = csv.reader(f, delimiter=",");
        for i in var:
            if len(i) is not 0:
                c_name.append(i[0]);
                p_name.append(i[1]);
                votes.append(int(i[2]));

        fig = plt.figure()
        index = np.arange(len(c_name))
        plt.bar(c_name, votes,color=['black', 'red', 'green', 'blue', 'cyan']);
        plt.xlabel('Candidate_name');
        plt.ylabel('No of Votes');
        plt.xticks(index,c_name, fontsize=5, rotation=70)
        plt.title('Constituency- wise results')
        #plt.show()
        plt.savefig("Rajasthan"+str(c3)+".png");
        plt.clf()


for c4 in range(1,120):
    with open("Telangana"+str(c4)+".csv", 'r') as f:
        var = [];
        c_name = [];
        p_name = [];
        votes = [];
        var = csv.reader(f, delimiter=",");
        for i in var:
            if len(i) is not 0:
                c_name.append(i[0]);
                p_name.append(i[1]);
                votes.append(int(i[2]));

        fig = plt.figure()
        index = np.arange(len(c_name))
        plt.bar(c_name, votes,color=['black', 'red', 'green', 'blue', 'cyan']);
        plt.xlabel('Candidate_name');
        plt.ylabel('No of Votes');
        plt.xticks(index,c_name, fontsize=5, rotation=70)
        plt.title('Constituency- wise results')
        plt.savefig("Telangana"+str(c4)+".png");
        plt.clf()