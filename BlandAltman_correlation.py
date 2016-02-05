#The following code demonstrates how Python can be used to do Bland-Altan and correlation statistical
#analysis using the numeric python, pyplot and scientific python librarys.  Two different groups of data are
#tested, and each group has two arrays of data that can be compared.  Bland-Altman and correlation analysis is
#often done in medicine to compare one measurement technique with another two see how well they are related and
#how well the two techniques agree with each other.



# Import numeric python library
import numpy as np


#import the Python plotting tool
from matplotlib import pyplot as plt


#Import the stats library from the scipy module
from scipy import stats










#Data group 1
#Create an array with the first dataset of group 1
Data1 = np.array([10.3, 5.1, 3.2, 19.1, 8.1, 11.7, 7.1, 13.9, 4.0, 20.1, 27.5, 6.4, 30.1, 13.0, 10.0,
                        16.8, 17.3, 3.0, 25.6, 19.3, 15.0, 27.3, 14.2, 13.0,14.4, 22.1, 19.0, 18.0, 13.0, 25.6,
                        18.4, 12.6, 25.5, 15.7, 20.2, 16.5, 19.3, 10.0, 18.8, 24.0, 22.8])


#Create an array with the second data set of group 1
Data2 = np.array([8.9, 4.0, 8.1, 21.2, 8.1, 12.0, 4.5, 13.9, 4.0, 20.1, 27.5, 6.4, 40.3, 13.0, 10.0, 32.2,
                          17.1, 9.4, 25.2, 18.8, 15.0, 27.3, 21.3, 13.0, 14.4,22.1, 17.9, 3.0, 13.0, 19.0, 18.4,
                          12.6, 25.5, 15.7, 21.2, 16.5, 19.3, 10.0, 30.8, 9.0, 22.8])








#This is a different group of data, which is the second group.
#Create an array of data set one for the second group
Dataset1 = np.array([10.3, 15.8, 6.4, 20.2, 17.1, 17.1, 21.2, 15.8, 15.0, 10.4, 16.4,
                         21.0, 19.0, 11.2, 10.0, 17.9, 10.2, 21.2, 23.0, 17.5, 8.9, 23.8, 26.1])


#Create an array of data for set two for the second group
Dataset2 = np.array([13.9, 16.8, 3.0, 25.6, 19.3, 15.0, 27.3, 13.0, 22.1, 19.0, 18.0, 13.0,
                           25.6, 18.4, 12.6, 25.5, 15.7, 20.2, 16.5, 19.3, 10.0, 18.8, 22.8])













#Function to create a correlation plot comparing two data sets.
def CorrelationPlot(Xdata, Ydata):


    # Create a matrix for the horizontal axis data for least squares fitting.
    #The T takes the transpose of a matrix and turns horizontal data into
    #columns instead of rows.
    A = np.vstack([Xdata, np.ones(len(Xdata))]).T


    #Calculate the least squares fit of the data. m refers to the slope
    #of the line and b refers to the y-intercept.
    m,b = np.linalg.lstsq(A,Xdata)[0]


    #Calculate the Pearson correlation coefficient and the 2-tailed p-value).
    R_and_P = np.round(stats.pearsonr(Xdata, Ydata),2)


    #Set the axis limits for the plot.  X-range is given followed by Y-range.
    plt.axis([0, (np.max(Xdata)+5), 0, (np.max(Ydata)+5)], fontsize = '16', lw = '2')


    #Plot the data on the correlation plot.
    #Use open circles with no marker face color, no lines, blue edge color, marker edge width of 2, marker size 8
    plt.plot(Xdata, Ydata, marker ='o', mfc = 'none', ls = 'None', mec = 'blue', mew= '2', ms = '8', lw = '2')


    #Plot the least squares fit line
    plt.plot(Xdata, m*Xdata + b , 'k', lw = '2')


    #Horizontal axis label.
    plt.xlabel('Dataset 2', fontsize = '16')


    #Vertical axis label
    plt.ylabel('Dataset 1', fontsize = '16')


    #Change the font size of the tick mark labels to be bigger
    #on both axes.
    plt.tick_params(axis='both', which='major', labelsize= '16', width = '2')


    #This if statement is used to determine the text box on the plot
    #to show the P value beside the r value.  If P is less than 0.01
    #then set the string to show just P < 0.01.  If not, just show the
    #P-value rounded to two decimal places.
    if R_and_P[1] < 0.01:
            P = '(P<0.01)'
    else:
            P = '(P=' + str(R_and_P[1]) + ')'


    #Add a text box with correlation coefficient and p-value
    #on the plot.
    plt.text(2, 28, 'r=' + str(R_and_P[0]) + P, fontsize='16')


    #Another way to set the border thickness.  Get current axes first
    #Then change their thickness using the set_linewidth() command.
    ax =plt.gca()
    ax.spines['top'].set_linewidth('2')
    ax.spines['left'].set_linewidth('2')
    ax.spines['right'].set_linewidth('2')
    ax.spines['bottom'].set_linewidth('2')


    #End the function
    return;









