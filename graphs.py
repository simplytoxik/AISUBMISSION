def graphs():

    import matplotlib.pyplot as plt  # Import matplotlib for plotting and visualization
    import seaborn as sns  # Import seaborn for advanced statistical data visualization
    import pandas as pd  # Import pandas for data manipulation and analysis
    import numpy as np  # Import numpy for numerical operations (not used in this code)

    # Load the dataset from a CSV file into a DataFrame
    df = pd.read_csv('riyal_data.csv')

    # Set the style for seaborn plots
    sns.set(style="darkgrid")

    #-------------------------------------------------------------------------------------------------------------------------------------------------------

    # Age-wise Distribution of genders
    # HISTPLOT
    plt.figure(figsize=(12, 8))  # Create a new figure with specified size for the plot

    # Create the histogram with Kernel Density Estimate (KDE), adjusting color and bins
    ax = sns.histplot(df['Age'], kde=True, color='skyblue', bins=25, edgecolor='black', linewidth=1.2)

    # Set the title of the graph
    plt.title('Age Distribution of Patients', fontsize=18, fontweight='bold')

    # Label the x and y axes with larger font size
    plt.xlabel('Age', fontsize=14, fontweight='bold')
    plt.ylabel('Frequency', fontsize=14, fontweight='bold')

    # Increase the font size of ticks for both x and y axes
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # Add gridlines for better readability
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')

    # Adjust the layout to make sure everything fits without overlap
    plt.tight_layout()

    # Show the plot
    plt.show()

    #-------------------------------------------------------------------------------------------------------------------------------------------------------

    # Diagnosis Count by Gender 
    # COUNTPLOT
    plt.figure(figsize=(14, 8))  # Create a new figure with specified size for the plot

    # Create the countplot with 'hue' for gender differentiation
    ax = sns.countplot(x='Diagnosis', hue='Gender', data=df, palette='Set2', dodge=True)

    # Set the title of the plot with larger font size and bold
    plt.title('Diagnosis Count by Gender', fontsize=18, fontweight='bold')

    # Label the axes with larger font size and bold
    plt.xlabel('Diagnosis', fontsize=14, fontweight='bold')
    plt.ylabel('Count', fontsize=14, fontweight='bold')

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45, ha='right', fontsize=12)

    # Customize the legend for better readability and positioning
    plt.legend(title='Gender', fontsize=12, title_fontsize=14, loc='upper right')

    # Add gridlines for better visibility of the counts
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')

    # Remove top and right spines for a cleaner look
    sns.despine()

    # Adjust layout to ensure everything fits without overlap
    plt.tight_layout()

    # Show the plot
    plt.show()

    #-------------------------------------------------------------------------------------------------------------------------------------------------------

    # Blood Pressure Distribution (Systolic and Diastolic)
    # BOXPLOT
    # Uncomment the following lines to enable the boxplot for blood pressure distribution

    # plt.figure(figsize=(14, 8))  # Create a new figure with specified size for the boxplot

    # Create the boxplot with a better color palette
    # ax = sns.boxplot(data=df[['Systolic', 'Diastolic']], palette='coolwarm', width=0.5)

    # Add a title with larger font size and bold
    # plt.title('Blood Pressure Distribution (Systolic and Diastolic)', fontsize=18, fontweight='bold')

    # Label the axes with larger font size and bold
    # plt.xlabel('Blood Pressure', fontsize=14, fontweight='bold')
    # plt.ylabel('Pressure Value (mmHg)', fontsize=14, fontweight='bold')

    # Customize tick labels
    # plt.xticks(fontsize=12)
    # plt.yticks(fontsize=12)

    # Add gridlines behind the plot to enhance readability
    # plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')

    # Remove top and right spines for a cleaner look
    # sns.despine()

    # Adjust the layout to ensure it fits within the figure
    # plt.tight_layout()

    # Show the plot
    # plt.show()

    #-------------------------------------------------------------------------------------------------------------------------------------------------------

    # Height vs. Weight
    # Height vs. Weight
    # SCATTERPLOT
    plt.figure(figsize=(10, 6))  # Create a new figure with specified size for the scatter plot

    # Create a scatter plot with height vs. weight, colored by gender
    sns.scatterplot(x='Height', y='Weight', data=df, hue='Gender', palette='muted', alpha=0.7, size='Age', sizes=(20, 200))  # Plot height vs. weight with gender differentiation and size based on age

    # Set the title of the scatter plot
    plt.title('Height vs. Weight', fontsize=18, fontweight='bold')  # Title for the scatter plot

    # Show the plot
    plt.show()

    #-------------------------------------------------------------------------------------------------------------------------------------------------------

    # Diagnosis Count
    # COUNTPLOT
    sns.set(style="whitegrid", palette="muted")  # Set the style for seaborn plots

    plt.figure(figsize=(14, 8))  # Create a new figure with specified size for the count plot
    ax = sns.countplot(x='Diagnosis', data=df, palette='Set1')  # Create a count plot for the diagnosis

    # Set the title of the count plot
    plt.title('Number of Patients by Diagnosis', fontsize=18, fontweight='bold')  # Title for the count plot

    # Label the axes with larger font size and bold
    plt.xlabel('Diagnosis', fontsize=14, fontweight='bold')  # X-axis label
    plt.ylabel('Number of Patients', fontsize=14, fontweight='bold')  # Y-axis label

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45, ha='right', fontsize=12)  # Adjust x-axis labels

    # Annotate each bar with the corresponding count value
    for p in ax.patches:  # Iterate over each bar in the count plot
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),  # Annotate the height of each bar
                    ha='center', va='center', fontsize=12, color='black', xytext=(0, 5), textcoords='offset points')  # Position the annotation

    # Add gridlines for better visibility of the counts
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')  # Add gridlines

    # Remove top and right spines for a cleaner look
    sns.despine()  # Clean up the plot appearance

    # Adjust layout to ensure everything fits without overlap
    plt.tight_layout()  # Adjust layout

    # Show the plot
    plt.show()  # Display the count plot ```python
    import matplotlib.pyplot as plt  # Import matplotlib for plotting and visualization
    import seaborn as sns  # Import seaborn for advanced statistical data visualization
    import pandas as pd  # Import pandas for data manipulation and analysis
    import numpy as np  # Import numpy for numerical operations (not used in this code)

    # Load the dataset from a CSV file into a DataFrame
    df = pd.read_csv('riyal_data.csv')

    # Set the style for seaborn plots
    sns.set(style="darkgrid")

    #-------------------------------------------------------------------------------------------------------------------------------------------------------

    # Age-wise Distribution of genders
    # HISTPLOT
    plt.figure(figsize=(12, 8))  # Create a new figure with specified size for the plot

    # Create the histogram with Kernel Density Estimate (KDE), adjusting color and bins
    ax = sns.histplot(df['Age'], kde=True, color='skyblue', bins=25, edgecolor='black', linewidth=1.2)

    # Set the title of the graph
    plt.title('Age Distribution of Patients', fontsize=18, fontweight='bold')

    # Label the x and y axes with larger font size
    plt.xlabel('Age', fontsize=14, fontweight='bold')
    plt.ylabel