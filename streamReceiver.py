import sys
import re

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":

    sc = SparkContext(appName="Web Log Analysis")
    sc.setLogLevel("ERROR")
    ssc = StreamingContext(sc, 10)

    host = "localhost"
    port = 9998

    lines = ssc.socketTextStream(host, int(port))

    dataRDD = lines.flatMap(lambda line: line.split("\n"))
    pattern = '(\S+) - - \[(\S+) (\S+)\] "(\S+) \S+ \S+" (\d+) (\d+) "(\S+)" "(.*)"'
    formatRDD = dataRDD.map(lambda line: list(re.findall(pattern,line)[0]))
    filterRDD = formatRDD.filter(lambda line : line[4] == '404')
    filterRDD.pprint()

    ssc.start()

    try:
        ssc.awaitTermination()
    except KeyboardInterrupt:
        ssc.stop()
        sc.stop()

