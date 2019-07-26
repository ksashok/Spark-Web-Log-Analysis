# Apache Spark Web Log Analysis

This project is used to monitor the Web log data which is processed by Apache Spark Streaming. The Spark Streaming program would read the logs and searches for 404 as status. If status 404 is found, it would display them on the screen with the details.

Language used   : Python 3.7

Framework       : Apache Spark 2.3

Libraries needed : Pyspark, Requests, Re

# Program setup

## textStream.py
Program which simulates streaming data. The program downloads the web log from proyectossbecorp.com and sends one line of record every 5 seconds.

## streamReceiver.py
This is Apache Spark stream receiver which receives the streaming data of the web log. The streaming process runs every 10 seconds. It uses regular expression to process the line received and filters for 404 error. This new value would be displayed on screen.

# Running the project locally

  - Clone the repository
    ```sh
    git clone https://github.com/ksashok/Spark-Web-Log-Analysis.git
    ```
  - Go to the project folder run the application
    ```sh
    .\run.sh
    ```
  - The program would display the entries which had 404 as error

# Sample Output

```
-------------------------------------------
Time: 2019-07-26 11:24:50
-------------------------------------------
['66.102.8.100', '17/Jan/2019:21:22:33', '-0500', 'GET', '404', '311', '-', 'Mozilla/5.0 (compatible; Google-Site-Verification/1.0)']
['66.102.8.100', '17/Jan/2019:21:22:33', '-0500', 'GET', '404', '311', '-', 'Mozilla/5.0 (compatible; Google-Site-Verification/1.0)']

```