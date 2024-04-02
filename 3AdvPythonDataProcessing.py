"""
Task 1: Travel Blog Sentiment Analysis:
    - Problem Statement:
        - Perform sentiment analysis on a collection of travel blog entries stored in travel_blogs.txt. Identify and count the occurrences of positive words (e.g., "amazing", "enjoy", "beautiful") and negative words (e.g., "bad", "disappointing", "poor").
    - Expected Outcome:
        - A summary report indicating the number of positive and negative words in the travel blogs, demonstrating the ability to process text data and apply basic sentiment analysis.
"""
import re


# def review_tally():

def analyze_blog_sentiments(blog_file):
    with open(blog_file, 'r') as file:
        reviews = file.read()
        pos_words = re.findall(r"amazing|enjoy|wonderful|breathtaking|stunning|memorable|mesmerizing|excellent|delicious|enlightening|fantastic|unforgetable", reviews)
        neg_words = re.findall(r"disappointing|overcrowded|poor|lackluster|scarce", reviews)
        return len(pos_words), len(neg_words)
        # num_neg = len(neg_words)


if __name__ == "__main__":
    report = analyze_blog_sentiments('travel_blogs.txt')
    print(f"Positive Words: {report[0]}, Negative Words: {report[1]}")


"""
Task 2: Historical Weather Data Compiler
    - Problem Statement:
        - Compile and analyze historical weather data from multiple files (weather_2020.txt, weather_2021.txt, etc.). Each file contains daily temperature data. Calculate the average temperature for each year and identify the year with the highest average.
    - Expected Outcome:
        - An aggregated view of average temperatures for each year and identification of the year with the highest average temperature, showcasing data aggregation and analysis skills.
"""
list_of_files = ['weather_2020.txt', 'weather_2021.txt']


def compile_weather_data(file_list):
    temp_averages = {}
    temp_list = []
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            temp_data = f.read()
            temperatures = re.findall(r"\d{1,}°", temp_data)
            for temp in temperatures:
                no_degree_sign = int(re.sub('°', '', temp))
                temp_list.append(no_degree_sign)
            sum_of_temps = sum(temp_list)
            average = round(sum_of_temps / len(temp_list))
        year = re.sub("weather_|.txt", '', file)
        temp_averages[year] = average
    highest_average = max(temp_averages)
    print(f"Highest Average Temperature: {temp_averages[highest_average]}°C in {highest_average}")
    return temp_averages


if __name__ == "__main__":
    print(compile_weather_data(list_of_files))