#Function to create a Bland-Altman plot comparing agreement between two data sets.
def BlandAltmanPlot(Xdata, Ydata):


    #Calculate the difference between the CACT and actual angles.  Will create a difference array comparing each angle
    Difference = Ydata - Xdata


    #Calculate the average value of the two datasets for each data point
    Average = (Xdata + Ydata)/2


    #Calculate the mean of the differences.
    Mean_difference = np.mean(Difference)


    #Calculate the sample standard deviation of the difference.
    Std_difference = np.std(Difference)


    #Calculate the upper and lower limits of the agreement (95% confidence).
    upper_limit = Mean_difference + 1.96*Std_difference
    lower_limit = Mean_difference - 1.96*Std_difference


    #Set axis limits, this will account for the maximum average difference and the upper and lower
    #limits of agreement, and all data points.
    plt.axis([0, np.max(Average)+5, np.min(Difference)-5, np.max(Difference)+5],
             fontsize = '16', lw = '2')


    #Do the Bland-Altman plot.
    plt.plot(Average, Difference, marker ='o', mfc = 'none', ls = 'None', mec = 'blue',
             mew= '2', ms = '8', lw = '2')


    #Add the mean, upper and lower levels of agreement to the Bland-Altman plot.
    plt.axhline(y=Mean_difference, lw ='2', color ='k', ls = 'dashed')
    plt.axhline(y=upper_limit,lw ='2', color ='k', ls = 'dashed')
    plt.axhline(y=lower_limit,lw ='2', color ='k', ls = 'dashed')


    #Horizontal axis label
    plt.xlabel('Average difference', fontsize = '16')


    #Vertical axis label
    plt.ylabel('Difference', fontsize = '16')


    #Change the font size of the tick mark labels to be bigger
    #on both axes.
    plt.tick_params(axis='both', which='major', labelsize= '16', width = '2')


    #Another way to set the border thickness.  Get current axes first
    #Then change their thickness using the set_linewidth() command.
    ax1 =plt.gca()
    ax1.spines['top'].set_linewidth('2')
    ax1.spines['left'].set_linewidth('2')
    ax1.spines['right'].set_linewidth('2')
    ax1.spines['bottom'].set_linewidth('2')


    #End the function
    return;











#Plot all the data
#Open up a figure.
plt.figure()



#Open up the subplot
plt.subplot(2,2,1)



#Call the correlation plot of Data1 and Data2 in the first data group.
CorrelationPlot(Data1, Data2)



#Open up another subplot for the Bland-Altman analysis.
plt.subplot(2,2,2)



#Call the Bland-Altman function for Data1 and Data2 in the first data group.
BlandAltmanPlot(Data1, Data2)



#Open up the third subplot
plt.subplot(2,2,3)



#Call the correlation plot function for the data set 1 and data set 2 in the second group
CorrelationPlot(Dataset1, Dataset2)



#Open up the last subplot
plt.subplot(2,2,4)



#Call the Bland-Altman function for data sets 1 and 2 for the second data group.
BlandAltmanPlot(Dataset1, Dataset2)



#Show all the plots at once.
plt.show()











